'''
9.4 Write a program to read through the mbox-short.txt and figure out who has
the sent the greatest number of mail messages. The program looks for 'From '
lines and takes the second word of those lines as the person who sent the mail.
The program creates a Python dictionary that maps the sender's mail address to a
count of the number of times they appear in the file. After the dictionary is
produced, the program reads through the dictionary using a maximum loop to find
the most prolific committer.
'''
name = input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)
senders1 = list()
senders = dict()
for line in handle:
    line = line.split()
    if len(line) < 3 or line[0] != 'From':
        continue
    senders1.append(line[1])

for sender in senders1:
    senders[sender] = senders.get(sender, 0) + 1

maximum = None
theone = None
for sender, count in senders.items():
    if maximum is None or count > maximum:
        maximum = count
        theone = sender

print(theone, maximum)
