'''
Created on 2011-4-23

@author: Administrator
'''
import os
import time
source = [r'E:\test\source\foo.txt',r'E:\test\source\bar']

#target_dir = 'E:\\test\\target\\'
target_dir = r'E:\test\target' + os.sep

today = target_dir + time.strftime("%Y%m%d")

now = time.strftime("%H%M%S")

if not os.path.exists(today):
    os.mkdir(today)
    print 'Successfully created dir',today
#target = target_dir + time.strftime("%Y%m%d%H%M%S") + '.zip'
target = today + os.sep + now + ".zip"

zip_command = "zip -qr '%s' %s" % (target,' '.join(source))

print zip_command



if os.system(zip_command) == 0:
    print 'successful back up to',target
else:
    print 'backpu failed'
    

