'''
Created on 2011-4-22

@author: Administrator
'''
mylist = ['book','pen','note']
print 'now,i have',len(mylist),'items'
print 'they are:'
for i in mylist:
    print i
print 'i also have to buy a eraser'
eraser = 'eraser'
mylist.append(eraser)
print 'now my list are:',mylist
print 'i have to sort mylist'
mylist.sort()
print 'after sorted,they are:'
print mylist
olditem = mylist[0]
print 'i bought',olditem
del mylist[0]
print 'now,the list is',mylist

