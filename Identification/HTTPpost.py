# -*- coding: utf-8 -*-
"""
Created on Thu Nov 28 11:35:45 2019

@author: Jules
"""


import simplejson
import requests
data = {'sender':   'Alice',
    'receiver': 'Bob',
    'message':  'We did it!'}
data_json = simplejson.dumps(data)
payload = {'json_payload': data_json}
r = requests.post("http://localhost:8000", json=payload)
