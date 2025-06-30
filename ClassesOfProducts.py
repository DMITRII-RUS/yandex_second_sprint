class Product:
    # Опишите инициализатор класса.
    # Инициализатор должен принять на вход
    # название (name) и количество (quantity) товара.
    # В теле инициализатора задайте соответствующие атрибуты экземпляра класса.
    def __init__(self, name: str, quantity: int):
        self.name = name
        self.quantity = quantity

    def get_basic_info(self):
        result = f'{self.name} (в наличии: {self.quantity})'
        return result

    def get_full_info(self):
        pass


class Kettlebell(Product):
    # Опишите инициализатор класса и переопределите метод get_full_info()
    def __init__(
        self,
        name: str,
        quantity: int,
        weight: int
    ):
        super().__init__(name, quantity)
        self.weight = weight

    def get_full_info(self) -> str:
        result_1 = self.get_basic_info()
        result_2 = f'. Вес: {self.weight} кг'
        result = result_1 + result_2
        return result


class Clothing(Product):
    # Опишите инициализатор класса и переопределите метод get_full_info()
    def __init__(
        self,
        name: str,
        quantity: int,
        size: str
    ):
        super().__init__(name, quantity)
        self.size = size

    def get_full_info(self) -> str:
        result_1 = self.get_basic_info()
        result_2 = f'. Размер: {self.size}'
        result = result_1 + result_2
        return result


# Для проверки вашего кода создадим пару объектов...
small_kettlebell = Kettlebell('Гиря малая', 15, 2)
shirt = Clothing('Футболка', 5, 'L')
milk = Product('Молоко', 100)

# ...и вызовем их методы:
print(small_kettlebell.get_full_info())
print(shirt.get_full_info())
print(milk.get_basic_info())
