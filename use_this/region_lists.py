import requests


def main():
    url = "https://api.vultr.com/v2/regions"

    response = requests.get(url)

    if response.status_code == 200:
        print(response.json())


if __name__ == '__main__':
    main()
