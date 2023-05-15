#!/bin/sh
pip install flask
pip install sentry-sdk[flask]
#pip install sudo
#pip install apt
#python sudo apt-get update
#python sudo apt-get install iptables
#iptables -I INPUT -j ACCEPT
flask --app app run --host=0.0.0.0