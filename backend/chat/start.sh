#!/bin/sh
pip install flask
python -m flask --app app run --host=0.0.0.0
echo Finished.