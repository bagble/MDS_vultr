import json

import requests
from dotenv import load_dotenv
import os

load_dotenv()
token = os.getenv('VULTR_TOKEN')

url = "https://api.vultr.com/v2/instances"
headers = {
    "Authorization": f"Bearer {token}",
    "Content-Type": "application/json"
}

try:
    with open("./result.json", "r") as json_file:
        data = json.load(json_file)
except FileNotFoundError:
    print("서버가 존재하지 않습니다!")
    exit(0)


def check_already_deployed():
    response = requests.get(f"{url}/{data['id']}", headers=headers)

    if response.status_code == 200:
        destroy()
    else:
        print("서버가 존재하지 않거나 이미 삭제되었습니다!")
        os.remove("./result.json")
        exit(0)


def destroy():
    response = requests.delete(f"{url}/{data['id']}", headers=headers)

    if response.status_code == 204:
        print("서버가 삭제되었습니다!")
        os.remove("./result.json")
        exit(0)
    else:
        print(f"서버 삭제에 실패했습니다! / 응답코드: {response.status_code}")
        exit(0)


if __name__ == "__main__":
    check_already_deployed()
