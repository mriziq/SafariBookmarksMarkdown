# Safari Bookmarks to Markdown Converter

## Overview
This Python script, `convert.py`, is designed to convert Safari bookmarks exported in HTML format into a neatly organized Markdown file. The script parses the HTML file, extracts bookmarks and their folder structure, and outputs them in Markdown format, maintaining the folder hierarchy.

## Requirements
- Python 3
- BeautifulSoup4

## Installation
1. Ensure Python 3 is installed on your system.
2. Install BeautifulSoup4, if not already installed:
   ```bash
   pip install beautifulsoup4
   ```

## Usage
1. **Export Bookmarks from Safari:**
   - In Safari, go to `File` > `Export Bookmarks...` and save the HTML file.

2. **Run the Script:**
   - Execute the script in the terminal by navigating to the script's directory and running:
     ```bash
     python convert.py [input_html_file] [output_markdown_file]
     ```
   - Replace `[input_html_file]` with the path to your exported HTML file.
   - Replace `[output_markdown_file]` with the desired path for the Markdown output.

## Troubleshooting
- Ensure that the HTML file is exported correctly from Safari.
- If the script fails to run or produces unexpected output, check the HTML file format and ensure it matches the expected bookmark export format of Safari.

## License
This script is released under the [MIT License](https://opensource.org/licenses/MIT).
