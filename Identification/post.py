import requests
import simplejson
import requests
data = {'sender':   'Alice',
    'receiver': 'Bob',
    'message':  'We did it!'}
data_json = simplejson.dumps(data)
payload = {'json_payload': data_json}
r = requests.post("http://localhost:8080/data",json=payload)
a=requests.get("http://localhost:8080/data")

#%%
data = {'sender':   'Alice',
    'receiver': 'Bob',
    'message':  'We did it!'}
data_json = simplejson.dumps(data)
payload = {'json_payload': data_json}
r = requests.post("http://localhost:8080/data",json=data_json)
a=requests.get("http://localhost:8080/data")