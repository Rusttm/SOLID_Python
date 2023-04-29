from Connectors.ConSaveProdMainClass import SaveConnectorMain


class ConSavePhonesArray(SaveConnectorMain):
    """ класс коннектора для записи телефона в файл"""

    def __init__(self, file_name, append=True):
        """ при создании коннектора можно указать способ записи
        append=False перезаписыват файл
        append=True добавляет в файл
        """
        super().__init__(file_name)

    def save_prod_array_2file(self, prod_array: list):
        """ метод записывает список объектов(телефонов) в файл """
        for prod in prod_array:
            self.save_prod_2file(prod)


