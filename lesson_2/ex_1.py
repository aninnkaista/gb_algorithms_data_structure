while True:
    # operation sign input
    inp_operation = input('Please type in math operator: ').strip()

    # validating input
    if inp_operation not in ('0', '+', '-', '*', '/'):
        print('The sign you entered is out of scope, try again')
        continue
    # checking if 0 then exit
    elif inp_operation == '0':
        print('Exiting')
        break
    # numbers input
    a, b = input('Now type in two numbers: ').strip().split()
    # to check if division by 0
    if float(b) == 0 and inp_operation == '/':
        print('Division by zero')
    # evaluating input and printing the result
    else:
        print(f'The result is {eval(" ".join((a, inp_operation, b)))}')