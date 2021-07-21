# to enter some positive integers and save them as a list of strings
cur_numbers = input('Enter positive integers to compare the sum of digits: ').strip().split()

# to create list of digits' sums
digits_sums = []
for num in cur_numbers:
    digits_sum = 0
    for dig in num:
        digits_sum += int(dig)
    digits_sums.append(digits_sum)

# to get maximum digits sums
max_dig_sum = max(digits_sums)
# corresponding numbers
corr_numbers = [cur_numbers[i] for i in range(len(digits_sums)) if digits_sums[i] == max_dig_sum]
# to print the result
print('Number(s) with the biggest sum of digits is(are)',
      *corr_numbers,
      f'and this sum is {max_dig_sum}')
