class MTR:
    def __init__(self, id, quantity, deliveryDate, deliveryAddress, inspector, inspectorKeys):
        self.id = id
        self.quantity = quantity
        self.deliveryDate = deliveryDate
        self.deliveryAddress = deliveryAddress
        self.inspector = inspector
        self.inspectorKeys = inspectorKeys


class Complaint:
    def __init__(self, orderid, id, status, number, dateFrom, buyer, tolerance, comment, chash, mtrList=list()):
        self.orderid = orderid
        self.id = id
        self.status = status
        self.number = number
        self.dateFrom = dateFrom
        self.buyer = buyer
        self.tolerance = tolerance
        self.comment = comment
        self.chash = chash
        self.mtrList = mtrList

    def addMtr(self, id, quantity, deliveryDate, deliveryAddress, inspector, inspectorKeys):
        self.mtrList.append(MTR(id, quantity, deliveryDate, deliveryAddress, inspector, inspectorKeys))

    def removeMtr(self, id):
        self.mtrList = [x for x in self.mtrList if x.id != id]

    def updateMtr(self, prevId, id, quantity, deliveryDate, deliveryAddress, inspector, inspectorKeys):
        for idx, item in enumerate(self.mtrList):
            if item.id == prevId:
                self.mtrList[idx] = MTR(id, id, quantity, deliveryDate, deliveryAddress, inspector, inspectorKeys)