from abc import ABCMeta, abstractmethod


class Operation(metaclass=ABCMeta):
    @abstractmethod
    def execute(self, a, b):
        raise NotImplementedError


class Adder(Operation):
    def execute(self, a, b):
        return a + b


class Wrapper(Operation):
    def __init__(self, obj: Operation):
        self.obj = obj

    def execute(self, a, b):
        return self.obj.execute(float(a), float(b))


def main():
    a, b = '2', '3'

    adder = Adder()
    value1 = adder.execute(a, b)
    print(f'adder.execute({a}, {b}) = {value1}')

    wrapped_adder = Wrapper(adder)
    value2 = wrapped_adder.execute(a, b)
    print(f'wrapped_adder.execute({a}, {b}) = {value2}')


if __name__ == '__main__':
    main()


# Is it possible to achive such behaviour in python without Wrapper class? (+)
# Is there any difference between decorator design pattern and pythonic decorator?
