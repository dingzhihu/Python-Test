'''
Created on 2011-4-28

@author: Administrator
'''
'''An address book.
'''
import sys
import cPickle as p

class Record:
    def __init__(self,name,tel):
        self.name = name
        self.tel = tel
    def __str__(self):
        return 'name:%s,tel:%s' % (self.name,self.tel)
    
def add(list,record):
    r = Record(record[0],record[1])
    list.append(r)
    f = file('address.txt','a')
    p.dump(list, f)
    f.close()
def query(name):
    f = file('address.txt')
    l = p.load(f)
    f.close()
    for item in l:
        if item.name == name:
            print 'name:%s,tel:%s' % (item.name,item.tel)
            
address = []
if len(sys.argv) == 1:
    print 'no argvs'
    r1 = Record('dd','123')
    r2 = Record('ff','333')
    r3 = Record('dd','666')
    address.append(r1)
    address.append(r2)
    address.append(r3)
    f = file('address.txt','w')
    p.dump(address,f)
    f.close()
    sys.exit()
else:
    if sys.argv[1] == 'add':
        add(address,sys.argv[2:])
    elif sys.argv[1] == 'query':
        query(sys.argv[2])
    else:
        print 'wrong para'
