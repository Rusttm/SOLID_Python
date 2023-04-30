from Connectors.ConSaveProdMainClass import SaveConnectorMain


class ConSavePhone(SaveConnectorMain):
    """ класс коннектора для записи телефона в файл"""

    def __init__(self, file_name, append=False):
        """ при создании коннектора можно указать способ записи
        append=False перезаписыват файл
        append=True добавляет в файл
        """
        super().__init__(file_name, append)
