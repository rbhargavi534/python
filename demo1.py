import os

path=os.getcwd()
print(path)

path+='\\demo1.py'
print(path)

(dirname,filename)=os.path.split(path)
print(dirname)
print(filename)