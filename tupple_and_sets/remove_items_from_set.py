words = {'Lewandoski','Sane',"Ganabry"}
print(words)

if 'Sane' in words:
    words.remove("Sane")
print(words)

remvd_value = words.pop()
print(words)
print(remvd_value)
words.clear()
print(words)
