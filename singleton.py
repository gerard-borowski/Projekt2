def singleton(cls):
    instances = {}
    def get_instance(*args, **kwargs):
        if cls not in instances:
            instances[cls] = cls(*args, **kwargs)
        return instances[cls]
    return get_instance


@singleton
class MyClass:
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
