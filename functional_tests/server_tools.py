from os import path
import subprocess
import os

THIS_FOLDER = path.dirname(path.abspath(__file__))

def create_session_on_server(host, email):
	return subprocess.check_output(
		[
			'fab',
			'create_session_on_server:email={}'.format(email),
			'--host=ubuntu@{}'.format(host),
			'--hide=everything,status',
			'-i',
			os.environ['AWS_KEYFILE']
		],
		cwd=THIS_FOLDER
	).decode().strip()

def reset_database(host):
	subprocess.check_call(
		[
			'fab',
			'reset_database',
			'--host=ubuntu@{}'.format(host),
			'-i',
			os.environ['AWS_KEYFILE']
		],
		cwd=THIS_FOLDER
	)