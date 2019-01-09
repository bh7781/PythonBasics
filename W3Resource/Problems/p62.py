# Write a Python program to compute sum of digits of a given string
def sum_of_digits(str1):
    digit_sum = 0
    for n in str1:
        if n.isdigit() == True:
            z = int(n)
            digit_sum = digit_sum + z
    return digit_sum

str1 = input('Enter string: ')
print('Sum of digits: ', sum_of_digits(str1))