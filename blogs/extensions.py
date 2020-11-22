#!/usr/bin/env python 
# -*- coding:utf-8 -*-
# 为何必须把项目源标记为源根
# 一个装饰前端网页的框架
from flask_bootstrap import Bootstrap
# 数据库包，实现模型对象到关系型数据库的映射
from flask_sqlalchemy import SQLAlchemy
# 提供接口，在flask应用中使用SMTP协议发送邮件(测试用)
from flask_mail import Mail
# 编辑文本样式的包，提供一系列的按钮和下拉列表来为文本设置格式
from flask_ckeditor import CKEditor
# 用来显示本地化的日期与时间
from flask_moment import Moment

"""
采用工厂来创建程序实例方便的在不同的环境下创建程序实例
但是这种方法会导致没有一个创建好的程序实例来生成一些扩展对象，比如数据库db
可以通过拓展提供的init_app()方法来分离扩展的实例化和初始化
我们将扩展类实例化的工作集中在extensions.py中进行处理
当我们初始化一个程序实例过后，要使用扩展对象直接从该模块导入即可
"""
bootstrap = Bootstrap()
db = SQLAlchemy()
moment = Moment()
ckeditor = CKEditor()
mail = Mail()
