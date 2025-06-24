from product import product
class discountedProduct(product):
    def __init__(self, name: str, price: float, discount_percent: float) : 
        super().__init__(name)
        self.base_price = price
        self.discount_percent = discount_percent

    def price(self) :
        return self.base_price * (1 - self.discount_percent / 100)