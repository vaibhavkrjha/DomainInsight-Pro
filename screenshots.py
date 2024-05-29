import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def take_screenshot(url, output_file):
    chrome_options = Options()
    chrome_options.add_argument("--headless")  # To run Chrome in headless mode (no GUI)
    chrome_options.add_argument("--start-maximized")  # Maximize window
    driver = webdriver.Chrome(options=chrome_options)

    try:
        driver.get(url)
        time.sleep(5)  # Adjust the sleep duration as needed (e.g., 5 seconds)
        driver.save_screenshot(output_file)
        print(f"Screenshot saved: {output_file}")
    except Exception as e:
        print(f"Failed to take screenshot: {e}")
    finally:
        driver.quit()


if __name__ == "__main__":
    input_file = "urls.txt"
    with open(input_file, "r") as file:
        urls = file.readlines()
    for i, url in enumerate(urls):
        url = url.strip()  # Remove leading/trailing whitespace and newline characters
        output_file = f"screenshot_{i}.png"
        take_screenshot(url, output_file)