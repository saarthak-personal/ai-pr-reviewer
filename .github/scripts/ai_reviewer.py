import os
import sys
import json
import requests

GITHUB_TOKEN = os.getenv("GITHUB_TOKEN")
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
PR_NUMBER = os.getenv("PR_NUMBER")
REPO_NAME = os.getenv("REPO_NAME")

if not all([GITHUB_TOKEN, OPENAI_API_KEY, PR_NUMBER, REPO_NAME]):
    print("Missing required environment variables.")
    sys.exit(1)

def get_pr_diff():
    """Fetches the raw diff text of the Pull Request."""
    url = f"https://github.com{REPO_NAME}/pulls/{PR_NUMBER}"
    headers = {
        "Authorization": f"token {GITHUB_TOKEN}",
        "Accept": "application/vnd.github.v3.diff"
    }
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        return response.text
    else:
        print(f"Failed to fetch diff: {response.status_code} - {response.text}")
        sys.exit(1)

def main():
    print(f"Starting AI Review for PR #{PR_NUMBER} in {REPO_NAME}...")
    diff_text = get_pr_diff()
    print(f"Successfully fetched PR diff. Total length: {len(diff_text)} characters.")

if __name__ == "__main__":
    main()