#!/usr/bin/env python 
# -*- coding:utf-8 -*-
import os
from flask import Flask


from blogs.settings import config
from blogs.blueprints.admin import admin_bp
from blogs.blueprints.auth import auth_bp
from blogs.blueprints.blog import blog_bp
"""
# 从配置类文件里读取配置类，先从环境变量里读取可以方便更改。（只更改环境变量）
app = Flask('blog')
config_name = os.getenv('FLASK_CONFIG', 'development')
# app.config.from_object()表示从类中加载配置，同样可以将配置存储在json中相应的换做from——json即可
app.config.from_object(config[config_name])
"""


# 定义程序工厂函数:接受配置文件名称为参数，返回创建好的程序实例
# 可以在不同的位置通过传入不同的配置类名来创建不同的程序实例
def create_app(config_name=None):
    if config_name is None:
        config_name = os.getenv('FLASK_CONFIG', 'development')

    app = Flask('blog')
    app.config.from_object(config[config_name])

    app.register_blueprint(blog_bp)
    app.register_blueprint(auth_bp, url_prefix='/auth')
    app.register_blueprint(admin_bp, url_prefix='/admin')

    return app



