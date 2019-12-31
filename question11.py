import pdb

numbers = [number for number in input().split(',')]
values = []

for number in numbers:
    tmp = int(number,2)
    if tmp%5 == 0:
        values.append(number)

print(','.join(values))
