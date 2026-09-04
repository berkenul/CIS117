# This is my first Python programming assignment
# Author: Berk Enul
# Date: 08/27/2026

name = input("What is your name? ")
print("Hello,", name)

my_id = 8912314

print(f"{my_id:08d}")
print(f"{my_id:.2f}")
print(f"{my_id:b}")
print(f"{my_id:#x}")

first = my_id // 1000000
last = my_id % 10

print(f"First digit: {first}")
print(f"Last digit: {last}")
print(f"First + last = {first + last}")