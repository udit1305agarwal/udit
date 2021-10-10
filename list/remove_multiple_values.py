x = [1,1,2,3,4,3,4,5,6,8,8,3,5,4,4,54,25,5,5,3,3,3,3,3,6,7,8,8,9,90]
# remove all the 3s in this list
y = x.copy()
for i in range(x.count(3)):
    x.remove(3)

print("Removed All 3")

# removing all the
while 3 in y:
    idx = y.index(3)
    y.pop(idx)
print(y) 

