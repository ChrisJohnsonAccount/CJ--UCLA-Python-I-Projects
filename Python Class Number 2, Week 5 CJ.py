
#prompt and open file
name = input("Enter file:")
nm = open(name)

#build dictionary of emails + frequency
freqlog = dict()

for line in nm:
    line = line.rstrip()
    if line.startswith("From "):
        row = line.split()
        address = row[1]
        if address not in freqlog:
            freqlog[address] = 1
        else:
            freqlog[address] = freqlog[address] + 1
    else:
        continue

#pull out highest frequency email
bigcount = None
bigword = None
for word,count in freqlog.items():
    if bigcount is None or count > bigcount:
        bigword=word
        bigcount=count

#find email


# print result- address + count
print(bigword, bigcount)
