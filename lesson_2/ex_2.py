digits = map(int, input('Enter your number: ').strip())
even = 0
odd = 0
for digit in digits:
    if digit % 2 == 0:
        even += 1
    else:
        odd += 1
if odd == 1 and even != 1:
    print(f'Your number has {even} even digits and {odd} odd digit')
elif odd == 1 and even == 1:
    print(f'Your number has {even} even digit and {odd} odd digit')
elif even == 1:
    print(f'Your number has {even} even digit and {odd} odd digits')
else:
    print(f'Your number has {even} even digits and {odd} odd digits')