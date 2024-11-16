import sys

if len(sys.argv) != 2:
    print("Usage: python github-user-activity.py <username>")
    sys.exit(1)

username = sys.argv[1]
print(f"Fetching activity for {username}")

