x = {1,2,3,11,23}
y = {1,2,3,4,5,6}
common = x.intersection(y)
print("x and y have",common)
xuniq = x.difference(y)
yuniq = y.difference(x)
print(xuniq)
print(yuniq)
x.intersection_update(y)