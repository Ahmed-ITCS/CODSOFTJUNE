import string
import random

n = input("Enter your password length: ")

password = "".join(random.choices(string.ascii_letters + string.digits, k=int(n)))
print("your password is '",password,"'")
