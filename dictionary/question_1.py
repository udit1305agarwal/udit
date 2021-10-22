# wap tp ask the user his/her expenses on different items
# .take around 15 key and value from user
# .and then perform sum and average on the values
expenses = {}
for i in range(5):
   k = input("enter items")
   v = int(input('price > '))
   expenses[k] = v
total = sum(list(expenses.values()))
average = sum(list(expenses.values())/len(expenses))
print(f"total is {total}, average is {average}")
    