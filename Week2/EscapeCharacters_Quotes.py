# we can use escape char to add specific symbols that we usualy can not add
# we can do so using '\'
a = 'It\'s a beautiful day'
print(a)
# '\'' is treadted as single character
print(len(a))

a = "We are from \"IIT\" Madras"
print(a)

print("My name is Ashutosh,\tI am from Pune.") # tab
print("My name is Ashutosh,\nI am from Pune.") # newline

# combination of quotes
print("It's a beautiful day") # single quote inside double quotes without escape
print('We are from "IIT" Madras') # double quotes inside single quote without escape

# when to use which quotes
# single and double quotes are to represent strings spanning single line
# triple quotes can be used to represent strigs spanning multiple lines
a = '''first line
second line
third line'''
print(a)
print(type(a))
# also the triple quotes can be used to represent multiline comments
'''comment 1
comment 2
comment 3'''