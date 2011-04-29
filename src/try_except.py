'''
Created on 2011-4-27

@author: Administrator
'''
import sys
try:
    s = raw_input('enter sth:')
except EOFError:
    print '\n why did u do an eof on me ?'
    sys.exit()
except:
    print '\nsome error occurred'

print 'Done'  

class ShortInputException(Exception):
    def __init__(self,length,atlest):
        Exception.__init__(self)
        self.length = length
        self.atlest = atlest

try:
    s = raw_input('enter:')
    if len(s) < 3:
        raise ShortInputException(len(s),3)
except EOFError:
    print '\nWhy did you do an EOF on me?'
except ShortInputException,x:
    print 'len %s,atlest %s' % (x.length,x.atlest)
else:
    print 'No exception was raised.'       
