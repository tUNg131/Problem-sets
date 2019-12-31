import pdb

items =[int(x) for x in input().split(',')]
rowNum = items[0]
colNum = items[1]

values = [None] * rowNum

for i in range(rowNum):
    values[i] = [j*i for j in range(colNum)]

print(values)
