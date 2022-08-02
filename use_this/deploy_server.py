import requests
from dotenv import load_dotenv
import os
import json
import asyncio

load_dotenv()
token = os.getenv('VULTR_TOKEN')
script_id = os.getenv('VULTR_SCRIPT_ID')

url = "https://api.vultr.com/v2/instances"
headers = {
    "Authorization": f"Bearer {token}",
    "Content-Type": "application/json"
}


def check_already_deployed():
    try:
        with open("./result.json", "r") as json_file:
            data = json.load(json_file)

        response = requests.get(f"{url}/{data['id']}", headers=headers)

        if response.status_code == 200:
            print("이미 서버가 생성되었습니다!")
            print(data)
            exit(0)
        else:
            os.remove("./result.json")
            asyncio.run(deploy())
    except FileNotFoundError:
        asyncio.run(deploy())


async def deploy():
    print("배포를 시작합니다...")
    data = {
        "region": "icn",
        "plan": "vc2-2c-4gb",
        "hostname": "MDS",
        "label": "MDS",
        "os_id": 1743,
        "script_id": f"{script_id}",
        "backups": "disabled",
        "ddos_protection": False
    }
    response = requests.post(url, headers=headers, json=data)

    save = {
        "id": response.json()['instance']['id'],
        "ip": response.json()['instance']['main_ip'],
        "password": response.json()['instance']['default_password'],
        "status": response.json()['instance']['status'],
        "power_status": response.json()['instance']['power_status'],
        "server_status": response.json()['instance']['server_status'],
        "kvm": None
    }

    while not (save['power_status'] == 'running' and save['status'] == 'active'):
        await asyncio.sleep(5)

        response = requests.get(f"{url}/{save['id']}", headers=headers)

        save['ip'] = response.json()['instance']['main_ip']
        save['status'] = response.json()['instance']['status']
        save['power_status'] = response.json()['instance']['power_status']
        save['server_status'] = response.json()['instance']['server_status']
        save['kvm'] = response.json()['instance']['kvm']

    with open("./result.json", 'w') as outfile:
        json.dump(save, outfile, indent=4)

    print("서버가 생성되었습니다!")
    print(save)
    await mc_server_status()


async def mc_server_status():
    status = False
    print("마인크래프트 서버 상태를 확인합니다...")
    with open("./result.json", "r") as json_file:
        data = json.load(json_file)

    while not status:
        await asyncio.sleep(10)
        mc_url = f"https://mcapi.us/server/status?ip={data['ip']}"

        response = requests.get(mc_url)
        status = response.json()['online']
    print("마인크래프트 서버가 확인 되었습니다!")
    print(f"서버 IP: {data['ip']}")


if __name__ == '__main__':
    check_already_deployed()