def avg(number=[]):
    if number:
        return sum(number)/len(number)
# print(avg(12,33,44,55,66))
# print(avg()) 
# print(avg(3131,441,414141,414141,41414,14141,41))

def stats(*val, action='max'):
    ''' 
    function for doing stats , like min, max, sum, avg, count, etc
    '''
    if val:
        if action == 'max':
            return max(val)
        elif action == 'min':
            return min(val)
        elif action == 'avg':
            return len(val)
        elif action == 'all':
            return max(val), min(val), sum(val), avg(val)
print("calling stats")
print(stats(1,2,3,4,5566,7,4,3,34,43,3,332))
print(stats(13,4,555,6,6,action='all'))
