age=int(input("enter your age:"))

'''
if age>=18:
    print('eligible to vote')
else:
    print('not eligible for vote')


'''

if age<13:
    if age<5:
        print('infant')
    else:
        print('child')
elif age<20:
    print('teenzger')
elif age<60:
    print('adult')
else:
    print('senior citizen')


    
