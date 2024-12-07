# HTTP-Header-Security-Scanner
3️⃣ HTTP Header Security Scanner Purpose Scan HTT


Scan HTTP headers for common security misconfigurations and vulnerabilities like missing Content-Security-Policy, X-Content-Type-Options, etc.


```python
import requests


# Function to analyze HTTP headers
def analyze_http_headers(url):
    try:
        response = requests.get(url)
        headers = response.headers

        print("[+] Analyzing HTTP headers...")
        if "Content-Security-Policy" not in headers:
            print("[!] Missing Content-Security-Policy Header")
        else:
            print("[+] Content-Security-Policy is set.")

        if "X-Content-Type-Options" not in headers:
            print("[!] Missing X-Content-Type-Options Header")
        else:
            print("[+] X-Content-Type-Options is set.")
    except Exception as e:
        print(f"[-] Error accessing URL: {e}")


# Main execution
url = input("Enter the target URL: ")
analyze_http_headers(url)
