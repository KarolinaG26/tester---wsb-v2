import os
import datetime
import time
import shutil

os.chdir('C:\\file\\tester-wsb')
print(os.getcwd())

with open ("C://file//tester-wsb//my_file.txt",'r')as f:
    lines = f.read()

for i in lines:
    print(i)






