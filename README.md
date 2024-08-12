# DomainInsight Pro

This Python script reads a list of domain names, retrieves WHOIS information, checks DNS status, captures screenshots of the websites, and compiles all the data into an Excel file. The tool is useful for analyzing domain information, verifying website availability, and documenting the visual appearance of websites.

## Features
- **WHOIS Lookup**: Retrieves detailed WHOIS information for each domain, including registrar, creation, expiry dates, and status.
- **DNS Status Check**: Verifies whether the domain is resolvable using DNS and provides relevant DNS error codes if not.
- **Hosting Information**: Retrieves the IP address and organization hosting the domain.
- **Website Screenshot**: Captures a full-screen screenshot of the website, including the URL bar, for visual documentation.
- **Data Export**: Compiles all gathered data into an Excel file (`BrandAbuse_output.xlsx`).

## Prerequisites
Ensure the following Python packages are installed:

```bash
pip install requests pandas dnspython tldextract python-whois ipwhois selenium pillow pyautogui openpyxl
```

You also need:
- **Google Chrome**: The script uses Chrome for taking screenshots.
- **ChromeDriver**: Ensure the appropriate version of ChromeDriver is installed and accessible in your system's PATH. [Download ChromeDriver](https://sites.google.com/a/chromium.org/chromedriver/downloads)

## Setup

1. **Create a `domains.txt` File**:  
   Place a `domains.txt` file in the same directory as the script. This file should contain a list of domain names, one per line.

   Example `domains.txt`:
   ```
   example.com
   google.com
   nonexistentsite.xyz
   ```

2. **Prepare a Screenshot Folder**:  
   The script will automatically create a `WebScreenshots` folder to store screenshots. If the folder does not exist, it will be created.

## How to Run

1. **Execute the Script**:  
   Run the script with Python:

   ```bash
   python script.py
   ```

   The script will:
   - Read domain names from `domains.txt`.
   - Perform WHOIS lookup and DNS checks.
   - Capture a screenshot of each domain's homepage (if accessible).
   - Collect hosting information.
   - Save all collected data into an Excel file named `BrandAbuse_output.xlsx`.

2. **Review the Output**:  
   After execution, check:
   - **`BrandAbuse_output.xlsx`**: This Excel file contains WHOIS details, DNS status, hosting information, and paths to the screenshots.
   - **`WebScreenshots/`**: This folder contains screenshots of the websites.

## Configuration

- **DNS Resolver**: The script uses Google's public DNS resolver (`8.8.8.8`). You can change the resolver by modifying the IP address in the `check_dns()` function.
- **Screenshot Delay**: The script waits 5 seconds before capturing the screenshot to ensure the page fully loads. Adjust the sleep duration (`time.sleep(5)`) if necessary.

## Error Handling

- **WHOIS Lookup Failures**: If WHOIS data cannot be retrieved, the script will log the failure and continue processing other domains.
- **DNS Resolution Errors**: The script captures various DNS resolution errors and records them in the output.
- **Screenshot Failures**: If a screenshot cannot be captured, an error will be logged, and the script will continue.

## Dependencies

- **requests**: For making HTTP requests.
- **pandas**: For handling data and exporting to Excel.
- **dnspython**: For DNS resolution checks.
- **tldextract**: For extracting domain components.
- **whois**: For performing WHOIS lookups.
- **ipwhois**: For retrieving hosting IP and organization details.
- **selenium**: For web automation and screenshot capturing.
- **Pillow (PIL)**: For handling image processing.
- **pyautogui**: For taking screenshots of the full screen.
- **openpyxl**: For exporting data to Excel.

## Known Issues

- Ensure that ChromeDriver and Google Chrome versions are compatible to avoid browser automation issues.
- The script assumes the website is accessible via `http://`. If a domain only supports `https://`, you may need to adjust the URL generation.

## License

This script is provided "as is", without warranty of any kind. Feel free to modify and use it for your purposes.
