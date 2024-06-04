# WEBSNAP - A Screenshot Capture Tool

This script reads a list of domain names from a text file, opens each domain in a browser, and takes a screenshot of the entire screen, including the browser URL bar. The screenshots are saved with filenames based on the domain names.

## Prerequisites

Before you run the script, make sure you have the following installed:

1. Python 3.x
2. `pip` (Python package installer)
3. Google Chrome browser
4. ChromeDriver compatible with your Chrome version (Download from [here](https://sites.google.com/a/chromium.org/chromedriver/downloads))

## Python Packages

You need to install the following Python packages:

- `selenium`
- `pillow`
- `pyautogui`

You can install these packages using `pip`:

```sh
pip install selenium pillow pyautogui
```

## Setup

1. **ChromeDriver**: Download ChromeDriver and ensure it is in your system PATH or place it in the same directory as your script.

2. **domains.txt**: Create a text file named `domains.txt` in the same directory as your script. Add the domain names you want to capture screenshots of, one per line. Example:

    ```
    example.com
    google.com
    github.com
    ```

## Usage

Run the script using Python:

```sh
python script_name.py
```

Replace `script_name.py` with the actual name of your script.

## Output

The script will:

1. Read the domain names from `domains.txt`.
2. Open each domain in Google Chrome.
3. Capture a screenshot of the entire screen, including the browser URL bar.
4. Save the screenshots in the same directory as the script, with filenames based on the domain names (dots and slashes replaced by underscores).

For example, a domain `example.com` will result in a screenshot named `example_com.png`.

### Notes

- Make sure your machine has a graphical environment available, as the script requires a display to open the browser and take screenshots.
- If running on a headless server, consider setting up a virtual display using tools like `xvfb` on Linux.

## Troubleshooting

1. **ChromeDriver not found**: Ensure ChromeDriver is in your system PATH or in the same directory as your script.
2. **Permissions**: Ensure the script has permission to read `domains.txt` and write screenshot files.
3. **Browser Issues**: If Chrome isn't opening, ensure Chrome is installed and updated, and ChromeDriver matches the Chrome version.

Feel free to customize the script as needed for your specific use case.

---

This README provides detailed instructions on setting up and running the script, along with troubleshooting tips.
