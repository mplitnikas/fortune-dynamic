#!/usr/bin/python
import fortune_db
from flask import Flask

app = Flask(__name__)

template = '''
<h1>Fortune page generator 0.2</h1>
<p>%s</p>
'''

@app.route('/')
def get_fortune():
    return template % fortune_db.get_random_fortune()

