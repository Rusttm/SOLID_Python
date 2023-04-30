
from MyModels.PhoneProd import PhoneProd
from MyModels.PrinterProd import PrinterProd
from Connectors.ConSavePhone import ConSavePhone
from Connectors.ConSavePhoesArray import ConSavePhonesArray

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

        # можем  выдать продукт(объекта) в виде словаря
        print(printer2.get_prod_dict())

        # можем получить ID продукта(объекта)
        print(printer2.get_prod_id())

        # можно записать один телефон
        phone_conn = ConSavePhone("phones_db.txt")
        phone_conn.save_prod_2file(phone3)

        # или записать массив телефонов
        phones_array = [phone1, phone2]
        phones_array_conn = ConSavePhonesArray("phones_db.txt")
        phones_array_conn.save_prod_array_2file(phones_array)

        # то же касается и принтеров
        # запись одного принтера
        printer_conn = ConSavePhone("printers_db.txt")
        printer_conn.save_prod_2file(printer1)

        # запись массива принтеров
        printers_array = [printer2,  printer3]
        printers_array_conn = ConSavePhonesArray("printers_db.txt")
        printers_array_conn.save_prod_array_2file(printers_array)


if __name__ == "__main__":
    newController = MainController()
    newController.runProgram()