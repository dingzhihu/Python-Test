'''
Created on 2011-4-27

@author: Administrator
'''
import cPickle as p
class Dog:
    def __init__(self,name):
        self.name = name
    def bark(self):
        print '@@@@@@@@'

shoplistfile = r'E:\test\shoplist.txt'
dog = Dog('wangcai')
shoplist = ['apple','mango','parrot']
f = file(shoplistfile,'w')
#p.dump(shoplist,f)
p.dump(dog,f)
f.close()

f = file(shoplistfile)
storedlist = p.load(f)
f.close()
storedlist.bark()
print storedlist.name