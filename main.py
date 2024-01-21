import requests
import sys

def check_directory(url):
    response = requests.get(url)
    if response.status_code == 404:
        return False
    else:
        return True

if len(sys.argv) != 2:
    print("Usage: python script.py <target_url>")
    sys.exit(1)

target_url = sys.argv[1]

with open("file.txt", "r") as file:
    directories = file.read().splitlines()

for directory in directories:
    url = f"http://{target_url}/{directory}"
    if check_directory(url):
        print("Valid directory:", url)

