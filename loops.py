# for i in [5, 4, 3, 2, 1]:
#    print(i)
# print('Blast')

#friends = ['Maira', 'Mohsin', 'Shah Zaib']
# for i in friends:
#    print('Hello', i)
# print('Welcome!')
'''
num_list = [56, 32, 2, 43, 65, 78, 12, 445, 5432, 4535, 435346, 7658, 242]
largest_so_far = 0
print('Before', largest_so_far)
for largest in num_list:
    if largest_so_far < largest:
        largest_so_far = largest
    print(largest_so_far, largest)
print('After: ', largest_so_far)
'''
'''
smallest = None
print("Before:", smallest)
for itervar in [3, 41, 12, 9, 74, 15]:
    if smallest is None or itervar < smallest:
        smallest = itervar

    print("Loop:", itervar, smallest)
print("Smallest:", smallest)
'''
'''
num_list = [56, 32, 2, 43, 65, 78, 12, 445, 5432, 4535, 435346, 7658, 242]
count = 0
print('Before', count)
for i in num_list:
    count += 1
    print(count, i)
print('After: ', count)
'''
'''
num_list = [56, 32, 2, 43]
count = 0
total = 0
print('Before: Sum:', total, ' Count:', count)
for i in num_list:
    count += 1
    total += i
    print(count, total, i)
print('Before:\nSum:', total, '\nCount:', count, '\nAverage:', total/count)
'''
'''
found = False
count = 0
for i in [1, 7, 5, 87, 3, 5]:
    count += 1
    if i == 3:
        found = True
        print(found, i)
        break
    print(found, i)
print('The', count, 'th element is 3')
'''
'''
smallest = None
print('Before')
for value in [1, 34, 63, 22, -1, 324, -2543, 2234]:
    if smallest is None:
        smallest = value
    elif value < smallest:
        smallest = value
    print(smallest, value)
print('After', smallest)
'''

total = 0.0
count = 0
while True:
    num = input('Enter a number: ')
    try:
        int_num = float(num)
        total += int_num
        count += 1
    except:
        if num == 'done' or num == 'Done':
            break
        else:
            print('Invalid entry')
print('Sum:', total)
print('Total entries:', count)
print('Average:', total/count)
