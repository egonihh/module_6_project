# url_scanner.py
import urllib.request
from urllib.parse import urlparse

url = input("Enter URL (include http/https): ").strip()
if not urlparse(url).scheme:
    print("Add http:// or https:// to the URL")
else:
    try:
        with urllib.request.urlopen(url, timeout=5) as r:
            print("Status:", r.status)
            print("Protocol:", urlparse(url).scheme)
    except Exception as e:
        print("Error:", e)
