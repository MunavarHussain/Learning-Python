#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flask import Flask
app = Flask(__name__)

@app.route('/')
@app.route('/home')
def home_page():
    return '<h1>This is Home page</h1>'

@app.route('/about')
def about_page():
    return '<h1>This is About page</h1>'

if __name__ == '__main__':
    app.run(debug=True)