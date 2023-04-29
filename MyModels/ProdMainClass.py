class ProdMainClass(object):
    """ суперкласс для объектов (продуктов)
    должен уметь выдавать ID"""
    id = 0

    def __init__(self):
        ProdMainClass.id += 1
        # print(f" Super id {ProdMainClass.id}")


    def get_prod_id(self):
        """ выдает значение ID обЪекта"""
        return ProdMainClass.id
