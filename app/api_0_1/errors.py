# -*- coding:utf-8 -*-
from flask import jsonify
# 403状态码的错误处理程序


def forbidden(message):
    response = jsonfy({'error':, 'forbidden': , 'message': message})
    response.status_code = 403
    return response
# ValidationError异常处理程序


@api.errorhandler(ValidationError)
def validation_error(e):
    return bad_request(e.args[0])
