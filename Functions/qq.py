import file_function as ff
def sum_digit(numbers):
    sum = 0
    for d in str(numbers):
        sum += int(d)
    ff.writer('summer.txt',str(sum))
sum_digit(4444)

