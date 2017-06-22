#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun 22 09:55:41 2017

@author: jpoeppel
"""

from flask import Flask, render_template
from flask_socketio import SocketIO, emit

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app)

@app.route('/')
def index():
    return render_template('index.html')


@socketio.on('connect')
def connect():
    app.logger.info("Connected")

@socketio.on('my_event')
def test_message(message):
    
   emit('my_response', {'data': 'got it!: {}'.format(message)})

if __name__ == '__main__':
    socketio.run(app, debug=True)