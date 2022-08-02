import requests


def main():
    url = "https://api.vultr.com/v2/plans"
    # view this : https://www.vultr.com/api/#tag/plans
    query = {
        "type": "all"
    }

    response = requests.get(url, params=query)

    if response.status_code == 200:
        print(response.json())


if __name__ == '__main__':
    main()
