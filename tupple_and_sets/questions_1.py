# WAP to add values from user in a set.
# they can add any number of values in the set
# use while loop to perform this task
a = set()
while (True):
    x = input("enter values in a set")
    if not x:
        break
    a.add(x)
print(a)
