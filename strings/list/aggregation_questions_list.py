# WAP to find the sum of all values in anumerical list
x = [123,2332,31313,444,11,2]
total = 0
for i in x:
    total += i
print(x,'>> total =', total)
total = sum(x)
print(total)
#  average
x_mean = sum(x) / len(x)
print(x_mean)
