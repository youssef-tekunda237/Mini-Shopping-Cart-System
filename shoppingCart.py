from typing import Dict
from product import product
class shoppingCart:
    def __init__(self) -> None:
        # keys are normalized product names; values are tuples: (Product, quantity)
        self.items: Dict[str, tuple[product, int]] = {}

    def add_item(self, product: product, qty: int = 1) -> None:
        key = product.name.strip().lower()  # Normalize
        if key in self.items:
            _, current_qty = self.items[key]
            self.items[key] = (product, current_qty + qty)
        else:
            self.items[key] = (product, qty)
        print(f"Added {qty} x {product.name}")

    def remove_item(self, product_name: str, qty: int = 1) -> None:
        key = product_name.strip().lower()  # Normalize
        entry = self.items.get(key)
        if not entry:
            print(f"No item named '{product_name}' in cart.")
            return

        product, current_qty = entry
        if qty >= current_qty:
            del self.items[key]
            print(f"Removed all of '{product_name}'")
        else:
            self.items[key] = (product, current_qty - qty)
            print(f"Removed {qty} x {product_name}")

    def view_cart(self) -> None:
        if not self.items:
            print("Your cart is empty.")
            return

        print("\nYour Cart:")
        for name, (product, qty) in self.items.items():
            line_total = product.price * qty
            print(f" - {qty} × {product} = ${line_total:.2f}")
        print(f"Subtotal: ${self.calculate_subtotal():.2f}")

    def calculate_subtotal(self) -> float:
        return sum(prod.price * qty for prod, qty in self.items.values())

    def calculate_total(self, discount: float = 0.0) -> float:
        """
        discount: percentage (e.g. 10.0 for 10% off)
        """
        subtotal = self.calculate_subtotal()
        if discount:
            return subtotal * (1 - discount / 100)
        return subtotal
    def clear_cart(self) -> None:
        self.items.clear()
        print("Cart cleared.")