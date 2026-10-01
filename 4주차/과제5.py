lst=[]
while True:
    n=int(input())
    if n == 0:
        break
    lst.append(n)

for i in range(1, len(lst),2):
    print(lst[i], end=" ")
