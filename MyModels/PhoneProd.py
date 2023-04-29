
from MyModels.ProdMainClass import ProdMainClass


class PhoneProd(ProdMainClass):
    id = 0

    def __init__(self, **kwargs):
        super().__init__()
        self.id = PhoneProd.id = super().get_prod_id()
        self.prod = dict()
        """ продукт в виде словаря"""
        self.prod.update(kwargs)
        self.prod.update(id=PhoneProd.id)

    def get_prod_dict(self):
        """ метод выдает продукт в виде словаря"""
        return self.prod

    def get_prod_id(self):
        return self.id




if __name__ == "__main__":
    newPhone1 = PhoneProd(name="iPhone", model="SE", brand="Apple", year="2015", memory="64", descr="refurbished", price="52000")
    newPhone2 = PhoneProd(name="iPhone", model="13 Pro Max", brand="Apple", year="2020", memory="256", descr="new", price="125000")
    newPhone3 = PhoneProd(name="Redmi", model="MI9", brand="Xiaomi", year="2018", memory="64", descr="", price="11000")
    print(f"Порядковый номер телефона(id) {newPhone3.get_prod_id()}")
    print(f"Телефон в виде словаря {newPhone2.get_prod_dict()}")