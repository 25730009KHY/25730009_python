def get_area(radius):
    area= 3.14*radius**2
    return area


result=get_area(3)
print("지름이 3인 원의 면적=", result)


print("\n","-"*45)

for i in range(6,0,-1):
    for j in range(i):
        print("*",end="")
    print()


for i in range(1,11):
    if i % 3==0:
        continue   #3의 배수를 제외하고 출력, 3일때 continue를 만나면 밑에는 출력 안되고 위로 다시 올라가서 4부터 다시 시
    else:
        print(i,end=" ")

print("\n","-"*45)

def add(a,b):
    return a+b
c=30
d=50
print(add(10,20))
print(add(c,d))


print("\n","-"*45)

def set_radius(radius):
    radius=100
    return radius

r=20
r=set_radius(r)
print(r)
