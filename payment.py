from abc import ABC, abstractmethod
class payment(ABC):
    """Abstract base for payment methods."""
    @abstractmethod
    def pay(self, amount: float) :
        pass

class StripeProcessor(payment):
    def pay(self, amount: float):
        print(f"[Stripe] Charged ${amount:.2f}")

class PaypalProcessor(payment):
    def pay(self, amount: float):
        print(f"[PayPal] Charged ${amount:.2f}")
