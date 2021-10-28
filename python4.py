# 제4장 데이터 구조

'''4.1 list'''
# list -> 순서대로 정리된 항목들을 담고 있는 자료구조. 항목의 목록을 저장할 수 있음
#      -> 파이썬에서는 쉼표로 각 항목을 구분
#      -> list를 정의할 때는 대괄호[]를 이용해서 선언
#      -> 한 번 list를 만들어 두면 여기에 새로운 항목을 추가하거나 삭제할 수 있으며, 특정 항목이 존재하는지 검색 가능
#      -> list는 0 개 이상의 요소로 구성됨
#      -> 앞은 0부터 시작, 뒤는 -1부터 시작 

la = [11, 22, 33] # 리스트를 생성하여 la에 저장 
ld = [] # 빈 list를 생성하여 ld에 저장
print() 

# 비어있는 list는 list() 함수로 나타냄
another_empty_list = list()
print(another_empty_list)

le = [[11, 22], [33, 44, 55]] # 중첩된 리스트. 리스트 안에 리스트 오는 것 가능 
print()

# list() 함수를 이용해서 데이터 목록 나타내고 수정 
print(list('python'))

birthday = '2/13/1957'
print(birthday.split('/'))

splitme = 'a/b//c/d///e'
print(splitme.split('/'))
print() 

# [색인번호] 이용한 항목 검색
man = ['홍길동', '이순신', '강감찬']
print(man) # 전체 목록
print(man[0]) # 첫 번째 항목 검색
print(man[-1]) # 역으로 항목 검색
print()

# list() 간 연결 -> list()에서 이미 선언된 다른 list 제목을 포함한 여러 유형의 요소를 나타낼 수 있음
city = ['서울시', '고양시']
gu = ['종로구', '영등포구', '덕양구']
dong = [1, '인사동', 2, '양평동', 3, '성사동']
all_data = [city, gu, '중구', dong]
print(all_data)
print(all_data[1])
print(all_data[1][0])

L = [-17.5, "kilo", 49, "V", ["ram", 5, "echo"], 7]
print(L[1][0])
print(L[-2][2])
print(L[4][2][1])
print() 
      
# list 항목의 수정
gu = ['종로구', '영등포구', '덕양구']
gu[2] = '일산동구'
print(gu)
print()

# 색인 범위로 항목 검색 및 출력 -> [n:m]은 n은 포함, m은 미포함
#                               -> [::n]은 n에서 하나 뺀 만큼 건너뜀 
gu = ['종로구', '영등포구', '덕양구']
print(gu[0:2]) # 0 1
print(gu[::2]) # 처음부터 1만큼 건너뛰어서 검색 
print(gu[::-2]) # 마지막 항목부터 1만큼 건너뛰어서 검색
print(gu[::-1]) # 역으로 전체 항목 검색

L = [15.8, "kilo", 49, "V", ["ram", 5, "echo"], 7]
print(L[0:3])
print(L[::3])
print(L[::-4])
print(L[::-1])
print()

# 두 개 이상의 변수가 선언된 경우 그 중 하나 앞에 *가 붙으면 변수에 항목이 할당. 나머지 모든 변수는 * 표시된 변수에 연결
first, *rest = [9, 2, -4, 8, 7]
print(first, rest)

first, *mid, last = "홍길동 이순신 강감찬 권율 유성룡".split()
print(first, mid, last)

*directories, executable = "/usr/local/bin/gvim".split("/")
print(directories, executable)
print()

# list 메소드의 종류
# append(x)     -> x를 리스트의 마지막 요소로 추가
# extend(list)  -> list의 요소로 원 리스트를 확장
# insert(i,x)   -> x를 i번째 위치로 끼워 넣음
# remove(x)     -> x와 같은 첫 번째 요소를 삭제
# pop()         -> 마지막 요소를 삭제하고 반환
# pop(i)        -> i번째 요소를 삭제하고 반환
# clear()       -> 모든 요소를 삭제
# index(x)      -> x와 같은 첫 번째 요소의 인덱스를 반환
# count(x)      -> x와 같은 요소들의 개수를 구함
# sort()        -> 요소의 정렬
# reverse()     -> 역순으로 배열
# copy()        -> 요소를 복사하여 반환 
 
