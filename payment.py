from abc import ABC, abstractmethod
class Payment(ABC):
    """Abstract base for payment methods."""
    @abstractmethod
    def pay(self, amount: float) :
        pass

class StripeProcessor(Payment):
    def pay(self, amount: float):
        print(f"[Stripe] Charged ${amount:.2f}")

class PaypalProcessor(Payment):
    def pay(self, amount: float):
        print(f"[PayPal] Charged ${amount:.2f}")
