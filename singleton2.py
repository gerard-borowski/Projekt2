# https://stackoverflow.com/questions/6760685/creating-a-singleton-in-python


class Singleton(type):
    _instances = {}
    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super().__call__(*args, **kwargs)
        return cls._instances[cls]


class MyClass(metaclass=Singleton):
    def __init__(self, x):
        self.x = x


def main():
    obj1 = MyClass(42)
    obj2 = MyClass(12)
    obj3 = MyClass(32)

    print(id(obj1), id(obj2), id(obj3))
    print(obj1.x, obj2.x, obj3.x)

    assert id(obj1) == id(obj2), f'{id(obj1)}, {id(obj2)}'


if __name__ == '__main__':
    main()
