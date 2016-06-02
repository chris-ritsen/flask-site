#!/usr/bin/python

import subprocess

from flask import Blueprint, render_template, abort, Flask, request
from jinja2 import TemplateNotFound
import redis

from flaskext.markdown import Markdown
from stuff import simple_page

r = redis.StrictRedis(host='localhost', port=6379, db=0)
app = Flask(__name__)
Markdown(app)
app.register_blueprint(simple_page.simple_page)

@app.route("/hello")

def hello():
  return "Hello World!"

@app.route("/window", methods=['GET', 'OPTIONS'])

def window():
  windows = subprocess.check_output(["wmctrl", "-l"]).decode()
  name = r.get('name').decode()
  return render_template('test.html', command=windows, title=name)

if __name__ == "__main__":
  app.run('0.0.0.0')

