first_letter_of_fav_color = input(
    'Enter the first letter of your favorite color: \n')
first_letter_of_birth_month = input(
    'Enter the first letter of the month your were born in: \n')
last_digit_of_age = input('Enter the last digit of your age: \n')
last_digit_of_mobile_number = input(
    'Enter the last digit of your mobile number: \n')

final = first_letter_of_fav_color + first_letter_of_birth_month + \
    last_digit_of_age + last_digit_of_mobile_number
print('Your 4 character password is', final)
