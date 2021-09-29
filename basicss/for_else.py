# prime number
num = int(input("enter the number"))
for i in range(2,num):
    if num % i == 0:
        print("non prime value", num)
        break
else:
    print("Prime value", num)