# Intro to Python ================~

# JS Data Types: Boolean, Numbers, Strings, Undefined, Null, NaN

'''
Data Types 🐍 ===============
Boolean
String
Integer (Number without decimal)
Float (a Decimal)
None

Tuples (Immutable Variable)
Dictionaries
Lists
'''

first_name = "Winter"
age = 99
is_instructor = True

# x = 10
# if x > 50:
#     print("bigger than 50")
# else:
#     print("smaller than 50")

# Print vs f-String(String Interpolation)

print('First Name : ' + first_name)
print(f'First Name : {first_name}')

# Conditionals

if age < 9000:
    print('Age is under 9000!')
else:
    print('Age is over 9000!')


# lists & loops
# Lists are ordered by their index value, just like in JS.
vacations = ['Bora-Bora', 'China', 'Yosemite', 'Ireland', 'Bali']

print(vacations[1])

for vacation in vacations: # Get each value from the list and put them into a variable called 'vacation'.
    print(vacation)
    for letter in vacation:
        print(letter)



# Range allows us to get numbers from 0 to the range provided, excludes the value used!
for num in range(1,11):
    print(num)

# Dictionaries - Key Value Pair

instructor_dict = {
    "first_name" : "Winter",
    "age" : 99
}

print(instructor_dict['first_name'])

# Tuples - Immutable List of Data

aTuple = ('China', 'Yosemite')

print(aTuple[0])

# Functions

def addNums(num1, num2):
    return num1 + num2

print(addNums(2,4))

print('=================\n')
print('Show this other line!')