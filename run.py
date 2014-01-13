#!/usr/bin/env python
# -*- coding: UTF-8 -*-

from flask import Flask, url_for, render_template, request, g, Response, stream_with_context, session
from peewee import *
import requests

app = Flask(__name__)

database = SqliteDatabase('databases/production.sqlite')
app.secret_key = 'SDPFUIOXMKLJCVSD897309847PIODJSMFKL'
# Config

@app.before_request
def before_request():
	g.db = database
	g.db.connect()

@app.after_request
def after_request(response):
	g.db.close()
	return response


@app.route("/")
def index():
	return render_template('index.html', name='Hibou')




if __name__ == "__main__":
	app.run(host='0.0.0.0',debug=True)
	