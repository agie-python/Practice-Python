base=12
hieght= 2
area= (base*hieght)/2
print(area)

#returning a value
def area_triangle(base, hieght):
    return base*hieght/2

area_a = area_triangle(5,4)
area_b = area_triangle(7,3)
sum = area_a + area_b
print("The sum of both aras is: " + str(sum))

def get_seconds(hours, minutes, seconds):
  return 3600*hours + 60*minutes + seconds

amount_a = get_seconds(2,30,0)
amount_b = get_seconds(0,45,15)
result = (amount_a + amount_b)
print(result)

#principles of code reuse.
name = "Kay"
number = len(name) * 9
print("Hello " + name + ". Your lucky number is " + str(number))

name = "Agnes"
number = len(name) * 9
print("Hello " + name + ". Your lucky number is " + str(number))

#how to summanrize to reuse the code...
def lucky_number(name): #function called luckyumber defines the calculation and prints it out
    number= len(name) *9
    print("Hello " + name + ". Your lucky number is " + str(number))
#calling the function twice.
#reusing a functio bycalling it with a different name.
lucky_number("Kay")
lucky_number("Agnes")


def month_days(month, days):
    print(month + "has " + str(days) + " days.")
month_days("june", 30)

def convert_distance(miles):
	return miles * 1.6  # approximately 1.6 km in 1 mile
km= convert_distance(55)
print("The distance in kilometers is " + str(km))

# This function compares two numbers and returns them
# in increasing order.
def order_numbers(number1, number2):
	if number2 > number1:
		return number1, number2
	else:
		return number2, number1

# 1) Fill in the blanks so the print statement displays the result
#    of the function call
smaller, bigger = order_numbers(100, 99)
print(smaller, bigger)

#comparing things
print("cat" == "dog")

#The is_positive function should return True if the number received is positive, otherwise it returns None. Can you fill in the gaps to make that happen?
def is_positive(number):
  if (number > 0):
     return True
  else:
      return None
print(is_positive(-5))

def is_postive(number):
 if number > 11:
   print(0)
 elif number != 10:
  print(1)
 elif number >= 20 or number < 12:
   print(2)
 else:
   print(3)
print(is_postive(10))

#If a filesystem has a block size of 4096 bytes, this means that a file comprised of only one byte will still use 4096 bytes of storage. A file made up of 4097 bytes will use 4096*2=8192 bytes of storage. Knowing this, can you fill in the gaps in the calculate_storage function below, which calculates the total number of bytes needed to store a file of a given size?
def calculate_storage(filesize):
    block_size = 4096
    # Use floor division to calculate how many blocks are fully occupied
    full_blocks =  filesize//4096
    # Use the modulo operator to check whether there's any remainder
    partial_block_remainder = filesize%4096
    # Depending on whether there's a remainder or not, return
    # the total number of bytes required to allocate enough blocks
    # to store your data.
    if partial_block_remainder > 0:
        return 4096*(full_blocks+1)
    return full_blocks*4096


def format_name(first_name, last_name):
    if first_name != " " and last_name != " ":
       string = ("Name: " + first_name + ", " + last_name)

    elif first_name = " " and last_name != " ":
      string = ("Name: " + last_name)

    return string
print(format_name("Ernest", "Hemingway"))