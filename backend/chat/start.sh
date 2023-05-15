#!/bin/sh
pip install flask
flask --app app run --host=0.0.0.0
echo Finished.