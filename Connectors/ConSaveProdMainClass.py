import os
from pathlib import Path
from MyModels.ProdMainClass import ProdMainClass


class SaveConnectorMain(object):
    """ суперкласс для записи данных в файл"""

    def __init__(self, file_name, append=False):
        """ при создании коннектора можно указать способ записи
        append=False перезаписыват файл
        append=True добавляет в файл
        """

        if append:
            self.append = "a"
        else:
            self.append = "w"
        p = Path(os.getcwd())
        self.file_name = f"{p.parent}/data/{file_name}"
        """ файл находится в директории data"""

    def get_file_name(self):
        """ возвращает путь к файлу """
        return self.file_name

    def save_prod_2file(self, phone: ProdMainClass):
        """ метод записывает в файл объект, который он преобразует в словарь"""
        prod_dict = phone.get_prod_dict()
        with open(self.file_name, self.append) as f:
            for key, value in prod_dict.items():
                f.write(f"{key}:{value};")
            f.write("\n")
