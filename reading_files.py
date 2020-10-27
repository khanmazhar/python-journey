#fhand = open('Readme.txt')
#count = 0
# for line in fhand:
#    line = line.rstrip()
#    count += 1
#    print(line)
#print('Count:', count)

#fhand = open('text.txt')
# contents = fhand.read()
# print(len(contents))
# print(contents[:40])

# for line in fhand:
#    line = line.rstrip()
#    if not 'Khan' in line:
#        continue
#    print(line)

file_name = input('Enter file name: ')
try:
    fhand = open(file_name)
except:
    print('Could not open the file:', file_name)
    quit()


for line in fhand:
    line = line.upper().rstrip()
    print(line)
