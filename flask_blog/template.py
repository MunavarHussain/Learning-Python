#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flask import Flask, render_template , url_for
app = Flask(__name__)

posts = [
        {
            'author':'Munavar Hussain',
            'Post_title':'Post 1',
            'Date_posted':'July 8,2019',
            'content':'post 1 content'
        },
        {
            'author':'Ashraf kutbudeen',
            'Post_title':'Post 2',
            'Date_posted':'July 9,2019',
            'content':'post 2 content'
        }
]

@app.route('/')
@app.route('/home')
def home_page():
    return render_template('home.html',posts=posts)

@app.route('/about')
def about_page():
    return render_template('about.html',title='About')

if __name__ == '__main__':
    app.run(debug=True)
