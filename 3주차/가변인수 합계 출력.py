

a=[1,2,3]
b=(1,2,3)


def add (*numbers): #가변인수로 지정한건 뒤 ---,numbers
    sum=0
    for i in numbers:
        sum=sum+i
        return sum

print(add(10,20,30,40,50))


print("\n","-"*45)

def add(a):
    return a +10

print(add(10))

add2= lambda x:x+10
print(add2(10))

print("\n","="*45)

a=10

def add():
    global a #global을 붙이면 뒤에 같이 a=20을 못 씀. 밑으로 내려서 써줘야
    a=20
    print(a)

add()
print(a)


    
