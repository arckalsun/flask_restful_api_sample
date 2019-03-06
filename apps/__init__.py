#!/usr/bin/python3
# encoding: utf-8

'''
@project: crawler_server
@author: sunkuanwei
@email: arckalsun@gmail.com
@file: __init__.py
@time: 2019/3/5 17:48 
'''
from apps.v1 import create_blueprint_v1

def register_blueprints(app):
    # 注册版本
    app.register_blueprint(create_blueprint_v1(),url_prefix='/api/v1')