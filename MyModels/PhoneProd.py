from MyModels.ProdLabelMainClass import ProdLabelMainClass

class PhoneProd(ProdLabelMainClass):
    # id = 0

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        # print(self.id)

        self.id = PhoneProd.id = super().get_prod_id()
        self.prod.update(id=PhoneProd.id)
        self.set_prod_label("brand", "name", "model")
        self.req_field = None
        self.set_requred_fields()

    def set_requred_fields(self, fields_array=None):
        """ устанавливает список обязательных полей для ввода"""
        if fields_array is None:
            fields_array = ["brand", "name", "model", "memory"]
        self.req_field = fields_array

    def get_requred_fields(self):
        """ возвращает список обязательных полей для ввода"""
        return self.req_field




if __name__ == "__main__":
    newPhone1 = PhoneProd(name="iPhone", model="SE", brand="Apple", year="2015", memory="64", descr="refurbished", price="52000")
    newPhone2 = PhoneProd(name="iPhone", model="13 Pro Max", brand="Apple", year="2020", memory="256", descr="new", price="125000")
    newPhone3 = PhoneProd(name="Redmi", model="MI9", brand="Xiaomi", year="2018", memory="64", descr="", price="11000")
    print(f"Порядковый номер телефона(id) {newPhone1.get_prod_id()}")
    print(f"Порядковый номер телефона(id) {newPhone2.get_prod_id()}")
    print(f"Порядковый номер телефона(id) {newPhone3.get_prod_id()}")
    print(f"Телефон в виде словаря {newPhone3.get_prod_dict()}")