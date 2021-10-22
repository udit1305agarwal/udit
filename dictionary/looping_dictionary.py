stdDict = {
    "name" : "billu",
    "maths" : 17,
    "english" : 15,
    "hindi" : 12,
    "age" : 14,
    "studies" : False,
    "delinquent" : True,
    "mobile no." : 93939393993
    }
print('only keys from dictionary')
for i in stdDict:
    print(i)
for item in stdDict:
    print(stdDict[item], end=' ')
for k,v in stdDict.items():
    print(k,'=>',v, end=' ')
    