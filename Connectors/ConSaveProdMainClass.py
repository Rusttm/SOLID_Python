
class SaveConnectorMain(object):
    """ суперкласс для записи данных в файл"""

    def __init__(self, file_name):
        self.file_name = file_name
        """ запоминает имя файла"""

    def get_file_name(self):
        """ возвращает путь к файлу """
        return self.file_name

    def save_prod_2file(self, obj):
        """ метод записыват продукт(объект) в файл"""
        pass





