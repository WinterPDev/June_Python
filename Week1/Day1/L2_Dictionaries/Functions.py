"""
function addNums(num1, num2 ) {
    return num1 + num2;
    }
"""

x = 3

# print(x)

def addNums(num1, num2):
    return num1 + num2

addNums(3, 5)
# result = addNums(3, 5)

# print(result)

# print(addNums(3,10))
# Add Default Values

def addNums2(num1=0, num2=0):
    return num1 + num2

print(addNums2())

