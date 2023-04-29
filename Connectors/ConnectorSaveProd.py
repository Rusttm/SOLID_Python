import AbstractConnector


class SaveConnector(AbstractConnector):
    id = 0

    def __init__(self, nameFile):
        self.id += 1
        self.nameFile = nameFile




