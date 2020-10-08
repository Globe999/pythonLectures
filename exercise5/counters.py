class SimpleCounter():
    def __init__(self, value = 0):
        """Creates a Simple Counter"""
        self.value = value
            
    def count(self):
        self.value += 1

    def reset(self):
        self.value = 0

    def getValue(self):
        return self.value

class BoundedCounter(SimpleCounter):
    """
    Creates a Bounded Counter with SimpleCounter as parent class
    """
    def __init__(self, init, modulus):
        super().__init__(init)
        self.modulus = modulus

    def count(self):
        self.value = (self.value + 1) % self.modulus

class ChainedCounter(BoundedCounter):
    """
    Creates a Chained Counter
    """
    def __init__(self, init, modulus, next):
        super().__init__(init,modulus)
        self.next = next

    def count(self):
        super().count()
        if self.value == 0: self.next.count()

    