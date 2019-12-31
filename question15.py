def add(a,n_digit):
    if n_digit == 0:
        return 0
    else:
        return add(a,n_digit-1) + int(a*n_digit)

print(add(input(),4))
