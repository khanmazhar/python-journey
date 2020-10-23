#num = float(input('Enter a number to check if its even or odd'))
# if num % 2 == 0:
#    print('Even')
# else:
#    print('Odd')

#num = float(input('Enter your GPA: '))
#count = 0
# while num > 0:
#    count = count + 1
#    num -= 0.33
# if count == 1:
#    print("A+")

units = float(input('Enter units of electricity consumed: '))
total_bill = 0
if units > 250:
    total_bill += 50 * 0.50
    units -= 50
    total_bill += 100 * 0.75
    units -= 100
    total_bill += 100 * 1.20
    units -= 100
    total_bill += units * 1.50
elif units > 150:
    total_bill += 50 * 0.50
    units -= 50
    total_bill += 100 * 0.75
    units -= 50
    total_bill += units * 1.20
elif units > 100:
    total_bill += 50 * 0.50
    units -= 50
    total_bill += units * 0.75
elif units > 50:
    total_bill += 50 * 0.50
    units -= 50
    total_bill += units * 0.75
elif units < 50:
    total_bill += units * 0.50

print(total_bill)
