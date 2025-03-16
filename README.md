# Alfred Clipboard Uploader

This Alfred workflow allows you to upload clipboard content (images and text) to a specified API endpoint using base64 encoding.

## Features

- Upload images from clipboard (automatically converted to base64)
- Upload text from clipboard (automatically converted to base64)
- Automatically copy the returned URL to clipboard
- Display success/failure notifications
- Alfred JSON format output for better integration
- All dependencies included, no additional installation required

## Installation

1. Download the workflow file (Clipboard Uploader.alfredworkflow)
2. Double-click to install in Alfred
3. Make sure you have Python 3 installed
4. **No need to install additional Python packages**, all dependencies (including the requests library) are included in the workflow

## Usage

1. Copy an image or text to your clipboard
2. Trigger the workflow:
   - Keyword: Type `upload` in Alfred
   - Hotkey: Press `Cmd+Option+U` (customizable)
3. The content will be converted to base64 format and uploaded to the API
4. Upon successful upload, the returned URL will be copied to your clipboard

## How It Works

1. Detects clipboard content type (image or text)
2. Converts the content to base64 format
3. Adds appropriate MIME type prefix based on content type
4. Sends the data to the API using the `base64` parameter
5. Processes the API response and displays the result

## Configuration

You can modify the following settings in the `upload_clipboard.py` file:

- `API_URL`: The API endpoint URL (default: `https://playground.z.wiki/img/upload/base64`)

## Troubleshooting

If you encounter any issues:

1. Make sure Python 3 is installed and in your PATH
2. Verify that the API endpoint is accessible
3. Ensure your clipboard contains valid content (image or text)
4. Check if the API supports base64 upload format
5. If upload fails, check the error message in Alfred output

## Changelog

### Latest Version
- Using base64 encoding for uploads, eliminating the need for temporary files
- Updated API endpoint for base64 uploads
- Optimized Alfred JSON output format for better user experience
- Improved error handling and debugging information
- Bundled all dependencies, no need to manually install requests

## License

This project is open source and available under the MIT License. 