def add(a,b=20):
    return a+b

print(add(10))

for i in range(10):
    print(i,end=" ")

for _ in range(10):
    print()



def printPattern(rows=5,cols=5,char="*"):
    for _ in range(rows):
        for _ in range(cols):
            print(char, end=" ")
        print()

printPattern(3,10,"%")


print("\n","-"*30)

for i in range(1,6):
    for j in range(i):
        print("*",end=" ")
    print(" ")

for i in range(5,0,-1):
    for j in range(i):
        print("@", end=" ")
    print(" ")
