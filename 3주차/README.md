# 25730009_python

**3주차_python

[파이썬 예제 0917.py](https://github.com/user-attachments/files/32315190/0917.py)
def get_area(radius):
    area= 3.14*radius**2
    return area


result=get_area(3)
print("지름이 3인 원의 면적=", result)


print("\n","-"*45)

for i in range(1,5):
    for j in range(1,5):
        print("*",end="")
    print()
