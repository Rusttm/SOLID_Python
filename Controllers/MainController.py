
from MyModels.PhoneProd import PhoneProd
from MyModels.PrinterProd import PrinterProd
from Connectors.ConSavePhone import ConSavePhone

class MainController(object):

    def runProgram(self):
        phone1 = PhoneProd(name="iPhone", model="SE", brand="Apple", year="2015", memory="64", descr="refurbished",
                              price="52000")
        phone2 = PhoneProd(name="iPhone", model="13 Pro Max", brand="Apple", year="2020", memory="256", descr="new",
                              price="125000")
        phone3 = PhoneProd(name="Redmi", model="MI9", brand="Xiaomi", year="2018", memory="64", descr="",
                              price="11000")
        printer1 = PrinterProd(name="Ecosys", model="P2040", brand="Kyosera", price="55000")
        printer2 = PrinterProd(name="LaserJet", model="M111A", brand="HP", price="14000")
        printer3 = PrinterProd(name="ImageClass", model="LBP6030", brand="Canon", price="23000")
        print(printer2.get_prod_dict())

        # phone_conn = ConSavePhone("phones_db.txt")
        # phone_conn.save_prod_2file(phone2)
        # print(printer2.get_prod_id())
        #
        # printer_conn = ConSavePhone("printers_db.txt", append=True)
        # printer_conn.save_prod_2file(printer1)



if __name__ == "__main__":
    newController = MainController()
    newController.runProgram()