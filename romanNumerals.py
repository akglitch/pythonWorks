input = int(input(f'Enter a number from one to ten \n >>> '))
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
roman_nums = ['I', 'II', 'III', 'IV', 'V', 'VI', 'VII', 'VIII', 'IX', 'X']
if (input > 10 or input < 1):
    print('Error')
else:
    print(f"the roman numeral for {input} is {roman_nums[nums.index(input)]}")