class Symbol(object):
    def __init__(self, value):
        self.value = value

    def __eq__(self, other):
        if isinstance(self, other.__class__):
            return self.value == other.value
        else:
                return NotImplemented
    def __hash__(self):
        return hash(self.value)

            
x = Symbol("Py")
y = Symbol("Py")

symbols = set()
symbols.add(x)
symbols.add(y)

print(x is y)
print(x == y)
print(len(symbols))
