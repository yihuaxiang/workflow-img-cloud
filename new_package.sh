#!/bin/bash

# 定义工作流名称
WORKFLOW_NAME="Clipboard Uploader.alfredworkflow"

# 删除已存在的工作流文件
rm -f "$WORKFLOW_NAME"

# 创建工作流文件
zip -r "$WORKFLOW_NAME" upload_clipboard.py info.plist icons lib requirements.txt README.md

echo "工作流已打包为 '$WORKFLOW_NAME'" 