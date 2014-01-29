import os
from flask import render_template, request, send_from_directory
from werkzeug.utils import secure_filename
from app import app

@app.route('/')
def index():
	return render_template('index.html')

@app.route('/upload', methods=['GET', 'POST'])
def upload_file():
	if reqest.method == 'POST':
		file = request.files['files']
		if file.filename:
			filename = secure_filename( file.filename )
			file.save( os.path.join(app.config['UPLOAD_FOLDER'], filename) )
			return render_template('index.html', filename=filename)
	return render_template('index.html') # otherwise handle the GET case

@app.route('/uploads/')
def uploaded_file(filename):
	return send_from_directory(app.config['UPLOAD_FOLDER'], filename, as_attachment=True)


