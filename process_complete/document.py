
class SubDoc:
    def __init__(self, id, docName, docType, docHash):
        self.id = id
        self.docName = docName
        self.docType = docType
        self.docHash = docHash

class Document:
    def __init__(self, id, number, status, type, comment, buyer, supplier, dateFrom, docList):
        self.id = id
        self.number = number
        self.status = status
        self.type = type
        self.comment = comment
        self.buyer = buyer
        self.supplier = supplier
        self.dateFrom = dateFrom
        self.docList = docList

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

    def addSubDoc(self, id, name, docHash):
        self.docList.append(SubDoc(id, name, docHash))

    def removeSubDoc(self, id):
        self.docList = [x for x in self.docList if x.id != id]

    def update_SubDoc(self, prevId, id, name, dhash, newType):
        for idx, item in enumerate(self.docList):
            if item.id == prevId:
                self.docList[idx] = SubDoc(id, name, newType, dhash)