from enum import Enum ,auto

class OrderStatus(Enum):
    PENDING = auto()
    COMPLETED = 1
    CANCELLED = 0
    FAILED = -1

    def __str__(self):
        return self.name.lower()