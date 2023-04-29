from MyModels.ProdMainClass import ProdMainClass


class PrinterProd(ProdMainClass):
    id = 0

    def __init__(self):
        super().__init__()
        PrinterProd.id = super().getProdID()
