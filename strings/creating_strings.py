name = "Alex mason"
city = 'Ney york'
story = '''this is a story about
alex mason, okay!
this guy is so good
that i cnat tell you'''
poem = """
johnny johnny,yes papa
eating sugar,no papa
thats okay,you did not lie
"""
print(type(name), type(city), type(story), type(poem))
print(name)
print(city)
print(story)
print()
print(poem)
properties = '''
1. indexed
2. immutable
3. str() is the constructor for creating strings [type cast]
4. it can be concatenated using +
5. it can be duplicated using *'''
print(properties)
name[0] = 'B' #will not work as strings are immutable