x = list(range(5)) # range -> range(0,5,1)이라면 0부터 5 전까지 1씩 증가시키라는 의미
x.append([5,6]) # x의 마지막 요소로 [5,6]이 들어감 
print(x)

x = list(range(5))
x.extend([5,6]) # x의 마지막에 [5,6]의 요소를 병합시킴
print(x)
print()
 
# append() 함수와 pop() 함수를 이용하여 리스트를 스택(stack) 처리 -> 스택은 나중에 들어간 것이 먼저 나오는 자료구조
stack = [3, 4, 5]
stack.append(6)
print(stack)
stack.append(7)
print(stack)
stack.pop()
print(stack)
stack.pop()
print(stack)
stack.pop()
print(stack)
print()

animals = ['강아지', '토끼', '고양이']
sorted_animals = sorted(animals) # animals 원본은 바뀌지 않음 
print('동물들 list: {}'.format(animals))
print('정렬된 동물들 list: {}'.format(sorted_animals))
animals.sort() # animals 원본 자체가 바뀜  
print('sort 메소드에 의해 정렬된 동물들: {}'.format(animals))
print()


'''4.2 Tuple'''
# tuple -> list와 마찬가지로 tuple은 임의 항목의 연속
#       -> list와 달리 tuple은 변경 불가능하며 tuple이 정의된 후에 항목을 추가, 삭제 또는 변경할 수 없음
#       -> 정의할 때 대괄호 대신 괄호()로 나타내며, 읽기 전용 목록으로 간주
#       -> tuple도 인덱싱과 슬라이싱이 가능하고 공통적인 연산(덧셈과 곱셈)이 가능
#       -> 데이터를 보호할 수 있음

t1 = () # empty tuple 생성 
t2 = (11,) # tuple의 요소가 하나일 경우 반드시 끝에 콤마를 붙여야 함
t3 = (11, 22)
t4 = ('abc', 11, [22, 33])
t5 = ((11, 22), ('hi', 'world'))
t6 = ((True, False))

# 빈 tuple을 생성하는 경우만 제외하고 모두 괄호 생략 가능
t2 = 11, 
t3 = 11, 22
t4 = 'abc', 11, [22, 33]
t5 = (11, 22), ('hi', 'world')
t6 = (True, False), # 콤마를 붙이지 않으면 True와 False를 갖고 있는 tuple이 되고, 콤마를 붙이면 True와 False를 가진 tuple을 첫 번째 요소로 가진 tuple이 됨 

# 여러 개의 변수를 동시에 생성시키는 경우
a,b,c = 11,22+33j,True # 좌변과 우변 모두 괄호가 생략된 tuple 
t = 11, 22, 33
e,f,g = t # e=t[0], f=t[1], g=t[2]와 같음
print(a)
print(b)
print(c) 
print(e)
print(f)
print(g)
print()

# tuple 연산자 -> 결합 및 복사 작업 후 새로운 tuple 생성
print(len((1,2,3))) #요소의 개수
print((1,2,3) + (4,5,6)) # tuple의 연결
print(['Hi!']*4) # 복사
print(3 in (1,2,3)) # 요소의 존재 여부
for x in (1,2,3):  # 반복
    print(x)
print()

# tuple 내장 함수
# len(tuple)    -> tuple 요소의 개수 출력
# max(tuple)    -> tuple 요소의 최대값 출력
# min(tuple)    -> tuple 요소의 최소값 출력
# tuple(seq)    -> tuple 요소의 전체 출력
# tuple.count() -> tuple 요소의 개수
# tuple.index() -> tuple 요소의 위치(index)

list1 = ['홍길동', '이순신', '강감찬', '권율']
tuple1 = tuple(list1) # list를 tuple로 바꿀 수 있음 
print(tuple1)
print()

# tuple을 사용하여 동시에 여러 변수에 값을 할당 
months_of_the_year = ('1월', '2월', '3월', '4월')
(jan, feb, mar, apr) = months_of_the_year
print(jan)
print(mar) 
print()

# 내장 max() 및 min() 함수를 사용하여 최댓값과 최솟값 반환
def high_and_low(numbers): # 함수. numbers는 인수(매개변수)
    highest = max(numbers)
    lowest = min(numbers)
    return (highest, lowest) # 파이썬은 리턴값을 여러 개 넘길 수 있음 
