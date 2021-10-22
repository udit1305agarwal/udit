mytuple = 12,23,1,23,13131,313,13,144411,4141,2
print(mytuple.count(1),'occurance of 1')
print(mytuple.index(13))

for i in mytuple:
    print(i, end=' ')
print('\nreversed')
for i in mytuple[::-1]:
    print(i, end=" ")
