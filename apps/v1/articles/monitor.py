#!/usr/bin/python3
# encoding: utf-8

'''
@project: crawler_server
@author: sunkuanwei
@email: arckalsun@gmail.com
@file: monitor
@time: 2019/3/6 10:28 
'''
from flask import request,current_app
from flask_restful import Resource
from ..decorator import sign_check

class ArticleMonitorAPI(Resource):
    '''监测文章'''

    @sign_check(app=current_app)
    def get(self):
        ret = {
            "code": 0,
            "msg": "success"
        }

        ret['data'] = 'monitor article finish'

        return ret