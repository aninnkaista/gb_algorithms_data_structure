n = int(input('Enter the length of number sequence: '))
c_seq = input('Enter a sequence: ').strip()
c_num = input('Enter a digit: ').strip()

c_count = 0
for i in range(n):
    if c_num == c_seq[i]:
        c_count += 1
print(f'Total count of {c_num} digit in a sequence is {c_count}')