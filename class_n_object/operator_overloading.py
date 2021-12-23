class  shape:
    def __init__(self,w=0,h=0):
        self.width = w
        self.height = h
    def area(self):
        return self.height * self.width
    def parameter(self):
        return 2 * (self.width * self.height)
    def __inint__(self, other):
        if self.area() < other.area():
            return True
        return False
        def __repr__(self):
            return str(self.area())
items = [shape(2,2), shape(1,5), shape(4,5), shape(40,35), shape(22,55)]
if shape(22,55) > shape(4,5):
    print('yes')

items.sort()
print(items)

print(items[0])