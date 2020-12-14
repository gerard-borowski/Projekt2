from abc import ABCMeta, abstractmethod


class ShippingProvider(metaclass=ABCMeta):

    @abstractmethod
    def calculate_cost(
        self,
        width: float,
        height: float,
        depth: float,
        mass: float
    ) -> float:
        raise NotImplementedError


class FedEx(ShippingProvider):
    def __init__(self, price: float, discount_rate: float):
        self._price = price
        self._discount_rate = discount_rate

    def calculate_cost(
        self,
        width: float,
        height: float,
        depth: float,
        mass: float
    ):
        volume = width * height * depth
        if mass <= 50:
            return volume * mass * self._price
        return self._price * volume * mass * (1 - self._discount_rate / 100.0)


class PostPoland(ShippingProvider):
    def __init__(self, price: float):
        self._price = price

    def calculate_cost(
        self,
        width: float,
        height: float,
        depth: float,
        mass: float
    ):
        volume = width * height * depth
        return volume * mass * self._price


class Calculator:
    def __init__(self, shipping_provider: ShippingProvider):
        self._shipping_provider = shipping_provider

    def calculate(
        self,
        width: float,
        height: float,
        depth: float,
        mass: float
    ):
        if self._shipping_provider is None:
            raise Exception('No shipping provider set')

        return self._shipping_provider.calculate_cost(
            width=width, height=height, depth=depth, mass=mass
        )

    def set_shipping_provider(self, new_shipping_provider):
        self._shipping_provider = new_shipping_provider


def main():
    post_poland = PostPoland(price=1.20)
    shipping_calculator = Calculator(post_poland)

    cost = shipping_calculator.calculate(15, 10, 20, 4)
    print(f'Shipping cost with Post Poland is {cost}')

    fedex = FedEx(price=5.25, discount_rate=10)
    shipping_calculator.set_shipping_provider(fedex)

    cost = shipping_calculator.calculate(15, 10, 20, 4)
    print(f'Shipping cost with FedEx is {cost}')

    cost = shipping_calculator.calculate(15, 10, 20, 51)
    print(f'Shipping cost with FedEx is {cost}')


if __name__ == '__main__':
    main()
