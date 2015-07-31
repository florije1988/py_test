# -*- coding: utf-8 -*-
__author__ = 'florije'

from wsgiref.simple_server import make_server, demo_app
import time


def application(environ, start_response):
    status = '200 OK'
    headers = [('Content-type', 'text/plain')]
    start_response(status, headers)
    time.sleep(0.1)
    return ["Hello World"]


if __name__ == '__main__':
    httpd = make_server('', 5001, application)
    print("Serving on port 5001")
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        pass
