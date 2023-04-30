from Connectors.ConSaveArrayMainClass import ConSaveArrayMainClass



class ConSavePrintersArray(ConSaveArrayMainClass):
    """ класс коннектора для записи массива телефонов в файл"""

    def __init__(self, file_name, append=True):
        """ используем базовый класс ConSaveArrayMainClass
        """
        super().__init__(file_name, append)



