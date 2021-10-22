word = {}#dict
word['alpha'] = "number one, the strating value, or the top value"
print("user input-->")
for i in range(3):
    k = input("enter a word")
    v = input("enter the meaning")
    word[k] = v
print(word)
# reading a particular
print(word['alpha'])
print(word['beta'])
print(word.get('beta','not found'))