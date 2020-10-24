#astr = input('Input an integer: ')
# try:
#    istr = int(astr)
#    print('You entered ', istr)
# except:
#    print('You entered an invalid input.')

# without using try except

#hours = float(input('Enter hours: '))
#hourly_rate = float(input('Enter hourly rate: '))
# if hours > 40:
#    pay = 40 * hourly_rate
#    hours -= 40
#    pay += hours * 1.5 * hourly_rate
# else:
#    pay = hours * hourly_rate

#print('Pay:', pay)

# using try except
hours = input('Enter hours: ')
hourly_rate = input('Enter hourly rate: ')
hrly_rate_abv_40 = 1.5
try:
    float_hrs = float(hours)
    float_hrly_rate = float(hourly_rate)
    if float_hrs > 40:
        pay = 40 * float_hrly_rate
        float_hrs -= 40
        pay += float_hrs * hrly_rate_abv_40 * float_hrly_rate
    else:
        pay = float_hrs * float_hrly_rate
    print('Pay:', pay)
except:
    print('Invalid input. Enter a numeric value.')
