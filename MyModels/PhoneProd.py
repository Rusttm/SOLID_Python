
from MyModels.ProdMainClass import ProdMainClass


class PhoneProd(ProdMainClass):
    id = 0

    def __init__(self):
        super().__init__()
        self.id = super().getProdID()
        print(f"{self.id=}")



if __name__ == "__main__":
    newClassObj = PhoneProd()
    newClassObj2 = PhoneProd()
    newClassObj3 = PhoneProd()
