#!/usr/bin/env python 
# -*- coding:utf-8 -*-
import os
import sys
"""
此文件用来保存配置文件，
利用python类将不同情况下
需要用到的配置用不同的类进行保存
包括一个基础配置类和几个特定的配置类
特定的配置类都继承了基础配置类
"""


# __file__表示文件的绝对路径
# os.path.dirname()去掉最后一个路径，返回剩余
# os.path.abspath()返回文件的绝对路径
basedir = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))

# sys.platform.startswith()传入win/linux，返回布尔值，判断操作系统类型
WIN = sys.platform.startswith('win')
if WIN:
    prefix = 'sqlite:///'
else:
    prefix = 'sqlite:////'


class BaseConfig(object):
    # os.getenv()读取环境变量，若未读到，使用给定值
    # 安全秘钥，用在一些需要加密的地方，如cookie ，session
    SECRET_KEY = os.getenv('SECRET_KEY', 'dev key')

    # 是否拦截重定向，默认拦截，这里关闭
    DEBUG_TB_INTERCEPT_REDIRECTS = False
    # 设置为true是会跟踪对象的修改并发出警告，应该将其禁用，这里将其禁用（False）
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    # 用于显式禁用或启用查询记录。（查询记录将在调试或测试模式下产生）
    SQLALCHEMY_RECORD_QUERIES = True

    # 用于为图片上传启用CSRF保护
    CKEDITOR_ENABLE_CSRF = True
    CKEDITOR_FILE_UPLOADER = 'admin.upload_image'

    # 邮件配置
    MAIL_SERVER = os.getenv('MAIL_SERVER')
    MAIL_PORT = 465
    MAIL_USE_SSL = True
    MAIL_USERNAME = os.getenv('MAIL_USERNAME')
    MAIL_PASSWORD = os.getenv('MAIL_PASSWORD')
    MAIL_DEFAULT_SENDER = ('Bluelog Admin', MAIL_USERNAME)

    BLUELOG_EMAIL = os.getenv('BLUELOG_EMAIL')
    BLUELOG_POST_PER_PAGE = 10
    BLUELOG_MANAGE_POST_PER_PAGE = 15
    BLUELOG_COMMENT_PER_PAGE = 15
    # ('theme name', 'display name')
    BLUELOG_THEMES = {'perfect_blue': 'Perfect Blue', 'black_swan': 'Black Swan'}
    BLUELOG_SLOW_QUERY_THRESHOLD = 1

    BLUELOG_UPLOAD_PATH = os.path.join(basedir, 'uploads')
    BLUELOG_ALLOWED_IMAGE_EXTENSIONS = ['png', 'jpg', 'jpeg', 'gif']


class DevelopmentConfig(BaseConfig):
    # 开发配置类
    # os.path.join()用于路径拼接 传入多个参数，从第一个以‘/’开头的参数开始拼接，之前的全部丢弃。若出现以'./'开头的，则以这个的上一个开始拼接
    # 用于连接数据库的URL
    SQLALCHEMY_DATABASE_URI = prefix + os.path.join(basedir, 'data-dev.db')


class TestingConfig(BaseConfig):
    # 测试环境下所用的配置
    TESTING = True
    WTF_CSRF_ENABLED = False
    SQLALCHEMY_DATABASE_URI = 'sqlite:///:memory:'  # in-memory database


class ProductionConfig(BaseConfig):
    # 生产配置类
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL', prefix + os.path.join(basedir, 'data.db'))


# 方便修改配置的类型，直接用字典访问的方法便可直接切换配置类型
config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'Production': ProductionConfig
}