import json

from werkzeug import Response, Request
import os

ALLOWED_HOSTS = os.environ.get('ALLOWED_HOSTS').split(',')


class CustomSecurityMiddleware:
    def __init__(self, app):
        self._app = app

    def __call__(self, environ, start_response):
        request = Request(environ)
        remote_addr = request.remote_addr

        if remote_addr in ALLOWED_HOSTS:
            return self._app(environ, start_response)

        payload = {
            'detail': 'You cannot access this resource'
        }
        response = Response(response=json.dumps(payload), mimetype='application/json', status=403)

        return response(environ, start_response)
