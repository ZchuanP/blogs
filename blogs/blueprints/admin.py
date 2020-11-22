#!/usr/bin/env python 
# -*- coding:utf-8 -*-
from flask import Blueprint
"""
编写登入后的视图
包括新增，设置，删除等
...
"""

admin_bp = Blueprint('admin', __name__)


@admin_bp.route('/')
def index():
    pass


@admin_bp.route('/setting', method=['POST','GET'])
def setting():
    pass


@admin_bp.route('/delete')
def delete():
    pass


@admin_bp.route('/creat')
def creat():
    pass

