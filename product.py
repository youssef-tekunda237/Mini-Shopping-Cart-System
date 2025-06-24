from abc import ABC, abstractmethod

class product(ABC):
    def __init__(self, name, price):
        self.name = name
        self._price = price
      
    @property
    @abstractmethod
    def price(self):
        pass  # Abstract, must be implemented in subclass
    
    @price.setter
    def price(self, value):
        if value < 0:
            raise ValueError("Price cannot be negative")
        self._price = value 

    def __str__(self):
        return f"Product: {self.name}, Price: {self.price}"

    def __eq__(self, other):
        if isinstance(other, product):
            return self.name == other.name and self.price == other.price
        return False
        
    def __hash__(self):
        return hash(self.name)

class simpleProduct(product):
    @property
    def price(self):
        return self._price
