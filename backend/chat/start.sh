#!/bin/sh
pip install flask
pip install gunicorn
#python -m flask --app app run --host=0.0.0.0
gunicorn -w 4 'app:app'
gunicorn -w 4 'app:create_app()'