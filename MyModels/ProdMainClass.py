class ProdMainClass(object):
    id = 0

    def __init__(self):
        ProdMainClass.id += 1
        print(f" Super id {ProdMainClass.id}")


    def getProdID(self):
        return self.id
