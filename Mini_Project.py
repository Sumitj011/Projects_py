# ------------Random Password Generator---------------
import random
import string

req = int(input("Hey!, How long do you need the password to be? "))

chars = string.ascii_letters+string.digits+string.punctuation

password = ""

for i in range(req):
    password += random.choice(chars)

print(password)
