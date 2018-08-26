 #!/usr/bin/env python3
import os
from flask import Flask

from core.controllers.login import controller as login
from core.controllers.home  import controller as home
from core.controllers.user import controller as user
from core.controllers.search import controller as search
from core.controllers.logout import controller as logout

def keymaker(app,filename='secret_key'):
	pathname=os.path.join(app.instance_path,filename)
	try:
		app.config['SECRET_KEY'] = open(pathname,'rb').read()
	except IOError:
		parent_directory = os.path.dirname(pathname)
		if not os.path.isdir(parent_directory):
			os.system('mkdir -p {}'.format(parent_directory))
		os.system('head -c 24 /dev/urandom > {}'.format(pathname))
		app.config['SECRET_KEY'] = open(pathname,'rb').read()

app = Flask(__name__)

app.register_blueprint(login)
app.register_blueprint(home)
app.register_blueprint(user)
app.register_blueprint(search)
app.register_blueprint(logout)

keymaker(app)
