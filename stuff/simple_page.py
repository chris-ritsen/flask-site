
import codecs
from os import path

from flask import Blueprint, render_template, abort, Flask, request
from jinja2 import TemplateNotFound
from markdown import markdown

simple_page = Blueprint('simple_page', __name__, template_folder='templates')

@simple_page.route('/', defaults={'page': 'index'})
@simple_page.route('/<page>')

def show(page):
  try:
    if path.isfile('templates/pages/%s.md' % page):
      page_file = 'templates/pages/%s.md' % page
      input_file = codecs.open(page_file, mode="r", encoding="utf-8")
      text = input_file.read()
      html = markdown(text)
      return html
    else:
      return render_template('pages/%s.html' % page)
  except TemplateNotFound:
    abort(404)

