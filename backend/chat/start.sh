#!/bin/sh
pip install flask
echo '#!/bin/sh'

python -m flask run --host=0.0.0.0
echo app setup complete.