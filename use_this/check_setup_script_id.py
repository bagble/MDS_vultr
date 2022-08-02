import requests
from dotenv import load_dotenv
import os

load_dotenv()
token = os.getenv('VULTR_TOKEN')


def main():
    url = "https://api.vultr.com/v2/startup-scripts"
    headers = {
        "Authorization": f"Bearer {token}",
        "Content-Type": "application/json"
    }

    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        print(response.json())


if __name__ == '__main__':
    main()
