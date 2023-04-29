from Connectors.ConSaveProdMainClass import SaveConnectorMain
from MyModels.PhoneProd import PhoneProd
import os
from pathlib import Path


class ConSavePhone(SaveConnectorMain):
    """ класс коннектора для записи телефона в файл"""

    def __init__(self, file_name, append=False):
        """ при создании коннектора можно указать способ записи
        append=False перезаписыват файл
        append=True добавляет в файл
        """
        super().__init__(file_name)
        if append:
            self.append = "a"
        else:
            self.append = "w"

        p = Path(os.getcwd())
        self.file_name = f"{p.parent}/data/{file_name}"
        """ файл находится в директории data"""

    def save_prod_2file(self, phone: PhoneProd):
        """ метод записывает в файл объект, который он преобразует в словарь"""
        prod_dict = phone.get_prod_dict()
        with open(self.file_name, self.append) as f:
            for key, value in prod_dict.items():
                f.write(f"{key}:{value};")
            f.write("\n")

    def get_file_name(self):
        return self.file_name
