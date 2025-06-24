from abc import ABC, abstractmethod
class product(ABC):
    def __init__(self, name, price):
        self.name = name
        self._price = price
      
    @property
    @abstractmethod
    def price(self):
        return self.price
    
    @price.setter
    def price(self, value):
        if value < 0:
            raise ValueError("Price cannot be negative")
        self._price = value 

    def __str__(self):
        return f"Product: {self.name}, Price: {self.price}, Quantity: {self.quantity}, Total Price: {self.total_price()}"
    
    def __eq__(self, other):
        if isinstance(other, product):
            return self.name == other.name and self.price == other.price
        return False
        
    def __hash__(self):
        return hash(self.name)    
        