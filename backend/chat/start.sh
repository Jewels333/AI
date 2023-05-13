#!/bin/sh
pip install flask
pip install socket
echo hostname -I
python -m flask run --host=0.0.0.0