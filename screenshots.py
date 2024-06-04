import time
import csv
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import pyautogui


def take_screenshot_with_url_bar(url, output_file):
    chrome_options = Options()
    chrome_options.add_argument("--start-maximized")  # Maximize window
    driver = webdriver.Chrome(options=chrome_options)

    try:
        driver.get(url)
        time.sleep(5)  # Adjust the sleep duration as needed (e.g., 5 seconds)

        # Take screenshot of the entire screen
        screenshot = pyautogui.screenshot()
        screenshot.save(output_file)
        print(f"Screenshot saved: {output_file}")
    except Exception as e:
        print(f"Failed to take screenshot: {e}")
    finally:
        driver.quit()


def main():
    input_file = "domains.txt"

    with open(input_file, "r") as file:
        domains = [line.strip() for line in file]

    for domain in domains:
        url = f"http://{domain}"
        # Replace special characters in domain name to make it a valid filename
        sanitized_domain = domain.replace(".", "_").replace("/", "_")
        output_screenshot_file = f"{sanitized_domain}.png"
        take_screenshot_with_url_bar(url, output_screenshot_file)


if __name__ == "__main__":
    main()
