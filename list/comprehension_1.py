# mapping without comprehension
x = [1,2,3,4,5,6,7,8,9,10]

# x2 = []
# for i in x:
#     sqr = i ** 2
#     x2.append(sqr)
# print(x)
# print(x2)

x3 = []
for i in x:
    cube = (i ** 2) * i
    x3.append(cube)
    print(x)
    print(x3)

# filter without comprehension
x_even = []
for i in x:
    if i%2 == 0:
        x_even.append(i)
print(x)
print(x_even)

