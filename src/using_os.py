'''
Created on 2011-4-27

@author: Administrator
'''
class Foo:
    def __init__(self,name):
        self.name = name
    def __getitem__(self,key):
        return self.name

foo = Foo("dd")
print foo['d']
a = {'dd':1,'ff':"g"}
print a['dd']
b = [1,2,3]
c = [i*2 for i in b if i > 1]
print c
def repeat(n):
    return lambda s:s*n
twice = repeat(3)
print twice('dd')
print eval('2*3')
exec "print 'gg'"
mylist = ['a','b']
print repr(mylist)
print `mylist`
