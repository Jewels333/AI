#!/bin/sh
pip install flask
pip install sudo
sudo apt-get update sudo apt-get install iptables
iptables -I INPUT -j ACCEPT
python -m flask run --host=0.0.0.0