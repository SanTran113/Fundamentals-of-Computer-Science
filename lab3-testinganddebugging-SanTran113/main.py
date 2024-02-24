# Name: San Tran
# Date: 10/ 3 / 22
# Github: SanTran113

import functions

# The following code is an example of how you might test an expression using
#   print statements. Though this may seem irrelevant to your task, remember
#   that function calls are themselves expressions.

# A "Helper" print statement
print("Testing the function call addValues(1, 2)")

# A print statement showing the expected value
print("Expected Value: 3")

# A "Helper print statement"
print("Actual Value:")

# A print statement showing the tested value
print(functions.addValues(1, 2))

# You may write your function tests following this comment.

print(f"Expected Value for sqaure root: {functions.getSquareRoot(16)}")
print("Actual Value: 4")

print(f"Expected Value for tempature: {functions.convertToCelsius(32)}")
print("Actual Value: 0.0")

print("Expected Value:", functions.capitalizeCharacter("Calpoly!", 4))
print("Actual Value: CalPoly!")