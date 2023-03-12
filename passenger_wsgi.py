import sys, os
INTERP = os.path.join(os.environ['HOME'], 'ai.sati.sh', 'venv', 'bin', 'python3')

#If we are not in Production - then it loads the Python Path from the .env file
if os.environ['HOME'] != '/home/dh_4q9r9f':
    from dotenv import load_dotenv
    load_dotenv()
    if (os.environ.get('INTERP')):
        INTERP = os.environ.get('INTERP')


if sys.executable != INTERP:
        os.execl(INTERP, INTERP, *sys.argv)
sys.path.append(os.getcwd())



from flask import Flask
application = Flask(__name__)
sys.path.append('app')
from app import app as application

