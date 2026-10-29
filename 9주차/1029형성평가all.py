#1
s=input()
n = int(input())
for i in range(n):
    print(s)

#2
a, b = map(int, input().split())
print(sum(range(a, b +1)))

#3
n = int(input())
for i in range(3, n+1, 3):
    print(i)
#4
n = int(input())
for i in range(1, n+1):
    if n % i ==0:
        print(i)
#5
n = int(input())
result = 1
i = 1
while result < n:
    i +=1
    result *= i
print(result)

#6
count = 0
while True:
    n = int(input())
    if n == 0:
        break
    if n % 2 == 0:
        count += 1
print(count)

#7
while True:
    c = input()
    if c == "A":
        print("ADD")
    elif c == "B":
        print("BACK")
    elif c == "C":
        print("COPY")
    elif c == "D":
        print("DELETE")
    elif c == "E":
        print("EXIT")
        break
    else:
        print("NONE")
