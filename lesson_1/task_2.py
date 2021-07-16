# function
def bitwise_operations(a, b):
    """Function performs bitwise operations on the given 2 numbers and
    prints results including short explanation, no return value"""
    # transfer them to bits
    bin_a, bin_b = bin(a), bin(b)
    # OR and print
    print(f'bitwise or of {a} and {b} is {a | b} and equals to per element OR of binary of them {bin_a} | {bin_b}',
          'which is then converted back to decimal')
    # AND and print transferring back to integer
    print(f'binary and of {a} and {b} is {a & b} and equals to per element AND of binary {bin_a} & {bin_b}',
          'which is then converted back to decimal')
    # XOR and print transferring back to integer
    print(f'bitwise xor of {a} and {b} is {a ^ b} and equals to per element XOR of binary {bin_a} ^ {bin_b}',
          'which is then converted back to decimal')
    # >> right shift of 5 by 2
    print(f'bit right shift by 2 of {a} is {a>>2} and equal to int division by 2**2, or shifting each element of',
          'the binary to the right filling new spaces with 0')
    # << left shift of 5 by 2
    print(f'bit left shift of {a} is {a<<2} and equal to multiplication by 2**2, or shifting each element of',
          'the binary to the left filling new spaces with 0')

if __name__ == '__main__':
    bitwise_operations(5,6)

