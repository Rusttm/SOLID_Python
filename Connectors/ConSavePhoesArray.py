from Connectors.ConSaveArrayMainClass import ConSaveArrayMainClass



class ConSavePhonesArray(ConSaveArrayMainClass):
    """ класс коннектора для записи массива телефонов в файл
    создан на базе класса ConSaveArrayMainClass"""

    def __init__(self, file_name, append=True):
        """ используем базовый класс ConSaveArrayMainClass
        """
        super().__init__(file_name, append)



