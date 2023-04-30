

class ViewCreateProdMainClass(object):
    """ класс View для создания нового продукта """

    def print_items(self, key="name"):
        """ выводит на экран поле и меню комманд"""
        print(f"Введите значение для ключа {key}")
        print("Для отмены наберите X")

    def add_info(self, info=""):
        """ метод выводит дополнительную информацию"""
        print(info)