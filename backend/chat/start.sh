#!/bin/sh
pip install flask
pyenv shell 3.8.13
python -m flask --app app run --host=0.0.0.0
