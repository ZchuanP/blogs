#!/usr/bin/env python 
# -*- coding:utf-8 -*-
from flask import Blueprint

blog_bp = Blueprint('blog', __name__)


@blog_bp.route('/')
def index():
    return 'Hello World!'


@blog_bp.route('setting')
def setting():
    pass


if __name__ == '__main__':
    app.run()