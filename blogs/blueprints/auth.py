#!/usr/bin/env python 
# -*- coding:utf-8 -*-
from flask import Blueprint
"""
编写认证视图，登入登出等
...
"""

auth_bp = Blueprint('auth', __name__)


@auth_bp.route('/login', method=['POST','GET'])
def login():
    pass


@auth_bp.route('/logout')
def logout():
    pass

