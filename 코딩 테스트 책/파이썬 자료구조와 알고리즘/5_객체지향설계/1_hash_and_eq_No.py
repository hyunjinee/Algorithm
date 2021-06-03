class Symbol(object):
    def __init__(self,value):
        self.value = value


x = Symbol("Py")
y = Symbol("Py")

symbols = set()
symbols.add(x)
symbols.add(y)

print(x is y)
print(x == y)
print(len(symbols))

# 두변수 xy의 참조가 다르므로 False
