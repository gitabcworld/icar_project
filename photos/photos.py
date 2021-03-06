from flask import Blueprint, request, render_template, flash, g, session, redirect, url_for, jsonify, json
from werkzeug import check_password_hash, generate_password_hash
from werkzeug.utils import secure_filename
from factory_responses import FactoryResponse
from subprocess import check_output

import uuid
import os

ALLOWED_EXTENSIONS=set(['jpg','jpeg','bmp','png','JPG','JPEG','BMP','PNG'])

photos = Blueprint('photos',__name__,url_prefix='/photos')

responses = FactoryResponse()

def allowed_file(filename):
	return '.' in filename and filename.rsplit('.',1)[1] in ALLOWED_EXTENSIONS

def timestamp():
	import time
	return str(time.time()).split(".")[0]

def execute_counterfeit_texture(filepath):
	app.logger.debug("filepath="+str(filepath))
	output=check_output(["echo", "caca1:resultado1\ncaca2:resultado2\ncaca3:resultado3\ncaca4:resultado4\ncaca5:resultado5"])
	app.logger.debug("output="+str(output))
	values = output.split("\n")[:-1][-5:]
	app.logger.debug("values="+str(values))
	return values

@photos.route('/photos',methods=['POST'])
def post_photos():
	app.logger.debug("Applying post photo...")

	data = None
	if request.method == 'POST':
		app.logger.debug("Applying post image")

		# check if the post request has the file part
		if 'file' not in request.files:
			flash('No file part')
			return redirect(request.url)                                                                                                                                                                     

		file = request.files['file']

		# if user does not select file, browser also
		# submit a empty part without filename
		if file.filename == '':
			flash('No selected file')
			return redirect(request.url)                        

		if file and allowed_file(file.filename):
			#filename = secure_filename(file.filename)                                                                                                 
			extension = os.path.splitext(file.filename)[1]
			identifier=timestamp()+str(uuid.uuid4())
			f_name=identifier + extension
			app.logger.debug("f_name="+f_name)
			app.logger.debug("identifier="+identifier)
			filepath=os.path.join(app.config['UPLOAD_FOLDER'], f_name)
			file.save(filepath)

			values = execute_counterfeit_texture(filepath)
			result = '\n'.join(values)
			data_to_object ={'uuid':identifier, 'filepath': filepath, 'analysed':True, 'info':str(values)}
			data = {'filename':f_name, 'info':str(values),'id': new_photo.id}

	resp = None
	if data == None:
		resp = responses.new200()
	else:
		resp = responses.new201(data)
		return resp

@photos.route('/photos/<int:id>',methods=['GET'])
def get_photos_one(id):
	app.logger.debug("get_photos_one...")
	#photo =Photo.query.get_or_404(id)
	#return jsonify(photo.serialize_all())
	resp = responses.new200()
	return resp

@photos.route('/photos',methods=['GET'])
def get_photos():
	app.logger.debug("get_photos...")
	resp = responses.new200()
	return resp
