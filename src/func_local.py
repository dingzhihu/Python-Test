'''
Created on 2011-4-22

@author: Administrator
'''
def func(x):
    print 'x is',x
    x = 30
    print 'x has changed to',x
    
def func2():
    global x
    print 'x is',x
    x = 5

def func3(message,times = 3):
    print message * times 

def func4(a,b = 5,c = 6):
    print 'a is',a,'and b is',b,'and c is',c
    
def func5():
    pass

def max(x,y):
    if x > y:
        return x
    else:
        return y
def max2(x,y):
    '''Prints the max of the two members.
    
    The two values must be integers.'''
    x = int(x)
    y = int(y)
    if x > y:
        return x
    else:
        return y

x = 55
func(x)
print 'x is still',x
func2()
print 'x has changed to',x
#func3("go away")
#func4(c = 3,a = 6)
print func5()
print max(1,5)
print max2(5,6)
print max2.__doc__
