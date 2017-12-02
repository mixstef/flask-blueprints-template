from flask import Blueprint



hello = Blueprint('hello',__name__)


@hello.route('/')
def index_page():
	
	return('Hello!')
	
