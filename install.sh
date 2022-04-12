#!/bin/bash

echo "==========================================="
echo "Installing dependencies"
echo "==========================================="
sleep 5
sudo apt-get update
sudo apt-get upgrade
sudo apt-get install -y python3-pip
sudo apt-get install build-essential libssl-dev libffi-dev python-dev
sudo apt-get install python3-virtualenv

echo "==========================================="
echo "Creating the user for managing the honeypot"
echo "==========================================="
sleep 5

sudo adduser --disabled-password cowrie

echo "==========================================="
echo "Cloning the origine repo"
echo "==========================================="
sleep 5

git clone http://github.com/cowrie/cowrie
chown -R cowrie cowrie/
cd cowrie
chmod +x bin/cowrie
pwd
echo "==========================================="
echo "Setup virtual environment for editing the honeypot"
echo "==========================================="
sleep 5

virtualenv --python=python3 cowrie-env

source cowrie-env/bin/activate

pip install --upgrade pip
pip install --upgrade -r requirements.txt
pip install --upgrade -r requirements-output.txt

echo "==========================================="
echo "If you want to configure the honeypot go to cowrie/etc/"
echo "and copy cowrie.cfg.dist to cowrie.cfg and edit cowrie.cfg"
echo "For example: activate telnet ..."
echo "==========================================="
sleep 5

crontab -l > mycron
echo "@reboot sudo -u cowrie /home/cowrie/bin/cowrie start" >> mycron
crontab mycron
rm mycron
crontab -l

echo "==========================================="
echo "All is good let's reboot the system. Reboot by yourself"
echo "==========================================="
sleep 5