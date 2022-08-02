#!/bin/sh

VERSION=1.19.1
OP_LIST=https://raw.githubusercontent.com/bagble/MDS_vultr/main/ops.json

# Update & Upgrade
sudo apt update && sudo apt upgrade -y

# Setup
mkdir -p /root/mc/
mkdir -p /root/mc/server
cd /root/mc
# Download purpur latest version
wget https://api.purpurmc.org/v2/purpur/$VERSION/latest/download -O /root/mc/force.jar
# Download server runner By - monun
wget https://raw.githubusercontent.com/bagble/MDS_vultr/master/run -O /root/mc/run
# OP
wget $OP_LIST -O /root/mc/server/ops.json

# Download requirements programs
sudo apt-get install openjdk-18-jdk -y
sudo apt install jq -y

# Open ports
sudo ufw allow 25565
sudo ufw allow 5005

# Start server
chmod +x /root/mc/run
screen -dmS MDS /root/mc/run
