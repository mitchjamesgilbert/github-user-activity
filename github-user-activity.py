import sys
import urllib.request
import json

if len(sys.argv) != 2:
    print("Usage: python github-user-activity.py <username>")
    sys.exit(1)

username = sys.argv[1]
print(f"Fetching activity for {username}")

url = f"https://api.github.com/users/{username}/events"

try:
    with urllib.request.urlopen(url) as response:
        data = json.load(response)
    
        print(json.dumps(data, indent=4))

except urllib.error.HTTPError as e:
    print(f"HTTP Error: {e.code} - {e.reason}")
except urllib.error.URLError as e:
    print(f"URL Error: {e.reason}")
except Exception as e:
    print(f"Unexpected Error: {e}")