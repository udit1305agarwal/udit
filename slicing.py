name = "Vijay deenanath chauhan"
print("size",len(name))
print(name[2:5])
print(name[6:-8])
# we can skip value before colon if we want to start from beginning
# we can skip value after colon if we want to stop at the end
print(name[:5])
print(name[-7:])
#  syntax for slicing
#  var[startIdx : endIdx : gap]
print(name[::2]) # start to end with gap of 2 index
print(name[1::2]) # 1 index to end with gap of 2 index
# reverse string
print(name[::-1])
print(name[:])
print(name[:][::-1][:-5])
print(name[1::2]) # 1 index to end with gap of 2 index