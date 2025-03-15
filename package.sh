#!/bin/bash

# Create a temporary directory for packaging
TEMP_DIR=$(mktemp -d)
WORKFLOW_NAME="Clipboard Uploader.alfredworkflow"

# Copy all files to the temporary directory
cp -R * "$TEMP_DIR"

# Remove the packaging script from the temporary directory
rm "$TEMP_DIR/package.sh"

# Create the workflow file
cd "$TEMP_DIR"
zip -r "$WORKFLOW_NAME" .

# Move the workflow file back to the original directory
mv "$WORKFLOW_NAME" ..

# Clean up
cd ..
rm -rf "$TEMP_DIR"

echo "Workflow packaged as '$WORKFLOW_NAME'" 