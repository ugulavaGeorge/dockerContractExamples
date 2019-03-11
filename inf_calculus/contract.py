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
    if command == 'CALL':
        a = 0
        while (True):
            a += 1
            a -= 1
    elif command == 'CREATE':
       sys.exit(0)
    else:
       sys.exit(-1)