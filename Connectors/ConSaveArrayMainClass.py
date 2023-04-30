from Connectors.ConSaveProdMainClass import SaveConnectorMain


class ConSaveArrayMainClass(SaveConnectorMain):
    """ дочерний класс коннектора SaveConnectorMain для записи массива телефонов в файл
    создан на основе класса SaveConnectorMain с добавлением метода
    save_prod_array_2file
    """

    def __init__(self, file_name, append=True):
        """ при создании коннектора указываем добавление
        append=False перезаписыват файл
        append=True добавляет в файл
        """
        super().__init__(file_name, append)

    def save_prod_array_2file(self, prod_array: list):
        """ метод по порядку записывает список объектов(телефонов) в файл """
        for prod in prod_array:
            self.save_prod_2file(prod)


