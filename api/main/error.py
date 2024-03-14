from flask import jsonify

from . import main


@main.app_errorhandler(400)
def clientError(e):
    return jsonify({
        'code': 400,
        'msg': '您的请求异常，请稍后再试'
    })

@main.app_errorhandler(403)
def forbidden(e):
    return jsonify({
        'code': 403,
        'msg': '您无权限访问此页面'
    })

@main.app_errorhandler(404)
def notFound(e):
    return jsonify({
        'code': 404,
        'msg': '页面不存在'
    })

@main.app_errorhandler(500)
def ServerError(e):
    return jsonify({
        'code': 500,
        'msg': '服务器端错误，请稍后再试。'
    })
