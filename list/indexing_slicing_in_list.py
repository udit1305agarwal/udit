num = list(range(20))
print(num)
print('first value',num[0])
print('seconf value',num[1])
print('last value',num[-1])
num[0] = 50
num[-1] = 20
print(num)
print('first 3 items',num[:3])
print('last 5 items',num[-5:])
print('all items except first 2 and lst 2',num[2 : -2])
print('reverse a list',num[::-1])
print('aljhh',num[::3])