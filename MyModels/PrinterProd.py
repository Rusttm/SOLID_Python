from MyModels.ProdMainClass import ProdMainClass


class PrinterProd(ProdMainClass):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.id = PrinterProd.id = super().get_prod_id()
        self.prod.update(id=PrinterProd.id)
        self.prod.update(label=self.get_prod_label("name", "model"))




if __name__ == "__main__":
    newPrinter1 = PrinterProd(name="Ecosys", model="P2040", brand="Kyosera", price="55000")
    newPrinter2 = PrinterProd(name="LaserJet", model="M111A", brand="HP", price="14000")
    newPrinter3 = PrinterProd(name="ImageClass", model="LBP6030", brand="Canon", price="23000")
    print(newPrinter3.get_prod_id())
    print(newPrinter2.get_prod_dict())
