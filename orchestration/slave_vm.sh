#!/bin/sh

echo "This slave is alive!"


sudo apt-get update -y
sudo apt-get upgrade -y

echo "Installing pip..."
sudo apt-get install -y python3-pip
sudo -H pip3 install --upgrade pip

echo "Installing celery, flask..."
sudo -H pip3 install celery
sudo -H pip3 install Flask

echo "Installing Octave and converter.."
sudo -H apt-get install -y octave
sudo -H pip3 install oct2py


echo "Installing the code..."
cd /home/ubuntu
sudo git clone https://github.com/TabeaHaverkamp/ACC-Project-BENCHOP.git


echo "Setting permission"
sudo chown -R ubuntu.users /home/ubuntu/ACC-Project-BENCHOP

sudo sed 's/localhost/192.168.2.146/' -i /home/ubuntu/ACC-Project-BENCHOP/BENCHOP/celery_app.py  
##TODO: REPLACE 192.168.2.146 WITH PRIVATE IP

echo "starting celery"
cd /home/ubuntu/ACC-Project-BENCHOP/BENCHOP 
sudo screen -S celeryserver -d -m bash -c 'cd /home/ubuntu/ACC-Project-BENCHOP/BENCHOP/ && celery -A tasks worker --loglevel=INFO -n worker1@%h --concurrency=1 --max-memory-per-child 100'
