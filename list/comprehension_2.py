'''# syntax comprehension

newlist = [ operation loop-for-existing !condition! ]
'''
x = [2,3,51,2,74,877,1084,422]
# mapping
x2 = [i**2 for i in x]
print(x)
print(x2)
# filter 
x_odd = [i for i in x if i%2!=0]
print(x_odd)

x_odd_sqrs = [i**2 for i in x if i%2!=0]
print(x_odd_sqrs)