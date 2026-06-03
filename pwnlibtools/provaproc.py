import os 
import sys


print(os.getgid())
print(os.listdir('./'))
#GET ROOT USERS 
'''
def get_root_users()
for groupid in os.getgrouplist('root', 1):
    print(groupid)
'''
#print()
#print()
#print()