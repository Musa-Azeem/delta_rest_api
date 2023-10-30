from app.restapi import blueprint
from flask import request, current_app
from werkzeug.utils import secure_filename

@blueprint.route('/upload_raw', methods=['POST'])
def upload_raw():
    if 'file' not in request.files:
        return 'No file part', 400 # Bad Request
    
    file = request.files['file']

    if file.filename == '':
        return 'No selected file', 400 # Bad Request
    
    if file:
        filename = secure_filename(file.filename)
        file.save(f'{current_app.config["UPLOAD_DIR"]}/{filename}')
        return "File upload successful", 200 # OK