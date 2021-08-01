# to have a dictionary of all pair hexadecimal digit => decimal number
translator = {'1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6,
               '7': 7, '8': 8, '9': 9, 'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15}
# to enter numbers
first_number = list(input('Enter your first hexadecimal number: '))
second_number = list(input('Enter your second hexadecimal number: '))

# to translate those numbers to decimal by digits
def to_decimal(hex: list):
    """To translate entered list of hex digits to decimal number"""
    # to check if negative number
    if hex[0] == '-':
        mul = -1
        hex = hex[1:]
    else:
        mul = 1
    hex_digits = [translator[hex_dig] for hex_dig in hex[::-1]]
    return sum([n * (16 ** i) for i, n in enumerate(hex_digits)]) * mul


first_number_dec = to_decimal(first_number)
second_number_dec = to_decimal(second_number)

# to find sum and multiplication of decimals
sum_dec = first_number_dec + second_number_dec
mul_dec = first_number_dec * second_number_dec

# to translate multiplication to list of hexadecimal digits
def to_hex_dig(dec: int):
    """To translate decimal to the list of hexadecimal digits"""
    # to check if negative
    if dec < 0:
        mul = '-'
        dec *= -1
    else:
        mul = None
    output = []
    while True:
        rem = dec % 16
        output.append(tuple(translator.keys())[tuple(translator.values()).index(rem)])
        if dec < 16:
            break
        else:
            dec = (dec - rem) / 16
    if mul is not None:
        output.append(mul)
    return output[::-1]

# results
sum_hex = to_hex_dig(sum_dec)
mul_hex = to_hex_dig(mul_dec)
# to print out sum and multiplication as lists
print(f'{sum_hex = }')
print(f'{mul_hex = }')



