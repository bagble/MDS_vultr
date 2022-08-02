#!/bin/sh

VERSION=1.19.1
OP_LIST=https://raw.githubusercontent.com/bagble/MDS_vultr/main/ops.json

# Update & Upgrade
sudo apt update && sudo apt upgrade -y

# Setup
mkdir -p /root/server
# Download purpur latest version
wget -P /root/server/ https://api.purpurmc.org/v2/purpur/$VERSION/latest/download -O force.jar
# Download server runner By - monun
wget -P /root/server/ https://raw.githubusercontent.com/bagble/MDS_vultr/master/run -O run
# OP
wget $OP_LIST -p /root/server -O ops.json

# Download requirements programs
sudo apt-get install openjdk-18-jdk -y
sudo apt install jq -y

# Start server
chmod +x /root/server/run
screen -S MDS
/root/server/run
