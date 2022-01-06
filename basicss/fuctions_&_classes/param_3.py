def word_counter(msg, limit):
    word = msg.split()
    wl = []
    for item in word:
        if len(item) == limit:
            wl.append(item)
    return len(wl)
data = '''the author who has made a
universe called cosmere is Brandon Sanderson'''
print("3 letter words count is:", word_counter(data, limit=3))
