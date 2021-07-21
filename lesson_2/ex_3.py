inp_number = input('Please enter your number: ').strip()
opp_number = inp_number[::-1]
print('Reverse number is', opp_number)


# recursion
def get_reverse(inp_number: str) -> str:
    """Gets input number as a string and returns reverse number as a string as well"""
    if len(inp_number) == 1:
        return inp_number
    else:
        return inp_number[-1] + get_reverse(inp_number[:-1])


print('Reverse number from recursion is', get_reverse(inp_number))

