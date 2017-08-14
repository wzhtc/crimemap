#!/usr/bin/python
import sys
import logging
logging.basicConfig(stream=sys.stderr)
sys.path.insert(0, "/var/www/crimemap/")

activate_this = '/var/www/crimemap/venv/bin/activate_this.py'
with open(activate_this) as file_:
    exec(file_.read(), dict(__file__=activate_this)


from crimemap import app as application
application.secret_key='your secret key'
