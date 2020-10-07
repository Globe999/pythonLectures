class SimpleCounter():
    def __init__(self):
        """Creates a Simple Counter"""
        self.value = 0
    def count(self):
        self.value += 1

    def reset(self):
        self.value = 0

    def getValue(self):
        return self.value

class BoundedCounter():
    """
    Creates a Bounded Counter with SimpleCounter as parent class
    Fråga till Niklas: Kan man skapa en parent-klass som hanterar alla count, reset osv men om man behöver, kan man overrida dem genom att skriva metoden igen?

    """
    def __init__(self, init, modulus):
        self.value = init
        self.modulus = modulus

    def count(self):
        #Doesn't work, needs fixing
        # print(self.value % self.modulus)

        self.value = 0 if self.value == self.modulus-1 else self.value +1

    def reset(self):
        self.value = 0

    def getValue(self):
        return self.value

class ChainedCounter():
    """
    Creates a Chained Counter
    """
    def __init__(self, init, modulus, next):
        self.value = init
        self.modulus = modulus
        self.next = next

    def count(self):
        #Doesn't work, needs fixing
        # print(self.value % self.modulus)

        if self.value == self.modulus-1:
            self.reset()
            if self.next: self.next.count()
        else:
            self.value += 1

    def reset(self):
        self.value = 0

    def getValue(self):
        return self.value

    