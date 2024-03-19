
class Product:
    """
    Класс продукта
    """
    name: str
    price: float
    description: str
    quantity: int

    def __init__(self, name, price, description, quantity):
        self.name = name
        self.price = price
        self.description = description
        self.quantity = quantity

    def check_quantity(self, quantity) -> bool:
        return self.quantity >= quantity
        #Верните True если количество продукта больше или равно запрашиваемому и False в обратном случае

    def buy(self, quantity):
        if self.check_quantity(quantity):
            self.quantity -= quantity
        else:
            raise ValueError("Not enough product")
        #реализуйте метод покупки. Проверьте количество продукта используя метод check_quantity
        # Если продуктов не хватает, то выбросите исключение ValueError

    def __hash__(self):
        return hash(self.name + self.description)


class Cart:
    products: dict[Product, int]

    def __init__(self):
        self.products = {}

    def add_product(self, product: Product, buy_count=1):
        if product in self.products:
            self.products[product] += buy_count
        else:
            self.products[product] = buy_count
        #Метод добавления продукта в корзину.
        #Если продукт уже есть в корзине, то увеличиваем количество


    def remove_product(self, product: Product, remove_count=None):
        if product in self.products:
            if remove_count is None or self.products[product] <= remove_count:
                del self.products[product]
            else:
                self.products[product] -= remove_count
        #Метод удаления продукта из корзины.
        #Если remove_count не передан, то удаляется вся позиция
        #Если remove_count больше, чем количество продуктов в позиции, то удаляется вся позиция


    def clear(self):
        self.products.clear()

    def get_total_price(self) -> float:
        total_price = 0
        for product, quantity in self.products.items():
            total_price += product.price * quantity
            return total_price

    def buy(self):
        for product, quantity in self.products.items():
            if product.quantity < quantity:
                raise ValueError("Product not enough")
            else:
                product.buy(quantity)
        #Метод покупки.
        #Учтите, что товаров может не хватать на складе.
        #В этом случае нужно выбросить исключение ValueError