x = {1,2,3,4,5,6,7,8,9,0}
y = {2,3,1,5}
z = {11,12,13,14}
a = {1,2,3,99,60}

print("x is a superset of y" , x.issuperset(y))
print("x is a superset of y" , x.issuperset(z))
print("x is a superset of y" , x.issuperset(a))

print("y is subset of x", y.issuperset(z))
print("a is unrelated to x", a.isdisjoint(x))
print("a is unrelated to x", a.isdisjoint(y))
