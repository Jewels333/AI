#!/bin/sh
pip install flask
echo '#!/bin/sh'

bash export FLASK_APP=app.py
bash flask run 