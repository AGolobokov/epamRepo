"""
Vasya implemented nonoptimal Enum classes.
Remove duplications in variables declarations using metaclasses.

from enum import Enum


class ColorsEnum(Enum):
    RED = "RED"
    BLUE = "BLUE"
    ORANGE = "ORANGE"
    BLACK = "BLACK"


class SizesEnum(Enum):
    XL = "XL"
    L = "L"
    M = "M"
    S = "S"
    XS = "XS"


Should become:

class ColorsEnum(metaclass=SimplifiedEnum):
    __keys = ("RED", "BLUE", "ORANGE", "BLACK")


class SizesEnum(metaclass=SimplifiedEnum):
    __keys = ("XL", "L", "M", "S", "XS")


assert ColorsEnum.RED == "RED"
assert SizesEnum.XL == "XL"
"""

# Основная цель метаклассов — автоматически изменять класс в момент создания.
# перехватить создание класса
# изменить класс
# вернуть модифицированный


class SimplifiedEnum(type):
    def __new__(cls, name, bases, namespace):
        # cls - SimplifiedEnum,
        # name - имя определяемого класса (ColorsEnum, SizesEnum))
        # bases - базовые классы для построенного класса
        # namespace - словарь определенных в класса методов и полей
        for name in namespace[f"_{name}__keys"]:
            namespace[name] = name
        return super(SimplifiedEnum, cls).__new__(cls, name, bases, namespace)
