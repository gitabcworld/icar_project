from flask import Flask
from flask_bootstrap import Bootstrap

import uuid
import os
import logging

# Initialization variables
app = Flask(__name__)
app.logger.debug("")
app.config.from_object('config')

#Bootstrap extension
Bootstrap(app)

#Load modules
from main.main import main
from photos.photos import photos
app.register_blueprint(main)
app.register_blueprint(photos)


if not app.debug:
    import logging
    from logging.handlers import RotatingFileHandler
    file_handler = RotatingFileHandler('log/my_app.log','a',1*1024*1024,10)
    file_handler.setFormatter(logging.Formatter('%(asctime)s %(levelname)s: %(message)s [in %(pathname)s:%(lineno)d]'))
    app.logger.setLevel(logging.INFO)
    file_handler.setLevel(logging.INFO)
    app.logger.addHandler(file_handler)
    app.logger.info('app startup')

@app.before_first_request
def setup_logging():
    if not app.debug:
        # In production mode, add log handler to sys.stderr.
        app.logger.addHandler(logging.StreamHandler())
        app.logger.setLevel(logging.INFO)

if __name__ == "__main__":
    app.run(host='0.0.0.0')
