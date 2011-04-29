'''
Created on 2011-4-22

@author: Administrator
'''
contact = {'dd' : '15855132832',
           'ff' : 'bj'
           }
print 'dd\'s addr is %s' % contact['dd']
contact['ding'] = '601859657'
del contact['dd']
print "there are %d items in contact" % len(contact)
for name,tel in contact.items():
    print "Contact %s at %s" % (name,tel)
    
if 'ding' in contact:
    print True
list = ['dd','gaga']
str = 'i am a string'
print list[-3:-1]
print str[0:-2]
tuple = ('a','b')
print tuple
print str.startswith('i ')
print 'i' in str
print str.find('  ')
print '*'.join(list)