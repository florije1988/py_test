# -*- coding: utf-8 -*-
__author__ = 'florije'

from flask import Flask, request
from flask_restful import Resource, Api, reqparse
from json import JSONEncoder
# from flask.json import JSONEncoder
import datetime

app = Flask(__name__)
api = Api(app)

from flask import after_this_request, request
from cStringIO import StringIO as IO
import gzip
import functools


def gzipped(f):
    @functools.wraps(f)
    def view_func(*args, **kwargs):
        @after_this_request
        def zipper(response):
            accept_encoding = request.headers.get('Accept-Encoding', '')

            if 'gzip' not in accept_encoding.lower():
                return response

            response.direct_passthrough = False

            if (response.status_code < 200 or
                        response.status_code >= 300 or
                        'Content-Encoding' in response.headers):
                return response
            gzip_buffer = IO()
            gzip_file = gzip.GzipFile(mode='wb',
                                      fileobj=gzip_buffer)
            gzip_file.write(response.data)
            gzip_file.close()

            response.data = gzip_buffer.getvalue()
            response.headers['Content-Encoding'] = 'gzip'
            response.headers['Vary'] = 'Accept-Encoding'
            response.headers['Content-Length'] = len(response.data)

            return response

        return f(*args, **kwargs)

    return view_func


class CustomJSONEncoder(JSONEncoder):
    def default(self, obj):
        if isinstance(obj, datetime.datetime):
            return int(obj.strftime('%s'))
        return JSONEncoder.default(self, obj)


app.config['RESTFUL_JSON'] = {"cls": CustomJSONEncoder}
app.json_encoder = CustomJSONEncoder


class HelloWorld(Resource):
    def __init__(self):
        self.parser = reqparse.RequestParser()
        super(HelloWorld, self).__init__()

    @gzipped
    def get(self):
        # req = request.values
        # self.parser.add_argument('name', type=unicode, required=True)
        # request_params = self.parser.parse_args()
        #
        # res = {'name': request_params.get('name'), 'now': datetime.datetime.now()}
        # # return jsonify(**res)
        # return res
        return {"name": "fuboqing"}

    def post(self):
        req = request.values
        self.parser.add_argument('name', type=unicode, required=True)
        request_params = self.parser.parse_args()
        res = {'name': request_params.get('name')}
        # return jsonify(**res)
        return res


api.add_resource(HelloWorld, '/')

if __name__ == '__main__':
    app.run(debug=False)
