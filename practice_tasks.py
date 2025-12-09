# ------------DAY -1 ----------------
# Task -1

# name = input("Enter your name: ")
# age = int(input("Enter your age: "))

# print(f"Hello {name}, you will be {age+10} years after 10 years")

# Task -2

# marks = int(input("Enter your score out of 100: "))

# if marks >= 90:
#     print("You got a A")
# elif marks >= 75:
#     print("You got a B")
# elif marks >= 60:
#     print("You got a C")
# else:
#     print("Ops! Fail")

# Task- 3

# for num in range(1, 51):
#     if num % 3 == 0 and num % 5 == 0:
#         print(num)

# ------------DAY-2 ------------------------------
# Task -1 (FizzBuzz)--------------------------------------------------------

# for i in range(1, 101):
#     if i % 3 == 0 and i % 5 == 0:
#         print("FizzBuzz")
#     elif i % 3 == 0:
#         print("Fizz")
#     elif i % 5 == 0:
#         print("Buzz")
#     else:
#         print(i)

# Task-2 (Password Strength Checker)------------------------------------------------------

# password = input("Provide your password: ")

# has_number = False
# has_upper = False
# has_lower = False

# for char in password:
#     if char.isdigit():
#         has_number = True
#     if char.isupper():
#         has_upper = True
#     if char.islower():
#         has_lower = True

# if len(password) >= 8 and has_number and has_upper and has_lower:
#     print("Strong")
# else:
#     print("weak!, Try again")


# Task-3 (Reverse a string manually)---------------------------------------------------------

# word = input("Enter word to reverse: ")

# new_word = ""

# for char in word:
#     new_word = char + new_word
# print(new_word)

# Task- 4 (Count vowels in a sentence)-----------------------------------------

word = input("Enter your scetence: ").lower()
count = 0

for char in word:
    if char in ("a", "e", "i", "o", "u"):
        count += 1

print(f"The final count is : {count}")