lucky_numbers = [37, 71, 47, 13, 17, 67]
(highest, lowest) = high_and_low(lucky_numbers)
print('최댓값 = {}'.format(highest))
print('최솟값 = {}'.format(lowest))
print()

a,b = b,a # 두 변수의 값 교환. 단 왼쪽에 있는 변수의 개수와 오른쪽에 있는 값의 개수는 같아야 함

a,b = (1,2)
print(a,b)
del a,b # 요소의 값 삭제

def f(x):
    return x, x**2 # 연산의 정의
for x,y in ((1,1), (2,4), (3,9)): # 연산의 반복
    print(x,y)

eyes = ("갈색", "빨강", "노랑", "녹색", "파랑", "회색")
colors = ("hair", eyes)
print(colors[1][3:-1]) # 녹색, 파랑 추출

things = (1, -7.5, ("pea", (5,"Xyz"), "queue"))
print(things[2][1][1][2]) # z 추출
print()

# tuple은 list로, list는 tuple로 변환할 수 있음
# list를 tuple로 변환하려면 list 변수 명을 tuple 함수 안에 대입하고, tuple을 list로 변환하려면 list 함수 안에 tuple 변수 명을 대입
# tuple의 요소값을 지우거나 변경하려고 할 경우 오류 발생. tuple의 요소값은 한 번 정하면 지우거나 변경할 수 없음

t1 = (1, 2, 'a', 'b') # tuple 인덱싱하기
print(t1[0])
print(t1[3])

t1 = (1, 2, 'a', 'b') # tuple 슬라이싱하기
print(t1[1:])

t2 = (3, 4) # tuple 더하기
print(t1 + t2)

print(t2 * 3) # tuple 곱하기
print()


'''4.3 dictionary'''
# dictonary -> 요소 순서는 중요하지 않음. 임의의 순서 가짐 
#           -> 변경 가능하므로 키 또는 값 요소를 추가, 삭제 및 변경 가능
#           -> {}로 둘러싸서 표현하고, {key1:value1, key2:value2, ...} 형태로 각 요소가 '키:값' 쌍을 이루고 있음
#           -> dictonary 함수에는 keys, values, items, clear, get, in 등이 있
#           -> 키는 유일해야 하지만 값은 상관없음
#           -> 값은 모든 데이터 유형을 가질 수 있지만 키는 문자열, 숫자, tuple과 같이 변경 불가 
dict1 = {'Alice': '2341', 'Beth': '9102', 'Cecil': '3258'}
dict2 = {'abc': 456} # 단일 선언
dict3 = {'abc': 123, 98.6: 37}

dict1 = {'Name': 'w3big', 'Age': 7, 'Class': 'First'}
print(dict1['Name'])

empty_dict = {} # 빈 dictionary 생성 
print(empty_dict)

d1 = dict({"id": 1957, "이름": "이순신", "size": 3})
print(d1) # dict 함수를 이용해서 dictionary를 바로 작성

d2 = dict(id=1957, 이름="이순신", size=3)
print(d2)

d3 =dict([("id", 1957), ("이름", "이순신"), ("size", 3)])
print(d3)

d4 = dict(zip(("id","이름","size"), (1957, "이순신", 3)))
print(d4)

d5 = {"id": 1957, "이름": "이순신", "size": 3}
print(d5)

pythons = {
    '의인': '홍길동',
    '장군': '이순신',
    }
print(pythons)
pythons['왕'] = '세종대왕' # dictionary에 새로운 key와 value 값을 추가 
print(pythons)
print()

# dictionary 안에 key를 이용해서 검색할 경우 dictionary_name.keys() 이용
# value 값을 이용해 검색할 경우 values() 메소드를 사용
# 검색 후 key 또는 value 값이 존재할 경우 True 반환, 그렇지 않으면 False
contacts = {'의인':['홍길동','임꺽정'], '장군':'이순신'}
if '의인' in contacts.keys():
    print("의인 = ", contacts['의인'][0])
print('이순신' in contacts.values())

contacts = {'의인':['홍길동','임꺽정'], '장군':'이순신'}
print(contacts.keys()) # dictionary 안에 key값만 검색
print()

