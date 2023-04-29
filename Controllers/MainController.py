
from MyModels.PhoneProd import PhoneProd
from MyModels.PrinterProd import PrinterProd


class MainController(object):

    def runProgram(self):
        newPhone1 = PhoneProd()
        newPhone2 = PhoneProd()
        newPrinter1 = PrinterProd()
        newPrinter2 = PrinterProd()
        print(newPrinter2.getProdID())


if __name__ == "__main__":
    newController = MainController()
    newController.runProgram()