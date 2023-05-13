#!/bin/sh
pip install flask
pip install socket
python -m flask run --host=0.0.0.0
echo app setup complete.
bash ipconfig
