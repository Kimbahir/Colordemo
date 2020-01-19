
from flask import Flask
import random
import socket

app = Flask(__name__)
# app.config['SECRET_KEY'] = 'df61f5fe12eb40792e85b284ead07d51'

app.config['kba_counter'] = 0
app.config['kba_color'] = (random.choice(range(256)), random.choice(
    range(256)), random.choice(range(256)))
app.config['kba_hostname'] = socket.gethostname()

from app import routes
