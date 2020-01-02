import math
position = [0,0]

while True:
    s = input()
    if not s:
        break
    instruction = s.split()
    if instruction[0] == "UP":
        position[1] += int(instruction[1])
    elif instruction[0] == "DOWN":
        position[1] -= int(instruction[1])
    elif instruction[0] == "LEFT":
        position[0] -= int(instruction[1])
    elif instruction[0] == "RIGHT":
        position[0] += int(instruction[1])
    else:
        pass

distance = math.sqrt(position[0]**2+position[1]**2)

print(int(distance))
