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
