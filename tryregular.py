import re
fruit_list = ['apple', 'banana', 'peach', 'plum', 'pineapple', 'kiwi']
fruit = re.compile('|'.join(fruit_list))
print type(fruit)