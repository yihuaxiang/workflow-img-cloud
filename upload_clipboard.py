#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import sys
import subprocess
import tempfile
import json
import base64
from datetime import datetime

# Add the lib directory to the Python path
script_dir = os.path.dirname(os.path.abspath(__file__))
lib_dir = os.path.join(script_dir, 'lib')
sys.path.insert(0, lib_dir)

import requests

# Configuration
API_URL = "https://playground.z.wiki/img/upload/base64"

def get_clipboard_content_type():
    """Determine if clipboard contains an image or text"""
    # Check if clipboard contains an image
    result = subprocess.run(['osascript', '-e', 'clipboard info'], 
                           capture_output=True, text=True)
    
    if "«class PNGf»" in result.stdout or "«class TIFF»" in result.stdout:
        return "image"
    else:
        # Check if clipboard contains text
        result = subprocess.run(['osascript', '-e', 'the clipboard as text'], 
                               capture_output=True, text=True)
        if result.stdout.strip():
            return "text"
    
    return None

def get_clipboard_as_base64():
    """Get clipboard content as base64 string"""
    content_type = get_clipboard_content_type()
    
    if content_type == "image":
        # 获取剪贴板图片并转换为 base64
        temp_file = save_clipboard_image_to_temp()
        if not temp_file:
            return None, None
            
        with open(temp_file, 'rb') as f:
            file_data = f.read()
            base64_data = base64.b64encode(file_data).decode('utf-8')
            
        # 清理临时文件
        try:
            os.remove(temp_file)
        except Exception:
            pass
            
        return base64_data, "image"
    elif content_type == "text":
        # 获取剪贴板文本并转换为 base64
        result = subprocess.run(['osascript', '-e', 'the clipboard as text'], 
                               capture_output=True, text=True)
        text = result.stdout
        base64_data = base64.b64encode(text.encode('utf-8')).decode('utf-8')
        return base64_data, "text"
    else:
        return None, None

def save_clipboard_image_to_temp():
    """Save clipboard image to a temporary file and return the filepath"""
    temp_dir = tempfile.gettempdir()
    timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
    filepath = os.path.join(temp_dir, f"clipboard_image_{timestamp}.png")
    
    # 检查剪贴板中的图片类型
    result = subprocess.run(['osascript', '-e', 'clipboard info'], 
                           capture_output=True, text=True)
    
    # 使用 osascript 保存剪贴板图片到文件
    if "«class PNGf»" in result.stdout:
        image_type = "«class PNGf»"
    elif "«class TIFF»" in result.stdout:
        image_type = "«class TIFF»"
    else:
        return None
    
    script = f'''
    set theFile to "{filepath}"
    set theClipboard to the clipboard as {image_type}
    set fileRef to (open for access theFile with write permission)
    write theClipboard to fileRef
    close access fileRef
    '''
    
    try:
        subprocess.run(['osascript', '-e', script], check=True)
        
        # 验证文件是否成功创建
        if os.path.exists(filepath) and os.path.getsize(filepath) > 0:
            return filepath
        else:
            return None
    except subprocess.CalledProcessError:
        return None

def upload_base64_to_api(base64_data, content_type):
    """Upload base64 data to API"""
    try:
        # 为 base64 数据添加前缀，根据内容类型
        if not base64_data.startswith('data:'):
            if content_type == "image":
                base64_data = f"data:image/png;base64,{base64_data}"
            elif content_type == "text":
                base64_data = f"data:text/plain;base64,{base64_data}"
            
        # 尝试使用 data 参数和 base64 键名
        data = {'base64': base64_data}
        print(f"DEBUG - Request data: {data}")
        response = requests.post(API_URL, data=data)
        
        if response.status_code == 200:
            print(f"DEBUG - Response: {response.text}")
            return {"success": True, "data": {"url": response.text.strip()}}
        else:
            # 尝试使用 json 参数
            response_json = requests.post(API_URL, json=data)
            if response_json.status_code == 200:
                return {"success": True, "data": {"url": response_json.text.strip()}}
            
            return {"error": f"API error: {response.status_code}", "details": response.text}
    except Exception as e:
        return {"error": str(e)}

def notify(title, message):
    """Show notification in Alfred"""
    # 使用 Alfred 的正确 JSON 格式
    output = {
        "items": [
            {
                "title": title,
                "subtitle": message,
                "arg": message,
                "text": {
                    "copy": message,
                    "largetype": message
                }
            }
        ]
    }
    # 确保输出是有效的 JSON
    print(json.dumps(output, ensure_ascii=False))
    # 刷新标准输出，确保 Alfred 能立即读取
    sys.stdout.flush()

def main():
    try:
        # 获取剪贴板内容的 base64 编码
        base64_data, content_type = get_clipboard_as_base64()
        
        if not base64_data:
            notify("Error", "Failed to get clipboard content or clipboard is empty")
            return
        
        # 上传 base64 数据
        result = upload_base64_to_api(base64_data, content_type)
        
        if "error" in result:
            error_message = result["error"]
            if "details" in result:
                error_message += f"\nDetails: {result['details']}"
            notify("Upload Failed", error_message)
        else:
            # 处理 API 响应
            if "data" in result and "url" in result["data"]:
                url = result["data"]["url"]
                # 复制 URL 到剪贴板
                subprocess.run(['osascript', '-e', f'set the clipboard to "{url}"'])
                notify("Upload Successful", f"URL copied to clipboard: {url}")
            else:
                notify("Upload Successful", "Content uploaded successfully")
    except Exception as e:
        notify("Error", f"Unexpected error: {str(e)}")

if __name__ == "__main__":
    main() 