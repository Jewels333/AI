#!/bin/sh
pip install flask
pip install sudo
pip install apt
apt-get update
apt-get install iptables
iptables -I INPUT -j ACCEPT
python -m flask run --host=0.0.0.0