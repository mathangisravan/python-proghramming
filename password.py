import random 
lower_case = "abcdefghijklmnopqrstuvwxyz"
upper_case = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
numbers = "0123456789"
symbols = "!@#$%^&*()_+:?/" 
use_for = lower_case +upper_case + numbers + symbols
max_length = 8
password = "".join(random.sample(use_for,max_length))
print("Your generated password is ",password)