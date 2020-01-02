people = []

while True:
    s = input()
    if not s:
        break
    person = tuple(s.split(","))
    people.append(person)

# people.sort(key= lambda x: (x[0],x[1],x[2]))
people.sort()
