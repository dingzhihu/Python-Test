'''
Created on 2011-4-26

@author: Administrator
'''
class SchoolMember:
    '''Represents any school member.'''
    def __init__(self,name,age):
        self.name = name
        self.age = age
        print '(Initialized School member %s)' % self.name
    def tel(self):
        '''Tell my details.'''
        print 'Name:%s,Age:%s' % (self.name,self.age)
        
class Teacher(SchoolMember):
    '''Repreents a teacher.'''
    def __init__(self,name,age,salary):
        SchoolMember.__init__(self, name, age);
        self.salary = salary
        print '(Initialized teacher %s)' % self.name
    def tel(self):
        SchoolMember.tel(self)
        print 'Salary %d' % self.salary
class Student(SchoolMember):
    '''Represents a student.'''
    def __init__(self, name, age, marks):
        SchoolMember.__init__(self, name, age)
        self.marks = marks
        print '(Initialized Student: %s)' % self.name

    def tel(self):
        SchoolMember.tel(self)
        print 'Marks: "%d"' % self.marks

t = Teacher('dd','25',5000000)
s = Student('foo','21',99)
print
m = [t,s]
for mem in m:
    mem.tel()
        
    