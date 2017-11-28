#import re
import re

x= list()

#open file
handle = open("open file")

#find integers
for line in handle:
    line = line.rstrip()
    y = re.findall('[0-9]+' ,line)
    z = list(map(int, y))
    x.extend(z)

total = sum(x)
print(total)
