from homework11.tasks.hw1 import SimplifiedEnum


def test_metaclass():

    class ColorsEnum(metaclass=SimplifiedEnum):
        __keys = ("RED", "BLUE", "ORANGE", "BLACK")

    class SizesEnum(metaclass=SimplifiedEnum):
        __keys = ("XL", "L", "M", "S", "XS")

    assert ColorsEnum.RED == "RED"
    assert SizesEnum.XL == "XL"
