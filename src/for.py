'''
Created on 2011-4-22

@author: Administrator
'''
def sayHello():
    print 'hello world'

def printMax(a, b):
    if(a>b):
        print a,'is larger than',b
    elif a<b:
        print a,'is smaller than',b
    else:
        print a,'is equal to',b
        
for i in range(1, 20, 3):
    if i == 10:
        break
    if i == 7:
        continue
    print i
else:
    print 'loop ends'
sayHello()
printMax(1,2)
printMax(2,1)
printMax(1,1)
