# strings------------------------------------------------
# course = "Python Programming"
# print(len(course))
# print(course[0])
# print(course[-1])
# print(course[0:3])
# print(course[0:])
# print(course[:3])
# print(course[:])

# formated strings - works as  a expression----------------------

# first = "Sumit"
# last = "Joshi"
# full = f"{first} {last}"
# print(full)

# strng methods--------------------------------------------

# course = "Python Programming"
# print(course.upper())
# print(course.lower())
# #etc...c

# Type Conversion-------------------------------------------

# x = input("x: ")
# y = int(x) + 1
# print(f"x: {x}, y:{y}")

# Conditional Statement--------------------------------------

# temperature = 23
# if temperature > 30:
#     print("It's warm")
#     print("Drink Water")
# elif temperature > 20:
#     print("It's nice")
# else:
#     print("It's cold")

# print("done")

# ternary operator----------------------------

# age = 17
# message = "Eligible" if age >= 18 else "Not Eligible"  # ternary operator
# print(message)

# Logial operators -- and ,or, not -----------------------------------------------

# high_income = False
# good_credit = True
# student = False

# if (high_income or good_credit) and not student:
#     print("eligible")
# else:
#     print("not eligible")


# Chaining comparison operator-----------------------------
# age should be between 18 and 65
# age = 17
# # if age >= 18 and age < 65:
# if 18 <= age < 65:  # chaining operator
#     print("Eligible")
# else:
#     print("not eligible")

# For loops-----------------------------------------

# type 1
# for num in range(3):
#     print("hello")
# type 2
# for nums in range(1, 4):
#     print("Hello", nums, nums * "@")
# type 3
# for nums in range(1, 10, 2):
#     print("Hello", nums, nums * "@")

# For Else------------------------------------------------
# sucessful = True
# for num in range(3):
#     print("attempted")
#     if sucessful:
#         print("successful")
#         break
# else:
#     print("attempted 3 times but failed")

# nested loops --------------------------------------------

# for x in range(5):
#     for y in range(4):
#         print(f"({x},{y})")

# Iterables - which itrates over iterable object like int, string,list------------------------------
# for i in range(5):
#     print(i)
# for x in "sumit":
#     print(x)
# for y in [1, 2, "egg", "radhe"]:
#     print(y)

# While Loops- will run until the condition is true-----------------------------------------------
# example-1
# num = 100
# while num > 0:
#     print(num)
#     num //= 2
# example -2
# command = ""
# while command.lower() != "quit":
#     command = input(">")
#     print("ECHO", command)

# Infinite Loop-----------------------------------------------------------------

# while True:
#     command = input(">")
#     print("ECHO", command)
#     if command.lower() == "quit":
#         break

# Exercise ---------------------------------------------------
# find even number
# count = 0
# for num in range(1, 10):
#     if num % 2 == 0:
#         count += 1
#         print(num)
# print(f"we have {count} even numbers ")

# functions --------------------------------------------

# def greet(first_name, last_name):
#     print(f"Hi {first_name} {last_name}")
#     print("welcome")


# greet("Sumit", "Joshi")

# functions types ------------------------------------------
# 1- function wich perform a task
# 2- return the value

# def greet(name):
#     return f"Hi {name}"


# message = greet("Sumit")
# print(message)


# keyword argummnets-------------------------------------

# def increment(number, by):
#     return number + by


# print(increment(3, 2))

# we can make the key argumnet optional

# def increment(number, by=1):
#     return number + by


# print(increment(2))

# args (argumnets)-----------------------------------------

def multiply(*numbers):
    total = 1
    for number in numbers:
        total *= number
    return total


print(multiply(1, 23, 4, 5))
