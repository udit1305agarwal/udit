def gutenberg_g():
    file = open('dummy.txt')
    content = file.read()
    c = 0
    for i in content:
        words = content.split()
        c =+ len(words)
        return c
    file.close()
file_to_read = 'question_gutenberg.py'
file_to_write = "answer_gutenberg.py"
x = open(file_to_read,'r')
data = x.read()
x.close()

with open(file_to_write,'a') as x:
    x.write(data)