phrase = """
It is a really long string
triple-quoted strings are used
to define multi-line strings
"""
length = len(phrase)
print(length)
print(type(length))
#first_half = phrase[:int(length/2)]
first_half = phrase[:int(length/2)]
first_half_length = len(first_half)
print(first_half)
print(first_half_length)

