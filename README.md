# Alfred Clipboard Uploader

这个 Alfred workflow 允许您将剪贴板内容（图片和文本）上传到指定的 API 端点，使用 base64 编码方式。

## 功能特点

- 上传剪贴板中的图片（自动转换为 base64）
- 上传剪贴板中的文本（自动转换为 base64）
- 自动将返回的 URL 复制到剪贴板
- 显示上传成功/失败的通知
- 符合 Alfred JSON 格式的输出，支持更好的集成
- 所有依赖库已内置，无需额外安装

## 安装方法

1. 下载 workflow 文件（Clipboard Uploader.alfredworkflow）
2. 双击安装到 Alfred
3. 确保您已安装 Python 3
4. **无需安装额外的 Python 包**，所有依赖（包括 requests 库）已包含在 workflow 中

## 使用方法

1. 复制图片或文本到剪贴板
2. 触发 workflow：
   - 关键词：在 Alfred 中输入 `upload`
   - 快捷键：按下 `Cmd+Option+U`（可自定义）
3. 内容将被转换为 base64 格式并上传到 API
4. 上传成功后，返回的 URL 将自动复制到剪贴板

## 工作原理

1. 检测剪贴板内容类型（图片或文本）
2. 将内容转换为 base64 格式
3. 根据内容类型添加适当的 MIME 类型前缀
4. 使用 `base64` 参数将数据发送到 API
5. 处理 API 响应并显示结果

## 配置选项

您可以在 `upload_clipboard.py` 文件中修改以下设置：

- `API_URL`：API 端点 URL（默认：`https://playground.z.wiki/img/upload/base64`）

## 故障排除

如果遇到问题：

1. 确保 Python 3 已安装并在您的 PATH 中
2. 验证 API 端点是否可访问
3. 确保剪贴板包含有效内容（图片或文本）
4. 检查 API 是否支持 base64 上传格式
5. 如果上传失败，查看 Alfred 输出的错误信息

## 更新日志

### 最新版本
- 使用 base64 编码方式上传内容，无需创建临时文件
- 更新 API 端点为 base64 上传接口
- 优化 Alfred JSON 输出格式，提供更好的用户体验
- 改进错误处理和调试信息
- 内置所有依赖库，无需手动安装 requests

## 许可证

本项目是开源的，基于 MIT 许可证发布。 