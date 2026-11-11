#a=1
#print(type(a))

#b,c,d= 1,2,3
#print(type(b),type(c).type(d))

#tur]ple
#a= 1,2,3
#print(type(a))

#list
a= 1,2,3  #<-- turple
a= list(a)
print(type(a))

#list
a= set({1,2,3,3,2,1})    #중복값생략후출력
print(a)

#set(고유한 값을 갖는다, 순서가 없다)
#b=[1,2,2,2,3,1,2]       
#a = set(b)
#print(*a)

#len()개수반환 
#fruits = {"apple", "banana", "grape"}
#size = len(fruits)
#print(size)

#in 포함되는지 
fruits = {"apple", "banana", "grape"}
if "apple" in fruits:
    print("apple 있습니다.")
else:
    pritn("없습니다")

string = input()
fruits = {"apple", "banana", "grape"}
if string in fruits:
    print(string,"있습니다.")
else:
    pritn("없습니다")


#출력(저장된 순서가 없다)
#fruits = {"apple", "banana", "grape"}
#print(fruits)

#출력(출력시 정렬해서 출력할 수는 있다)
fruits = {"apple", "banana", "grape"}
for x in sorted(fruits):      #fruits,뒤에 reverse=True 추가 하면 내림차순 정리
    print(x, end=" ")
print()

# 문자열 슬라이싱
s = 'Monty Python'
# 슬라이싱 [start:end:step]
# Python
print(s[6:12])
print(s[6:])

#Monty
print(s[0:5])
print(s[:5])
print(s[5])  # XXXX

# 거꾸로 출력
print(s[::-1])

# 문자자료형 + 문자자료형 (연결)
print(s[:5] + s[6:])

# in 문자열안에 문자 혹은 문자열을 포함하고 있는지 체크
# 영어는 대소문자를 구분한다.
print("a" in "Abc") # False
print("a" in "abc") # True
print("a" not in "Abc") # True

# 숫자 -> 문자로 형변환 str()
name = "홍길동"
age = 21
print("제 이름은 " + name + "입니다.")
print("제 나이는 " + str(age) + "입니다.")

# print % 서식문자 ( %d 정수, %f 실수, %c 문자, %s 문자열)
print("제 이름은 %s 입니다"%name)
print("제 이름은 %s입니다. 저는 %s살입니다." %(name, age))

# f-string 활용해서 문자열 출력
print(f"제 이름은 {name} 입니다. 저는 {age}살 입니다.")

# 딕셔너리
num ={"one":1,"two":2,"three":3}
print(num["one"]) # key 를 사용해서 value 출력
#print(num["four"]) # key error

# get() 메서드는 특정 키에 해당하는 값을 가져올때 사용
# 존재하지 않는 키를 조회해도 오류가 발생하지 않는다.
print(num.get("four", "해당키가 없습니다."))

# get() 개수를 카운트 할때 사용 가능
fruits = ["apple", "banana", "apple", "melon", "banana", "apple"]
count = {}  # set을 만들려면 b = set()

for fruit in fruits:
    count[fruit] = count.get(fruit, 0) + 1

# 문자열 슬라이싱
s = 'Monty Python'
# 슬라이싱 [start:end:step]
# Python
print(s[6:12])
print(s[6:])

#Monty
print(s[0:5])
print(s[:5])
print(s[5])  # XXXX

# 거꾸로 출력
print(s[::-1])

# 문자자료형 + 문자자료형 (연결)
print(s[:5] + s[6:])

# in 문자열안에 문자 혹은 문자열을 포함하고 있는지 체크
# 영어는 대소문자를 구분한다.
print("a" in "Abc") # False
print("a" in "abc") # True
print("a" not in "Abc") # True

# 숫자 -> 문자로 형변환 str()
name = "홍길동"
age = 21
print("제 이름은 " + name + "입니다.")
print("제 나이는 " + str(age) + "입니다.")

# print % 서식문자 ( %d 정수, %f 실수, %c 문자, %s 문자열)
print("제 이름은 %s 입니다"%name)
print("제 이름은 %s입니다. 저는 %s살입니다." %(name, age))

# f-string 활용해서 문자열 출력
print(f"제 이름은 {name} 입니다. 저는 {age}살 입니다.")

# 딕셔너리
num ={"one":1,"two":2,"three":3}
print(num["one"]) # key 를 사용해서 value 출력
#print(num["four"]) # key error

# get() 메서드는 특정 키에 해당하는 값을 가져올때 사용
# 존재하지 않는 키를 조회해도 오류가 발생하지 않는다.
print(num.get("four", "해당키가 없습니다."))

# get() 개수를 카운트 할때 사용 가능
fruits = ["apple", "banana", "apple", "melon", "banana", "apple"]
count = {}  # set을 만들려면 b = set()

for fruit in fruits:
    count[fruit] = count.get(fruit, 0) + 1
# 문자열 슬라이싱
s = 'Monty Python'
# 슬라이싱 [start:end:step]
# Python
print(s[6:12])
print(s[6:])

#Monty
print(s[0:5])
print(s[:5])
print(s[5])  # XXXX

# 거꾸로 출력
print(s[::-1])

# 문자자료형 + 문자자료형 (연결)
print(s[:5] + s[6:])

# in 문자열안에 문자 혹은 문자열을 포함하고 있는지 체크
# 영어는 대소문자를 구분한다.
print("a" in "Abc") # False
print("a" in "abc") # True
print("a" not in "Abc") # True

# 숫자 -> 문자로 형변환 str()
name = "홍길동"
age = 21
print("제 이름은 " + name + "입니다.")
print("제 나이는 " + str(age) + "입니다.")

# print % 서식문자 ( %d 정수, %f 실수, %c 문자, %s 문자열)
print("제 이름은 %s 입니다"%name)
print("제 이름은 %s입니다. 저는 %s살입니다." %(name, age))

# f-string 활용해서 문자열 출력
print(f"제 이름은 {name} 입니다. 저는 {age}살 입니다.")

# 딕셔너리
num ={"one":1,"two":2,"three":3}
print(num["one"]) # key 를 사용해서 value 출력
#print(num["four"]) # key error

# get() 메서드는 특정 키에 해당하는 값을 가져올때 사용
# 존재하지 않는 키를 조회해도 오류가 발생하지 않는다.
print(num.get("four", "해당키가 없습니다."))

# get() 개수를 카운트 할때 사용 가능
fruits = ["apple", "banana", "apple", "melon", "banana", "apple"]
count = {}  # set을 만들려면 b = set()

for fruit in fruits:
    count[fruit] = count.get(fruit, 0) + 1
print(count)
