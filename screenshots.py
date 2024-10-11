import os
import requests
import pandas as pd
import csv
import dns.resolver
import tldextract
import whois
import socket
from ipwhois import IPWhois
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from PIL import Image
import pyautogui
import time

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

def check_dns(domain):
    resolver = dns.resolver.Resolver(configure=False)
    resolver.nameservers = ['8.8.8.8']  # Using Google's public DNS resolver
    try:
        resolver.resolve(domain)
        return True, "NoError"
    except dns.resolver.NXDOMAIN:
        return False, "NXDOMAIN"
    except dns.resolver.NoAnswer:
        return False, "NoAnswer"
    except dns.exception.Timeout:
        return False, "Timeout"
    except dns.resolver.NoNameservers:
        return False, "NoNameservers"
    except dns.resolver.NoRootSOA:
        return False, "NoRootSOA"
    except dns.exception.SyntaxError:
        return False, "SyntaxError"
    except dns.exception.FormError:
        return False, "FormError"
    except dns.exception.BadQuery:
        return False, "BadQuery"
    except dns.exception.BadResponse:
        return False, "BadResponse"
    except dns.exception.WantRead:
        return False, "WantRead"
    except dns.exception.WantWrite:
        return False, "WantWrite"
    except dns.exception.ConnectTimeout:
        return False, "ConnectTimeout"
    except dns.exception.SessionError:
        return False, "SessionError"

# Function to extract the root domain from a URL
def get_root_domain(url):
    extracted = tldextract.extract(url)
    root_domain = f"{extracted.domain}.{extracted.suffix}"
    return root_domain

# Function to perform WHOIS lookup
def perform_whois(domain):
    try:
        whois_data = whois.whois(domain)
        return whois_data
    except Exception as e:
        print(f"Failed to perform WHOIS lookup for {domain}: {e}")
        return None

# Function to get the hosting IP and organization
def get_hosting_info(domain):
    try:
        ip_address = socket.gethostbyname(domain)
        obj = IPWhois(ip_address)
        results = obj.lookup_rdap()
        org_name = results['network']['name']
        return ip_address, org_name
    except Exception as e:
        print(f"Failed to get hosting info for {domain}: {e}")
        return None, None

# Create folder for screenshots
screenshot_folder = "WebScreenshots"
if not os.path.exists(screenshot_folder):
    os.makedirs(screenshot_folder)

# Read domains from the file
with open('domains.txt', 'r') as file:
    domains = file.read().splitlines()

# Prepare a list to hold the combined data
combined_data = []

# Iterate over each domain to get WHOIS information and DNS status
for domain in domains:
    root_domain = get_root_domain(domain)
    
    whois_data = perform_whois(root_domain)

    if whois_data:
        whois_entry = {
            'Domain': whois_data.get('domain_name', root_domain),
            'Registrar Name': whois_data.get('registrar'),
            'Registrar Email': whois_data.get('emails'),
            'WHOIS Status': whois_data.get('status', ''),  # Original WHOIS status
            'Creation Date': whois_data.get('creation_date'),
            'Expiry Date': whois_data.get('expiration_date'),
            'Update Date': whois_data.get('updated_date')
        }
    else:
        whois_entry = {
            'Domain': root_domain,
            'Registrar Name': None,
            'Registrar Email': None,
            'WHOIS Status': '',  # Keeping Status blank
            'Creation Date': None,
            'Expiry Date': None,
            'Update Date': None
        }

    # Get hosting IP and organization
    hosting_ip, hosting_org = get_hosting_info(root_domain)
    whois_entry['Hosting IP'] = hosting_ip
    whois_entry['Hosting Organization'] = hosting_org
    
    # To keep the system awake during analysis and automated screenshot capturing process
    {"message_id":"04caba5f-a46c-4f6b-b45c-7b08877337a8","conversation_id":"67090d8e-96b8-800d-9919-2bddfcce7a34","source":"mouse","feedback":{"feedback_type":"copy","selected_text":"# Define a function to keep the system awake\nAdd-Type @\"\nusing System;\nusing System.Runtime.InteropServices;\n\npublic class SleepPreventer {\n    [DllImport(\"user32.dll\")]\n    public static extern void mouse_event(uint dwFlags, uint dx, uint dy, uint dwData, IntPtr dwExtraInfo);\n\n    public static void KeepAwake() {\n        // Simulate mouse movement slightly to prevent sleep\n        mouse_event(0x0001, 1, 0, 0, IntPtr.Zero); // Move mouse right\n        mouse_event(0x0001, -1, 0, 0, IntPtr.Zero); // Move mouse left\n    }\n}\n\"@\n\n# Set an interval to keep the system awake\n$interval = 60 # time in seconds\n\nwhile ($true) {\n    [SleepPreventer]::KeepAwake()\n    Start-Sleep -Seconds $interval\n}\n"},"location":"code-snippet"}
    
    # Check DNS status
    dns_status, dns_code = check_dns(domain)

    # Take screenshot if the domain is available
    if dns_status:
        url = f"http://{domain}"
        # Replace special characters in domain name to make it a valid filename
        sanitized_domain = domain.replace(".", "_").replace("/", "_")
        output_screenshot_file = os.path.join(screenshot_folder, f"{sanitized_domain}.png")
        take_screenshot_with_url_bar(url, output_screenshot_file)

    combined_entry = {
        **whois_entry,
        'DNS Status': 'Available' if dns_status else 'Unavailable',
        'DNS Code': dns_code,
        'Screenshot Path': output_screenshot_file if dns_status else None
    }

    combined_data.append(combined_entry)

# Convert the combined data to a DataFrame
df = pd.DataFrame(combined_data)

# Write the DataFrame to an Excel file
output_excel_file = 'BrandAbuse_output.xlsx'
df.to_excel(output_excel_file, index=False)

print(f"Combined data has been written to {output_excel_file}")



