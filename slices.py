import time

word = input("Enter any word: ")

points = [".", "..", "..."]

for p in points:
    print(f"Wait{p}")
    time.sleep(0.5)


print(f"The first 3 letters of your word {word[0:3]}")

time.sleep(1)

print(f"The last 3 letters of your word {word[-3:]}")

time.sleep(1)

print(f"The whole word is the opposite {word[::-1]}")
    