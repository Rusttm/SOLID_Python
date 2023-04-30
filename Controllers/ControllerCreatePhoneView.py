from Controllers.ControllerViewMainClass import ControllerViewMainClass

from Views.ViewCreatePhone import ViewCreatePhone

class ControllerCreatePhoneView(ControllerViewMainClass):
    """ класс контроллера для работы с View создания продукта"""

    def __init__(self):
        super().__init__()
        self.view = ViewCreatePhone()
        """ создает объект - View"""

    def print_item(self, key=""):
        """ транслирует значение ключа в View"""
        self.view.print_items(key)

    def add_info(self, info):
        self.view.add_info(info)

    def get_answer(self):
        answer = str(input())
        return answer


