wiki_content = '''tjhe klnanjd jnkjdbakjdbw iaghwbuhbwub aiugbdiwabdiabd iuagbduhvbbkJh q guqgigqiegqiug  zgigeig'''
words = wiki_content.split()
print(words)

# for word in words:
    # print(f'{word} -> {words.count(word)}')
max_frq = 0
mx_occ_world = ''
for item in words:
    count = words.count(item)
    print(f'{item} -> {count}')
    if count > max_freq:
        max_freq = count
        mx_occ_world = item
print(f'{mx_occ_world} =>>> {max_freq}')

