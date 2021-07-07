#try -> try
#catch -> except

try:
    #print(a)
    a=int(input("Enter age: "))
    print(a)
except NameError:
    print('Variable is not declared')
except:
    print('Other errors')
else:
    print("Else executes when there is no error")