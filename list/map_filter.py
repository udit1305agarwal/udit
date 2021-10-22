x = [1,2,3,42424,55,3]
words = "Python is the best lang for coding".split()
'''
map() - mordern way for mapping a sequence for a operation in 1 line
filter() - mordern way for filtering a sequence using condition in 1 line'''
'''
map() and reduce() use lazy objects concept,
 in which data is not cnsuming memory until it is
 casted to a particular datatype like list, tuple, set
'''
x2 = list(map(lambda i : i ** 2, x))
y = [2,3,4,5,6,7,5]
f = lambda i,j: i + j
if len(x) == len(y): 
    xy = list(map(f, x, y))
    print(xy)

# filter 
words_with_a = list(filter(lambda i: "n" in i, words)
print(words_with_a)
