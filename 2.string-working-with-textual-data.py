message = "Hello world"
message = 'Bobby\'s world'
''' message = """Bobby's world was a good
cartoon in the 1998s
""" '''

# print(message)
# print(len(message))
# print(message[0])
# print(message[10])
# Slicing
# print(message[0:5])
# print(message[:5])
# print(message[6:])
# String Methods
# print(message.lower())
# print(message.upper())
# print(message.count('b')) 
# print(message.find('world'))
# print(message.find('java'))
# print(message)
# new_message = message.replace('world', 'universe')
# print(new_message)

greeting = 'Hello'
name = 'Michael'
message = greeting + ' ' + name + '. Welcome!'
message = '{} {}. Welcome!'.format(greeting, name)
message = f'{greeting} {name.upper()}. Welcome!'
print(message)
# print(dir(name))
# print(help(str))
print(help(str.lower))
