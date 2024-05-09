from flask import jsonify

from . import error


@error.app_errorhandler(400)
def clientError(e):
    return jsonify({
        'code': 400,
        'message': '您的请求异常，请稍后再试'
    }),400

@error.app_errorhandler(403)
def forbidden(e):
    return jsonify({
        'code': 403,
        'message': '您无权限访问此页面'
    }),403;

@error.app_errorhandler(404)
def notFound(e):
    return jsonify({
        'code': 404,
        'message': '页面不存在'
    }),404;

@error.app_errorhandler(405)
def methodError(e):
    return jsonify({
        'code': 405,
        'message': '请求方法错误'
    }),405;

@error.app_errorhandler(500)
def ServerError(e):
    return jsonify({
        'code': 500,
        'message': '服务器端错误，请稍后再试。'
    }),500;
