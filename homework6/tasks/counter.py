"""
Написать декоратор instances_counter, который применяется к любому классу
и добавляет ему 2 метода:
get_created_instances - возвращает количество созданых экземпляров класса
reset_instances_counter - сбросить счетчик экземпляров,
возвращает значение до сброса
Имя декоратора и методов не менять

Ниже пример использования
"""


def instances_counter(cls):
    """Some code"""

    class NewCls:

        counter = 0
        setattr(cls, 'counter', counter)

        def __init__(self, *args, **kwargs):
            cls.counter += 1
            self._obj = cls(*args, **kwargs)

        @staticmethod
        def get_created_instances(*args):
            return cls.counter

        property(get_created_instances)
        setattr(cls, 'get_created_instances', get_created_instances)

        @staticmethod
        def reset_instances_counter(*args):
            temp_value = cls.counter
            cls.counter = 0
            return temp_value

        property(reset_instances_counter)
        setattr(cls, 'reset_instances_counter', reset_instances_counter)
    return NewCls


@instances_counter
class User:
    pass


if __name__ == '__main__':

    User.get_created_instances()  # 0
    user, _, _ = User(), User(), User()
    user.get_created_instances()   # 3
    user.reset_instances_counter() # 3
