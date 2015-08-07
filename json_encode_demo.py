# -*- coding: utf-8 -*-
__author__ = 'florije'

import json
from bson import json_util
from json import JSONEncoder
import datetime


class CusJsonEncoder(JSONEncoder):
    def default(self, o):
        if isinstance(o, datetime.datetime):
            print "datetime"
        if isinstance(o, int):
            print int
        return JSONEncoder.default(self, o)


if __name__ == '__main__':
    sim_dict = {'age': 10, 'time': datetime.datetime.now()}
    # print json.dumps(sim_dict, cls=CusJsonEncoder)
    try:
        print json_util.dumps(sim_dict)
    except Exception as e:
        print e.message
