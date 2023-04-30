from MyModels.ProdMainClass import ProdMainClass

class ProdLabelMainClass(ProdMainClass):
    """ расширение класса ProdMainClass для добавления label"""

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def set_prod_label(self, *args):
        """ метод получает список ключей по которым формируется label"""
        label = ""
        if len(args) != 0:
            for key in args:
                if key in self.prod.keys():
                    label += str(self.prod[key]) + " "
        label = label[0:-1]
        self.prod["label"] = label

    def get_prod_label(self):
        """ возвращает значение label"""
        return self.prod["label"]