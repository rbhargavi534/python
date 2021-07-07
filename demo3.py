import os

mydir=os.getcwd()

for r,d,f in os.walk(mydir):
    for file in f:
        print('File:',file)
    for dir in d:
        print('Folder:',dir)

mylist=os.listdir()
print(mylist)
print(type(mylist))

textfiles=[]
for m in mylist:
    if m.endswith(".txt"):
        print(m)
        textfiles.append(m)

print(textfiles)