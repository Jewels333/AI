#!/bin/sh

pip install flask
pip install socket
bash app.py iptables -I INPUT -j ACCEPT
python -m flask run --host=0.0.0.0