import orderStatus, payment, shoppingCart
class Order:
    """Handles checkout and order status."""
    def __init__(self, cart: shoppingCart, processor: payment) -> None:
        self.cart = cart
        self.processor = processor
        self.status: orderStatus = orderStatus.PENDING

    def checkout(self) -> None:
        total = self.cart.calculate_total()
        self.processor.pay(total)
        self.status = orderStatus.COMPLETED
        self.cart.clear_cart()

    def __str__(self) -> str:
        return f"Order({len(self.cart.items)} items) - Status: {self.status.name}"
