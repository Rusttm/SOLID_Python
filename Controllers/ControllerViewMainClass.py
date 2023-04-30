class ControllerViewMainClass(object):
    """ класс для работы с view """
    id = 0

    def __init__(self, descr=""):
        """ при инициализации класса можно указать описание"""
        self.id += 1
        self.descr = str(self.id) + ". " + descr

    def get_descr(self):
        """ возвращает название контроллера"""
        return self.descr
