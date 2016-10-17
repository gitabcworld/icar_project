from flask import Blueprint, request, render_template, flash, g, session, redirect, url_for, jsonify, json
import os

main = Blueprint('main',__name__,url_prefix='/')

@main.route('/',methods=['POST','GET'])
def index():
	return render_template('index.html')

#@main.route("/")
#def init():
#    app.logger.debug("init")
#    return "<h1 style='color:blue'>Hello There!</h1>"
