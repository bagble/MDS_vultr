#!/bin/sh

VERSION=1.19.1
OP_LIST=https://raw.githubusercontent.com/bagble/MDS_vultr/main/ops.json

# Update & Upgrade
sudo apt update && sudo apt upgrade -y

# Setup
mkdir -p /root/server
# Download purpur latest version
wget https://api.purpurmc.org/v2/purpur/$VERSION/latest/download -O /root/server/force.jar
# Download server runner By - monun
wget https://raw.githubusercontent.com/bagble/MDS_vultr/master/run -O /root/server/run
# OP
wget $OP_LIST -O /root/server/ops.json

# Download requirements programs
sudo apt-get install openjdk-18-jdk -y
sudo apt install jq -y

# Open ports
sudo ufw allow 25565
sudo ufw allow 5005

# Start server
chmod +x /root/server/run
/root/server/run
