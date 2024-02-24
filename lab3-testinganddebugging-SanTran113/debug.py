# Name: San Tran
# Date: 10/ 3 / 22
# Github: SanTran113

this_name_is_acceptable = 1
this_name_isnt= 2
is_this_a_good_name = 3

six = this_name_is_acceptable + this_name_isnt + is_this_a_good_name
ten = 10
thousand = 1000

hundred = thousand / ten

print("hello world")

is_this_line_indented = "Yes, wrongly."
what_about_this_line = "Yes, wrongly again."

def hi():

    print("Hello world! Also, this line may be indented wrong.")

v = "<- Change this variable's name to something else!"

hi()

def multiplication(x: int, y: int) -> int:
    return x * y

def division(x: float, y: float) -> float:
  return x / y

print("5 * 5 should evaluate to 25, right?")
print("Lets see:")
print(multiplication(5, 5))

print("6.0 / 3.0 should evaluate to 2.0, right?")
print("Lets see:", division(6.0, 3.0))
