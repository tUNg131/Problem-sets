lines = []

while True:
    str = input().upper()
    if str:
        lines.append(str)
    else: break

print('\n'.join(lines))
