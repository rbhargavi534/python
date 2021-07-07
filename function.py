def abc():
    print('hello')

abc()

def show(a,b):
    print('a=',a,' b=',b)

show(1,2)
show(b=1,a=2)

def add(*args):
    sum=0
    for i in args:
        sum+=i
    return sum

print(add(1,2))
print(add(1,2,6,7,9))
print(add(1,2,3,4))
print(add(1,2,7))

# key, value -> dict
def myf(**kwargs):
    print(kwargs)
    print(kwargs["eid"],kwargs["ename"])
    for k,v in kwargs.items():
        print(k,v)

myf(eid=101,ename="bhargavi")

def sum(a,b,c=0):
    print(a+b+c)

sum(1,2)
sum(2,3,5)

def docdemo():
    """
    This is doc string
    """
    txt='''Text
    in multiple lines'''
    print(txt)

docdemo()
print(docdemo.__doc__)