#!/bin/sh
pip install flask
echo '#!/bin/sh'

python -m flask --app app run
echo app setup complete.