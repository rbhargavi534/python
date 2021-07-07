emp={"eid":101,"ename":"Deepak"}

print(emp)
print(type(emp))

print(emp["eid"],emp["ename"])

print(emp.get("eid"))
emp["ename"]="Ravi"

print(emp)

print("-"*10)

for key in emp:
    print(key)

print("-"*10)

for value in emp.values():
    print(value)

print("-"*10)

for key,value in emp.items():
    print(key,value)

print("-"*10)

if "ename" in emp:
    print("Present")
else:
    print("Not")

print("-"*10)
print(len(emp))

emp["sal"]=75000
print(emp)
print(len(emp))

del emp["sal"]
print(emp)
print(len(emp))

#del emp
#print(emp)#error

#emp.clear()
#print(emp)

emp2=emp.copy()
print(emp)
print(emp2)

emp3=dict(emp2)
print(emp3)

emp4=dict(eid=102,ename="Tarun")
print(emp4)