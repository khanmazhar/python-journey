x = input('Enter a number.')
y = input('Enter another number.')

try:
    x_num = float(x)
    y_num = float(y)
except:
    print('Invalid Input! Try again...')
    quit()

if x_num % 2 == 1 and y_num % 2 == 1:
    print('Product of x and y is', x_num * y_num)

if y_num % 11 == 0 and y_num % 13 != 0:
    if x_num % 11 != 0 and x_num % 13 == 0:
        print('Vice versa!')
    else:
        print('False Alarm :(')

if x_num >= 0 and y_num >= 0 or x_num <= 0 and y_num <= 0:
    print('Product would be positive.')
else:
    print('Product would be negative.')
