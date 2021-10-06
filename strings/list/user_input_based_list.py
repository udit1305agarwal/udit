# wap to take user input to create a list
# the usser should decide the size of list
# the list should be numeric
# display list values and sum,min, mean of the list
n = int(input('enter the size of list>>'))
for i in range(n):
    val = int(input(f'{i+1}>>>'))
    n.append(val)
print("you entered the following values")
print(n)
print("sum >>",sum(n))
print("max value >>",max(n))
print("min value >>",min(n))
print("mean value >>",sum(n)/len(n))


