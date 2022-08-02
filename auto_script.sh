#!/bin/sh

# make latest server
sudo apt update && sudo apt upgrade -y

mkdir -p /root/server
# download purpur latest 1.19.1 version
wget https://api.purpurmc.org/v2/purpur/1.19.1/latest/download -p /root/server
# download server runner By - monun
wget https://raw.githubusercontent.com/bagble/MDS_vultr/master/run -p /root/server

# download requirements programs
sudo apt-get install openjdk-18-jdk -y
sudo apt install jq -y
