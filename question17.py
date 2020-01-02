
balance = 0

while True:
    s = input()
    if s:
        message = [word for word in s.split() if s]
        if message[0] == "D":
            balance += int(message[1])
        elif message[0] == "W":
            balance -= int(message[1])
    else:
        break

print(balance)
