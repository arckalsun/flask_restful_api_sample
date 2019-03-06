#!/usr/bin/python3
# encoding: utf-8

'''
@project: crawler_server
@author: sunkuanwei
@email: arckalsun@gmail.com
@file: model
@time: 2019/3/5 17:52 
'''
from mongoengine import *
import datetime


class Articles(Document):
    title = StringField(required=True,max_length=200)
    body = StringField(required=True,max_length=100000)
    url = URLField(required=False,default=None,max_length=200)
    created = DateTimeField(default=datetime.datetime.now())
