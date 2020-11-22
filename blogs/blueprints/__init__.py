#!/usr/bin/env python 
# -*- coding:utf-8 -*-
from flask import Flask

app = Flask(__name__)




from blogs.blueprints.auth import auth_bp
app.register_blueprint(auth_bp, url_prefix='/auth')
