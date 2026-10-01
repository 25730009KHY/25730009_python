lst=[]
while True:
    n=int(input())
    if n == 0:
        break
    lst.append(n)

for i in range(len(lst)-1, -1, -1):
    print(lst[i])
