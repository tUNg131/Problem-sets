# s = input()
#
# numbers = 0
# letters = 0
#
# for char in s:
#     if char.isalpha():
#         letters += 1
#     elif char.isnumeric():
#         numbers += 1
#
# print(f"LETTERS {letters}")
# print(f"NUMBERS {numbers}")

s = input()

d = {"Numbers":0, "Letters":0}

for char in s:
    if char.isalpha():
        d["Letters"] += 1
    elif char.isdigit():
        d["Numbers"] += 1
    else:
        pass

print("LETTERS",d["Letters"])
print("NUMBERS",d["Numbers"])
