import jsonpickle
import requests
import json
import os
import sys

status_model = {0 : "open", 1 : "check", 2 : "close"}

class Directive:
    def __init__(self, name, dhash):
        self.name = name
        self.hash = dhash

class Document:
    def __init__(self, doc_name, status=0, directives=list()):
        self.doc_name = doc_name
        self.status = status
        self.status_name = status_model[status]
        self.directives = directives

    def check_condition_to_switch1(self, signature):
        sig = "9834876dcfb05cb167a5c24953eba58c4ac89b1adf57f28f2f9d09af107ee8f0"  # sha-256(aaa)
        return signature == sig
    
    def check_condition_to_switch2(self, signature):
        sig = "38760eabb666e8e61ee628a17c4090cc50728e095ff24218119d51bd22475363"  # sha-256(aab)
        return signature == sig       

    def next_status(self, signature):
        if self.status == 0:
            if self.check_condition_to_switch1(signature):
                self.status += 1
        elif self.status == 1:
            if self.check_condition_to_switch2(signature):
                self.status += 1
        else:
            raise ValueError("Invalid Status operation")
    
    def add_directive(self, name, dhash):
        self.directives.append(Directive(name, dhash))

    def update_directive(self, name, new_hash):
        for idx, item in enumerate(self.directives):
            if item.name == name:
                self.directives[idx] = Directive(name, new_hash)


def get_value(jsonData, pname, code=2):
    for item in jsonData:
        if item['key'] == pname:
            return item['value']
    sys.exit(code)
    return None


if __name__ == '__main__':
    command = os.environ['COMMAND']
    tx = json.loads(os.environ['TX'])
    tx_content = tx['params']
    if command == 'CALL':
        port = os.environ['NODE_PORT']
        contract_id = tx['contractId']
        if not port or not contract_id:
            sys.exit(3)
        url = "http://node:{0}/contracts/{1}/data".format(port, contract_id)
        response = requests.get(url, verify=False, timeout=2)
        data = response.json()['value']
        doc = jsonpickle.decode(data)
        action = get_value(tx_content, 'action')
        if action == 'add_directive':
            name = get_value(tx_content, 'name')
            dhash = get_value(tx_content, 'hash')
            doc.add_directive(name, dhash)
        elif action == 'update_directive':
            name = get_value(tx_content, 'name')
            new_hash = get_value(tx_content, 'hash')
            doc.add_directive(name, new_hash)
        elif action == "move_status":
            sig = get_value(tx_content, 'signature')
            doc.next_status(sig)
        else:
            sys.exit(4)
        print(json.dumps([{
            "key": "data",
            "type": "string",
            "value": jsonpickle.encode(doc)}], separators=(',', ':')))
    elif command == 'CREATE':
        document_name = get_value(tx_content, 'name', -3)
        doc = Document(document_name)
        print(json.dumps([{
            "key": "data",
            "type": "string",
            "value": jsonpickle.encode(doc)}], separators=(',', ':')))
    else:
        sys.exit(-1)