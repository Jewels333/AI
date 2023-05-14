#!/bin/sh

pip install flask
pip install socket
pip install sudo
pip install ubuntu
ubuntu iptables -A INPUT -i lo -j ACCEPT
ubuntu iptables -A OUTPUT -o lo -j ACCEPT
python -m flask run --host=0.0.0.0