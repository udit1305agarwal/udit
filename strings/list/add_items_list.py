x = [] #empty 
print('enter 3 value:')
for i in range(3):
    val = input('->')
    x.append(val)
x.append(10)
x.append('Helium')
x.append(True)
x.append(['a','b','c'])
print(x)
# insert
x.insert(0,200)
print(x)
# extend
a = [1,2,3,4]
b = [3,2,1,3]
a.extend(b)
print(a)
b.extend(a)
print(b)