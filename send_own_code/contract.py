import requests
import subprocess
import json
import sys
import os

def find_param_value(params, name):
    for param in params:
        if param['key'] == name: return param['value']
    return None

if __name__ == '__main__':
    command = os.environ['COMMAND']
    tx = json.loads(os.environ['TX'])
    url = 'https://httpbin.org/post'
    file_name = __file__
    contract_source = {}
    contract_source["data"] = str(subprocess.Popen("cat "+os.path.abspath(file_name),shell=True, stdout=subprocess.PIPE).stdout.read())
    request = requests.post(url, data=json.dumps(contract_source))
    #print(request.text)
    if command == 'CALL':
       a = find_param_value(tx['params'], 'a')
       b = find_param_value(tx['params'], 'b')
       if a is None or b is None: sys.exit(-1)
       print(json.dumps([{
           "key": '{0}+{1}'.format(a, b),
           "type": "integer",
           "value": a + b}], separators=(',', ':')))
    elif command == 'CREATE':
       sys.exit(0)
    else:
       sys.exit(-1)