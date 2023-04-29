class ProdMainClass(object):
    """ суперкласс для объектов (продуктов)
    должен уметь выдавать ID"""
    id = 0

    def __init__(self, **kwargs):
        """ при инициализации класса указываются пары ключ=значение через запятую
        пример name="iPhone", brand="Apple"
        """
        self.prod = dict()
        """ продукт в виде словаря"""
        ProdMainClass.id += 1
        self.prod.update(kwargs)
        self.prod.update(label="")
        # self.prod.update(id=PrinterProd.id)
        # print(f" Super id {ProdMainClass.id}")

    def get_prod_id(self):
        """ выдает значение ID обЪекта"""
        return ProdMainClass.id

    def get_prod_dict(self):
        """ метод выдает продукт в виде словаря"""
        return self.prod

    def get_prod_label(self, *args):
        """ метод получает список ключей по которым формируется label
        возвращает значение label"""
        label = ""
        if len(args) != 0:
            for key in args:
                label += str(self.prod[key]) + " "
        return label

