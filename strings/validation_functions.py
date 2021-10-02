value = input("enter something")
ans = value.isupper()
print("is the value entered is Upper?", ans)
ans = value.islower()
print("Is the value entered is Lower", ans)
ans = value.isalpha()
print("does the value contains only alphabet?", ans)
ans = value.isnumeric()
print("does the value contains only numbers?", ans)
ans = value.isspace()
print("does the value contains only space?", ans)
ans = value.isprintable()
print("is the value printable on screen?, ans")
ans = value.isdigit()
print("does the value contains only digits?", ans)
name = "Dr. Ram Verma"
if name.startswith("Dr"):
    print("hello Doctor")
if name.startswith("Mr"):
    print("Hello Mister")
file = input("enter the filename:")
if file.endswith(".doc"):
    print(f"{file} is Application file")
elif file.endswith(".exe"):
    print(f"{file} is Word file")
elif file.endswith(".png"):
    print(f"{file} is PDF file")