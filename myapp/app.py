import os

from flask import Flask

from .views import blueprints


def create_app():
	
	app = Flask(__name__)
	
	# TBD proper config here
	APP_URL_PREFIX = os.environ.get('MY_APP_PREFIX',None)
	
	for bp in blueprints:
		app.register_blueprint(bp,url_prefix=APP_URL_PREFIX)
		
		
	return app
	

app = create_app()	
	
