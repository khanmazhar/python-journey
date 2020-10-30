# abc = 'With three words'
# stuff = abc.split()
# print(stuff)
#    print(w)

# abc = 'with;three;words'
# stuff = abc.split(';')
#    print(w)
#


# line = 'From mazharkhan@lums.edu.pk Sat jun 2022'
# a = line.find('@')
# b = line.find(' ', a)
# print(line[a+1:b])

# a = line.split()
# b = a[1]
# c = b.split('@')
# d = c[1]
# print(d)
# fname = input('Enter the file name: ')
# fhand = open(fname)
# lst = list()
# for line in fhand:
#    line = line.strip()
#    line1 = line.split()
#    for word in line1:
#        if lst.__contains__(word):
#            continue
#        else:
#            lst.append(word)
# lst.sort()
# print(lst)
count = 0
fname = input('Enter file name: ')
fh = open(fname)
for line in fh:
    line = line.rstrip()
    wds = line.split()
    if len(wds) < 1 or wds[0] != 'From':
        continue
    count += 1
    print(wds[1])
print('There were', count, 'lines in the file with From as the first word')
