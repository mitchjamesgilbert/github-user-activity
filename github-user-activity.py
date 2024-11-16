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
        # print(json.dumps(data, indent=4))
    
        for event in data:
            event_type = event["type"]
            repo_name = event["repo"]["name"]
            # print(event_type)
            # print(repo_name)

            if event_type == "PushEvent":
                commit_count = len(event["payload"]["commits"])
                commit_word = "commit" if commit_count == 1 else "commits"
                print(f"- Pushed {commit_count} {commit_word} to {repo_name}")
            
            elif event_type == "WatchEvent":
                print(f"- Starred {repo_name}")
            
            elif event_type == "IssuesEvent":
                action = event["payload"]["action"]
                print(f"- {action.capitalize()} an issue in {repo_name}")
            
            elif event_type == "CreateEvent":
                ref_type = event["payload"]["ref_type"]
                ref_name = event["payload"].get("ref", "N/A")
                if ref_type == "repository":
                    print(f"- Created a new repository: {repo_name}")
                else:
                    print(f"- Created a new {ref_type} '{ref_name}' in {repo_name}")

except urllib.error.HTTPError as e:
    print(f"HTTP Error: {e.code} - {e.reason}")
except urllib.error.URLError as e:
    print(f"URL Error: {e.reason}")
except Exception as e:
    print(f"Unexpected Error: {e}")