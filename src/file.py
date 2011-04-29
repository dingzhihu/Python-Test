'''
Created on 2011-4-26

@author: Administrator
'''
poem = '''\
i love u.
happy every day.
put on a smile.
'''
path = r'E:\test\poem.txt'

f = file('poem.txt','w')
f.write(poem)
f.close()

f = file('poem.txt')
while True:
    line = f.readline()
    if len(line) == 0:
        break
    print line ,
f.close()