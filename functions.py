#big = max('Hello world')
#print('Big: ', big)
#small = min('Helloworld')
#print('Small ', small)
#highest = max(1, 2, 3, 4, 5, 6, 7)
#smallest = min(1, 2, 4, 5, 6, 7)
#print('Highest: ', highest)
#print('Smallest: ', smallest)

# def greet(lang):
#   if lang == 'es':
#        return 'Hola'
#    elif lang == 'fr':
#        return 'Bonjour'
#    else:
#        return 'Hello'


#user_input = input('Enter your language: ')
#print(greet(user_input), 'Sam')

hrs = input('Enter hours: ')
hrly_rate = input('Enter hourly rate: ')


def computePay(a, b):
    try:
        float_hrs = float(hrs)
        float_hrly_rate = float(hrly_rate)
        if float_hrs > 40:
            pay = 40 * float_hrly_rate
            float_hrs -= 40
            pay += float_hrs * 1.5 * float_hrly_rate
        else:
            pay = float_hrs * float_hrly_rate
        print('Pay: ', pay)
    except:
        print("Invalid entry.")


computePay(hrs, hrly_rate)
