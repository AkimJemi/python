# 1 capitalize()
# 2 ()
# 3 ()
# 4 ()
# 5 ()
# 6 ()
# 7 ()
# 8 ()
# 9 ()
# 10 ()
# 11 ()
# 12 ()
# 13 ()
# 14 ()
# 15 ()
# 16 ()
# 17 ()
# 18 ()
# 19 ()
# 20 ()
# 21 ()
# 22 ()
# 23 ()
# 24 ()
# 25 ()
# 26 ()
# 27 ()







# 28 & 29
text: str = 'That is BaBcon.'
text2: str = 'ggggg Bb.'

table = text.maketrans('B', 'ⓔ')
print(text)
print(table)
print(text.translate(table))
print(text2.translate(table))

# 30 partition()
text: str = 'a+b=c'
print(text.partition('='))

# 32 removeprefix()
text: str = 'Wazzp'
print(text.removeprefix('Wazz'))

# 33 replace()
text: str = 'Remember to comment & comment!'
print(text.replace('comment', 'subscribe', 0))

# 34 rfind()
text: str = 'A: Some text. A'
print(text.rfind('B'))
print(text.rfind('A'))

# 35 rindex()
text: str = 'A: Some text. A'
# print(text.rindex('B'))  # if not found, raises error
print(text.rindex('A'))

# 36 rjust()
text: str = 'text'
print(text.rjust(20, '_'))

# 37 rpartition()
text: str = 'text=text2=text3'
print(text.rpartition('='))

# 38 split() & split()
text: str = 'This is some special stuff'
print(text.rsplit(sep=' ', maxsplit=2))

text: str = 'This is some special stuff'
print(text.split(maxsplit=2))

# 40 strip() & rstrip()
text: str = 'Mario, His name is Mario Mario'
print(text.strip('Mario'))
print(text.rstrip('Mario'))

# 41 splitlines()
text: str = 'Remember to comment!\nor else...\n'
print(text.splitlines())

# 42 startswith()
text: str = 'Luigi has pasta.'
print(text.strip('Luigi'))

# 44 swapcase()
text: str = 'Luigi has pastA.'
print(text.swapcase())

# 45 title()
text: str = 'this is a title'
print(text.title())

# 46 upper()
text: str = 'text'
print(text.upper())

# 47 zfill()
text: str = 'text'
print(text.zfill(5))
