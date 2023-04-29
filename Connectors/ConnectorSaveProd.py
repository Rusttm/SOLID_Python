
class SaveConnectorMain(object):
    """ суперкласс для записи данных в файл"""

    def __init__(self, file_name):
        self.file_name = file_name
        """ запоминает имя файла"""

    def get_file_name(self):
        return self.file_name





