#!/bin/sh
pip install flask
echo '#!/bin/sh'

execute export FLASK_APP=app.py
execute flask run 