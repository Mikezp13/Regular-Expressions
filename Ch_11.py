# import re
#library regular expressions
# hand=open('mbox.txt')

# for line in hand:
#     line=line.rstrip()
#     if re.search('From:',line):
#         print(line)

# import re
# x='My 2 favorite numbers are 19 and 42'
# y=re.findall('[0-9+]+',x)
# print(y)
#
# y=re.findall('[AEIOU]+',x)
# print(y)
#
# import re
# x='From: Using the : character'
# y=re.findall('^F.+:',x)
# print(y)

# import re
# x='From: Using the : character'
# y=re.findall('^F.+?:',x)
# print(y)

import re
hand=open('mbox.txt')
numlist=list()
for line in hand:
    line=line.rstrip()
    stuff=re.findall('X-DSPAM-Confidence: ([0-9.]+)',line)
    if len(stuff)!=1: continue
    num=float(stuff[0])
    numlist.append(num)
print('Maximum: ',max(numlist))

