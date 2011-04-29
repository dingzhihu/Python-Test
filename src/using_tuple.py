'''
Created on 2011-4-22

@author: Administrator
'''
zoo = ('tiger', 'lion')
print 'animals number in zoo is:', len(zoo)
new_zoo = ('monkey', 'elephent', zoo)
print 'number of animals in the new zoo', len(new_zoo)
print 'animals in the new zoo are:', new_zoo
print 'last animals brought from the old zoo are:', new_zoo[2][1]
singleton = (2,)
print 'singleton len is', len(singleton)
age = 22
name = 'dd'
print '%s is %d years old' % (name, age)
print 'my name is %s' % name
