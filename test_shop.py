import pytest
from models import Product, Cart


@pytest.fixture
def product():
    return Product("book", 100, "This is a book", 1000)

@pytest.fixture
def cart():
    return Cart()

class TestProducts:
    def test_product_check_quantity(self, product):
        assert product.check_quantity(1000)
        assert not product.check_quantity(5000)

    def test_product_buy(self, product):
        product.buy(100)
        assert product.quantity == 900

    def test_product_buy_more_than_available(self, product):
        with pytest.raises(ValueError):
            product.buy(1010)

class TestCart:
    def test_add_product(self, cart, product):
        assert len(cart.products) == 0
        cart.add_product(product)
        assert len(cart.products) == 1

        cart.add_product(product, buy_count=5)
        assert len(cart.products) == 6


    def test_remove_product(self, cart, product):
        cart.add_product(product, buy_count=5)
        cart.remove_product(product,remove_count=2)
        assert cart.products[product] == 3

    def test_cart_clear(self, cart, product):
        cart.clear()
        assert product not in cart.products

        cart.add_product(product, buy_count=3)
        assert product in cart.products
        cart.clear()
        assert product not in cart.products

    def test_total_price(self, cart, product):
        cart.clear()
        assert cart.get_total_price() is None

        cart.add_product(product, buy_count=3)
        assert cart.get_total_price() == product.price * 3