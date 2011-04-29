'''
Created on 2011-4-27

@author: Administrator
'''
import time

try:
    path = r'E:\test\poem.txt'
    f = file(path)
    while True: # our usual file-reading idiom
        line = f.readline()
        if len(line) == 0:
            break
        time.sleep(2)
        print line,
finally:
    f.close()
    print 'Cleaning up...closed the file'
