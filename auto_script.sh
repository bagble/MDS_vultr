#!/bin/sh

VERSION=1.19.1
OP_LIST=https://raw.githubusercontent.com/bagble/MDS_vultr/main/ops.json

# Update & Upgrade
sudo apt update && sudo apt upgrade -y

# Setup
mkdir -p /root/server
# Download purpur latest version
wget https://api.purpurmc.org/v2/purpur/$VERSION/latest/download -O force.jar
# Download server runner By - monun
wget https://raw.githubusercontent.com/bagble/MDS_vultr/master/run -O run
# OP
wget $OP_LIST -O ops.json

# Move Files
mv force.jar /root/server/
mv run /root/server/
mv ops.json /root/server/

# Download requirements programs
sudo apt-get install openjdk-18-jdk -y
sudo apt install jq -y

# Start server
chmod +x /root/server/run
screen -S MDS /root/server/run
