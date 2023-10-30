from flask import Blueprint

blueprint = Blueprint('restapi', __name__)

from app.restapi import routes