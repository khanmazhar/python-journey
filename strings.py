'''
fruit = 'banana'
index = 0
while index < len(fruit):
    letter = fruit[index]
    print(index, letter)
    index += 1

print(len(fruit))
'''
'''
fruit = 'banana'
index = 0
for letter in fruit:
    print(index, letter)
    index += 1
'''
'''
fruit = 'banana'
count_of_a = 0
count_other_than_a = 0
for letter in fruit:
    if letter == 'a':
        count_of_a += 1
    else:
        count_other_than_a += 1
print('Total number of A are', count_of_a)
print('Non A letters are', count_other_than_a)
'''
'''
fruit = 'banana'
if 'n' in fruit:
    print('Found it!')
'''
'''
fruit = 'aanana'
if fruit < 'banana':
    print('The word', fruit, 'comes before banana')
else:
    print('The word', fruit, 'comes after banana')
'''
'''
word = input('Input a word')
print(word.lower())
print(type(word))
print(dir(word))
'''
'''
word = 'banana'
pos = word.find('na')
print(pos)
aa = word.find('z')
print(aa)
'''
#Search and replace
'''
greet = 'Hello Mazhar'
print(greet)
new_greet = greet.replace('Mazhar', 'Khan')
print(new_greet)
'''
# strip
'''
greet = '    Hello World    '
print(greet.lstrip())
print(greet.rstrip())
print(greet.strip())
'''
# startwith funtion
'''
line = 'Hello world.. I\'m a noob.'
print(line.startswith('Hello'))
'''
#parsing and extracting
'''
data = 'From mazharkhan.24020465@lums.edu.pk Monday November'
start = data.find('@', 0)
print(start)
end = data.find(' ', start)
print(end)
address = data[start+1:end]
print(address)
'''

# Exercise
string = 'X-DSPAM-CONFIDENCE: 0.8475'
start = string.find('0')
print(start)
end = string.find('5', start) + 1
print(end)
num = float(string[start:end])
print(num)
print(type(num))
