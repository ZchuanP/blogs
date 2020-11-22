#!/usr/bin/env python 
# -*- coding:utf-8 -*-
from flask import Blueprint


auth_bp = Blueprint('blog', __name__)


@auth_bp.route('/login', method=['POST','GET'])
def login():
    pass


@auth_bp.route('/logout')
def logout():
    pass

