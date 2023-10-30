from flask import Flask
from config import Config
from app.restapi import blueprint as restapi_bp
# from flask_cors import CORS, cross_origin
from pathlib import Path

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    # Enable Cross Origin
    # cors = CORS(app)
    # app.config['CORS_HEADERS'] = 'Content-Type'

    # Register blueprints
    app.register_blueprint(restapi_bp)

    if not Path(app.config['UPLOAD_DIR']).is_dir():
        Path(app.config['UPLOAD_DIR']).mkdir()
    return app