from dotenv import load_dotenv
import os
load_dotenv()
from pathlib import Path

basedir = os.path.abspath(os.path.dirname(__file__))

class Config:
    BASE_DIR = basedir
    UPLOAD_DIR = f'{basedir}/uploads'
