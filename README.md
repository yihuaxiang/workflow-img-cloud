# Alfred Clipboard Uploader

This Alfred workflow allows you to upload clipboard content (both images and text) to a specified API endpoint.

## Features

- Upload images from clipboard
- Upload text from clipboard
- Automatically copies the response URL to clipboard
- Shows notifications for success/failure

## Installation

1. Download the workflow file
2. Double-click to install in Alfred
3. Make sure you have Python 3 installed
4. Install the required Python packages:
   ```
   pip3 install requests
   ```

## Usage

1. Copy an image or text to your clipboard
2. Trigger the workflow using:
   - Keyword: Type `upload` in Alfred
   - Hotkey: Press `Cmd+Option+U` (customizable)
3. The content will be uploaded to the API
4. Upon successful upload, the response URL will be copied to your clipboard

## Configuration

You can modify the following settings in the `upload_clipboard.py` file:

- `API_URL`: The API endpoint URL (default: "https://playground.z.wiki/img/upload")
- `UID`: The user ID to send with the request (default: "alfred-user")

## Troubleshooting

If you encounter any issues:

1. Make sure Python 3 is installed and in your PATH
2. Verify that the requests library is installed
3. Check that the API endpoint is accessible
4. Ensure your clipboard contains valid content (image or text)

## License

This project is open source and available under the MIT License. 