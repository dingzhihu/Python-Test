'''
Created on 2011-4-24

@author: Administrator
'''
class Person:
    '''Represents a person.'''
    _v = 1
    _v2 = 2
    population = 0
    def __init__(self,name):
        '''Initializes a person's data.'''
        self.name = name
        print '(Initializing %s)' % self.name
        Person.population += 1
    def __del__(self):
        '''I'm dying.'''
        print 'deleting person %s' % self.name
        Person.population -= 1
        if Person.population == 0:
            print 'i am the last person'
        else:
            print 'there are still %d person left' % Person.population
    def sayHi(self):
        '''Greeting by the person.'''
        print 'hi,my name is %s' % self.name
    def howMany(self):
        '''Prints the current population.'''
        if Person.population == 1:
            print 'i am the only person left'
        else:
            print 'there are still %d persons left' % Person.population
        
print Person.__init__.__doc__    
print Person._v
print Person._v2    