contacts = {'의인':['홍길동','임꺽정'], '장군':'이순신'}
contacts['장군'] = '강감찬' # 수정 
print(contacts)

up = {'의인': ['이황', '정성원']}
contacts.update(up) # update() 메소드를 이용해서 한꺼번에 여러 값 수정 
print(contacts)
print()

contacts = {'의인': '홍길동', '장군': '이순신', '왕': '세종대왕'}
del contacts['왕'] # del 명령으로 해당 요소 삭제 
print(contacts) 

contacts.clear() # clear() 메소드를 이용하여 전체 요소 삭제 
print(contacts)
print()

# dictonary 메소드 종류
# clear()           -> 모든 요소를 dict d에서 제거
# copy()            -> dict d의 복사된 요소를 반환
# fromkeys(s,v)     -> 문자열 s의 항목에서 v까지 연관된 key의 dict를 반환
# get(k)            -> key k의 연관 값을 반환하거나, k가 dict d에 없으면 None을 반환
# get(k,v)          -> key k의 연관 값을 반환하거나, k가 dict d에 없으면 v를 반환
# items()           -> dict d의 모든 (key, value)의 내용을 반환
# keys()            -> dict d의 key의 내용을 반환
# pop(k)            -> key의 연관 값을 반환. key가 k인 요소를 제거하거나 k의 key가 d에 없으면 KeyError 예외를 발생
# pop(k,v)          -> key의 연관 값을 반환. key가 k인 요소를 제거하거나 k가 dict d에 없으면 v를 반환
# popitem()         -> dict d에서 임의의 (key, value)를 반환하고 제거. d가 비어있는 경우 KeyError 예외를 발생
# setdefault(k,v)   -> dict.get() 메소드와 비슷. key가 dict d에 없으면 key가 k이고 value가 없거나 v가 지정되면 v의 새 요소가 삽입된다는 점을 제외
# update(a)         -> d에서 d에 없는 모든 (key, value) 값을 추가. d와 a에 있는 모든 key에서 d의 연관 값을 a의 값으로 수정
# values()          -> dict d의 모든 값 반환

d = {'a':1, 'b':2}
f = d.copy()
print(f)

s = ['a', 'b', 'c']
d = d.fromkeys(s, 1) # s는 key, 1은 value가 됨 
print(d)

d = {'hello': 1}
d['g'] = d.get('g', 0) # g를 검색하고, 없다면 key가 g, value가 0인 것을 넣음 
print(d)

d = {'a':1, 'b':2, 'c':3}
print(d.items())
print(type(d.items()))

d = {'a':1, 'b':2, 'c':3}
print(d.keys())
print(type(d.keys()))

d = {'a':1, 'b':2, 'c':3}
print(d.pop('a')) # a가 반환되면서 제거됨 
print(d.pop('d',-1)) # d가 없기 때문에 -1 나옴 

d = {'a':1, 'b':2, 'c':3}
print(d.popitem()) # 랜덤이긴 하지만 일반적으로는 맨 뒤 값이 삭제됨 

d = {'hello':2, 'world':3}
print(d.setdefault('hello',None)) # hello가 존재하면 2(값)가 나오고, 존재하지 않으면 None이 나옴 
print(d.setdefault('world',None))
print(d.setdefault('', 3)) # 없으면 집어넣음. get은 없으면 끝, setdefault는 없으면 집어넣음 
print(d)

d = {'banana':1, 'apple':2, 'pineapple':3}
print(d.update({'melon':4, 'tomato':5}))
print(d)

print(d.keys())
print(d.values())
print() 

pythons = {'Chapman':'Graham', 'Cleese':'John', 'Jones':'Terry'}
copy_pythons = pythons
pythons['Cleese'] = 'Tom' # copy_pythons도 같이 변경됨 
print(pythons)
print(copy_pythons)
print()


'''4.4 Set'''
# set -> 선언된 0개 이상의 객체를 참조하기 위한 순서가 없는 collection
#     -> 요소를 쉽게 추가 또는 제거할 수 있고 순서가 선언되지 않아서 색인 개념이 없음
#     -> dictionary에서 값을 제거한 키와 비슷한 원리
#     -> 중괄호로 값을 구분
#     -> 순서대로 저장되지 않음. 중복된 값은 한 번만 저장 
           



