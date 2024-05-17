class Calculator:
    def add(self, a, b, c=None):
        if c is not None:
            return a + b + c
        else:
            return a + b

Cal = Calculator()
print("Add Two Numbers =", Cal.add(5, 4))
print("Add Three Numbers =", Cal.add(3, 4, 8))
