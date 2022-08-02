# Minecraft Development Server on Vultr

---
#### <img src="https://www.vultr.com/media/icon_onwhite.svg" width="16" height="16" alt="https://www.vultr.com/?ref=9163513-8H"/>: [Vultr](https://www.vultr.com/?ref=9163513-8H)
#### [Monun](https://github.com/monun/minecraft-server-launcher)


## Requirements
* [Vultr](https://www.vultr.com/?ref=9163513-8H) account
* python 3.9 or higher `requirement package: python-dotenv, requests`
---
## Installation
* Install Requirements Programs
* Download Files from this Repository
```bash
1. wget https://raw.githubusercontent.com/bagble/MDS_vultr/master/use_this/deploy_server.py
2. wget https://raw.githubusercontent.com/bagble/MDS_vultr/master/use_this/destroy_server.py
3. wget https://raw.githubusercontent.com/bagble/MDS_vultr/master/use_this/check_setup_script_id.py
```
* Create `.env` file
```bash
VULTR_API=<Vultr API Key>
VULTR_SCRIPT_ID=<Vultr Script ID> # after
```
* Register/Login to [Vultr](https://www.vultr.com/?ref=9163513-8H)
* Go to `https://my.vultr.com/startup/manage/?id=new`
```bash
#!/bin/sh

wget https://raw.githubusercontent.com/bagble/MDS_vultr/main/auto_script.sh -O /root/auto_script.sh
wget https://raw.githubusercontent.com/bagble/MDS_vultr/main/mdsStartup -O /etc/init.d/mdsStartup

# Permission
chmod +x /etc/init.d/mdsStartup
chmod +x /root/auto_script.sh

# Startup
sudo update-rc.d mdsStartup defaults
sudo systemctl enable mdsStartup

# Reboot
bash -c "sleep 5; reboot"&
```
* Add Script
* Run `python3 check_setup_script_id.py`
* Check `id` then put `VULTR_SCRIPT_ID` in `.env`
* Run `python3 deploy_server.py`
* Done!
---
## Tips
* You can use `python3 destroy_server.py` to destroy the development server.
