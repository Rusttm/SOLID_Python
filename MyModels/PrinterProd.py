from MyModels.ProdMainClass import ProdMainClass


class PrinterProd(ProdMainClass):

    def __init__(self, **kwargs):
        super().__init__()
        PrinterProd.id = super().getProdID()
        self.prod = dict()
        self.prod.update(kwargs)
        self.prod.update(id=PrinterProd.id)




if __name__ == "__main__":
    newPrinter1 = PrinterProd(name=)
    newPrinter2 = PrinterProd()
    newPrinter3 = PrinterProd()
    # print(newPrinter3.getProdID())
