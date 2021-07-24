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

    class NewCls(cls):

        counter = 0
        setattr(cls, 'counter', counter)

        def __init__(self, *args, **kwargs):
            super(type(cls), cls).__init__()
            cls.counter += 1

        setattr(cls, '__init__', __init__)

        @staticmethod
        def get_created_instances(*args):
            return cls.counter

        setattr(cls, 'get_created_instances', get_created_instances)

        @staticmethod
        def reset_instances_counter(*args):
            temp_value = cls.counter
            cls.counter = 0
            return temp_value

        setattr(cls, 'reset_instances_counter', reset_instances_counter)

    return cls


@instances_counter
class User:
    def __init__(self):
        print("Hello User!")


if __name__ == '__main__':

    User.get_created_instances()  # 0
    user, _, _ = User(), User(), User()
    user.get_created_instances()  # 3
    user.reset_instances_counter()  # 3
