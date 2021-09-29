all_data = ""           
while True:
    line = input("~")
    if not line:
        break
    all_data += line+'\n'
print("Your data")
print(all_data)
print("you entered",len(all_data),"chars")
