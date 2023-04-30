class ProdMainClass(object):
    """ суперкласс для объектов (продуктов)
    должен уметь выдавать
    get_prod_id : ID
    get_prod_dict: сам продукт в виде словаря
    """
    id = 0

    def __init__(self, **kwargs):
        """ при инициализации класса указываются пары ключ=значение через запятую
        пример name="iPhone", brand="Apple"
        """
        self.prod = dict()
        """ продукт в виде словаря"""
        # ProdMainClass.id += 1
        self.id += 1
        self.prod.update(kwargs)
        self.prod.update(label="No Label")


    def get_prod_id(self):
        """ выдает значение ID обЪекта"""
        return self.id

    def get_prod_dict(self):
        """ метод выдает продукт в виде словаря"""
        return self.prod
