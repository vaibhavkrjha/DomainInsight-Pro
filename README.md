# WEBSNAP - A Screenshot Capture Tool

This tool allows you to take screenshots of web pages using the Selenium WebDriver with Google Chrome in headless mode. It reads a list of URLs from a text file and saves the screenshots as PNG images.

## Prerequisites

Before using this tool, ensure you have the following installed:

1. Python 3.x
2. Google Chrome
3. ChromeDriver compatible with your version of Google Chrome
4. Required Python packages: `selenium`

You can install the `selenium` package using pip:

```bash
pip install selenium
```

## Setup

1. **Download ChromeDriver**: Download the appropriate version of ChromeDriver from [here](https://sites.google.com/a/chromium.org/chromedriver/downloads) and ensure it is in your system PATH or in the same directory as your script.

2. **Create a URLs file**: Create a text file named `urls.txt` in the same directory as your script. Add the URLs you want to take screenshots of, one per line. For example:
    ```
    https://example.com
    https://anotherexample.com
    ```

## Usage

To run the script, use the following command:

```bash
python screenshot_capture.py
```

The script will read the URLs from `urls.txt` and save the screenshots as `screenshot_0.png`, `screenshot_1.png`, etc., in the same directory.

## Code Explanation

Here's a breakdown of the script:

1. **Imports**:
    - `time`: To add a delay to allow the page to fully load.
    - `selenium`: To control the web browser.
    - `Options` from `selenium.webdriver.chrome.options`: To configure Chrome to run in headless mode.

2. **Function `take_screenshot(url, output_file)`**:
    - Configures Chrome to run headless and maximized.
    - Navigates to the provided URL.
    - Waits for a few seconds to allow the page to load completely.
    - Saves a screenshot of the page to the specified output file.
    - Handles any exceptions that occur and ensures the browser is closed.

3. **Main Script**:
    - Reads URLs from `urls.txt`.
    - Iterates over each URL, taking a screenshot and saving it with a unique filename.

## Customization

- **Adjusting Load Time**: The script waits for 5 seconds (`time.sleep(5)`) to ensure the page loads completely. You can adjust this duration based on your requirements.

- **Output Filenames**: Modify the naming convention for output files if needed. Currently, the filenames are `screenshot_0.png`, `screenshot_1.png`, etc.

## Example

Given a `urls.txt` containing:
```
https://www.google.com
https://www.github.com
```

Running the script will generate:
- `screenshot_0.png` (screenshot of Google homepage)
- `screenshot_1.png` (screenshot of GitHub homepage)

## Notes

- Ensure your `urls.txt` does not contain empty lines or extra whitespace.
- Running the browser in headless mode means it will not open any window; everything runs in the background.

By following these instructions, you should be able to capture screenshots of web pages automatically using this Python script.
