from MyModels.ProdMainClass import ProdMainClass


class PrinterProd(ProdMainClass):

    def __init__(self, **kwargs):
        super().__init__()
        self.id = PrinterProd.id = super().get_prod_id()
        self.prod = dict()
        """ продукт в виде словаря"""
        self.prod.update(kwargs)
        self.prod.update(id=PrinterProd.id)

    def get_prod_dict(self):
        """ метод выдает продукт в виде словаря"""
        return self.prod

    def get_prod_id(self):
        return self.id


if __name__ == "__main__":
    newPrinter1 = PrinterProd(name="Ecosys", model="P2040", brand="Kyosera", price="55000")
    newPrinter2 = PrinterProd(name="LaserJet", model="M111A", brand="HP", price="14000")
    newPrinter3 = PrinterProd(name="ImageClass", model="LBP6030", brand="Canon", price="23000")
    print(newPrinter3.get_prod_id())
    print(newPrinter2.get_prod_dict())
