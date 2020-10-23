#first_name = input('Enter you first name: ')
#last_name = input('Enter your last name: ')

#initials = first_name[0:len(first_name) - 1:2] + '\n' + last_name[0:1:1]

#print('Your initials are', initials)

#length_of_str_1 = len(input('Enter first string: '))
#length_of_str_2 = len(input('Enter second string: '))
#total_len = length_of_str_1 + length_of_str_2
#print('Total length:', total_len)

# roll number converter

#roll_num = input('Enter you roll number: ')
# official_roll_num = '20' + roll_num[0:2] + \
#    '-' + roll_num[2:4] + '-' + roll_num[5:]
# print(official_roll_num)

string = input("Enter a string: ")
#reversed_str = string[::-2]
# print(reversed_str)
#length = len(string)
#reversed_str = []
# while length > 0:
#    reversed_str += string[length-1]
#    length -= 1
#joined = ''
# print(joined.join(reversed_str))

reversed_str = ''.join(reversed(string))
print(reversed_str)
