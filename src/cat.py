'''
Created on 2011-4-27

@author: Administrator
'''
import sys
def readfile(name):
    '''print a file to the standard output.'''
    f = file(name)
    while True:
        line = f.readline()
        if len(line) == 0:
            break
        print line ,
    f.close()

#scripts start from here
if len(sys.argv) < 2:
    print 'no action specified'
    sys.exit()

if sys.argv[1].startswith('--'):
    option = sys.argv[1][2:]
    if option == 'version':
        print 'Version 2'
    elif option == 'help':
        print 'help'
    else:
        print 'unknow'
    sys.exit()
else:
    for filename in sys.argv[1:]:
        readfile(filename)
    

