s = input()

numbers = 0
letters = 0

for char in s:
    if char.isalpha():
        letters += 1
    elif char.isnumeric():
        numbers += 1

print(f"LETTERS {letters}")
print(f"NUMBERS {numbers}")
