s = input()

d = {"Upper":0, "Lower":0}

for char in s:
    if char.isupper():
        d["Upper"] += 1
    elif char.islower():
        d["Lower"] += 1
    else:
        pass

print("UPPER CASE",d["Upper"])
print("LOWER CASE",d["Lower"])
