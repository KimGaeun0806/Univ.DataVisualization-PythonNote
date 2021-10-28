# 제3장 자료형과 연산자

'''3.1 자료형'''
# 대표적인 다섯 가지 데이터 유형 -> 숫자형(Number), 문자열(String), 리스트(List), 튜플(Tuple), Dictionary

# 숫자형 -> 10진수(0-9)를 사용할 수 있으며, 특별한 접두어 [0x(16진수), 0o(8진수), 0b(2진수)]같은 것이 없으면 10진수로 간주
# 실수를 정수로 바꾸려면 int를 사용하면 됨. 소수 이하 자리는 잘림
a = int(5.4)
print(a)

b = int(-1.75)
print(b) # -7/4 = -1.75, -7//4 = -2임. //와 혼동하지 말기
print()

# 파이썬에서 나누기는 /와 // 두 가지가 있다는 것 주의하기 
# 파이썬에서 정수 나누기의 결과는 항상 음수의 무한대로 반올림
# 데이터 유형을 확인할 때는 type() 함수 사용
x = 1
print(type(x))

x = 1.0
print(type(x))

x = int(x)
print(type(x))
print()

# x + y     -> x와 y를 더하기
# x - y     -> x에서 y를 빼기
# x * y     -> x와 y를 곱하기
# x / y     -> x를 y로 나누기. 항상 float(또는 x 또는 y가 복소수이면 복소수)를 산출
# x // y    -> x를 y로 나누기. 분수 부분을 제거하여 항상 int 결과를 산출
# x % y     -> x를 y로 나누고 나머지를 산출
# x ** y    -> x의 y제곱의 연산
# -x        -> x를 부정. 0이 아니면 x의 부호를 변경하고 0이면 반응없음. 양수는 음수로, 음수는 양수로 
# +x        -> 아무것도 하지 않음. 코드를 명확히 하기 위해 사용

# abs(x)        -> 절댓값 x 산출
# divmod(x, y)  -> x를 y로 나눈 몫과 나머지를 두 int의 튜플로 반환
# pow(x, y)     -> x를 y의 거듭 제곱으로 올림
# pow(x,y,z)    -> (x ** y) % z 연산
# round(x, n)   -> n이 음의 int이면 n을 정수로 반올림한 x를 반환하고 n이 양의 정수이면 n을 소수 자리로 반올림하여 x를 반환 (반환 값은 x와 같은 형태)

# 수식의 진수 변환 종류 
# bin(i)        -> i의 2진수를 문자로 반환 (bin(1980) == '0b11110111100')
# hex(i)        -> i의 16진수 표현을 문자열로 반환 (hex(1980) == '0x7bc')
# int(x)        -> 객체 x를 정수로 변환(반올림 x). 실패할 경우 ValueError를 발생시키거나 x의 데이터 유형이 정수 변환을 지원하지 않는 경우 TypeError를 발생. x가 정수와 소수 이하 수치로 나타나면 잘리고 정수로 나타냄
# int(s, base)  -> str을 정수로 변환. 실패하면 ValueError를 발생. 선택적 base 인수가 주어지면 2와 36 사이의 정수
# oct(i)        -> i의 8진수 표현을 문자열로 반환 (oct(1980) == '0o3674')

value = 60
b = bin(value)
o = oct(value)
h = hex(value)
print(b)
print(o)
print(h)
print()

num = 12345
a = int(bin(num), 2) # 2진수라고 알려주는 것 -> 2진수를 10진수로 변환 
print(a) # 10진수 출력 

b = int(oct(num), 8) # 8진수라고 알려주는 것 
print(b) # 10진수 출력 

c = int(hex(num), 16) # 16진수라고 알려주는 것 
print(c) # 10진수 출력
print()

# 비트 연산 종류 
# i|j   -> i와 j의 비트 연산 OR(|). 음수는 2의 보수를 사용
# i^j   -> i와 j의 비트 단위 배타적 논리합(XOR) (다르면 참, 같으면 거짓)
# i&j   -> i와 j의 비트 연산 AND(&)
# i<<j  -> 정수 i 내부 비트를 j 비트만큼 왼쪽으로 이동
# i>>J  -> 정수 i 내부 비트를 j 비트만큼 오른쪽으로 이동
b1 = 0x57
b2 = 0xf5
print("bin(b1|b2) =", bin(b1|b2)) # bit or 연산자 |
print("bin(b1&b2) =", bin(b1&b2)) # bit and 연산자 &
print("bin(b1^b2) =", bin(b1^b2)) # bit xor 연산자 ^
print("bin(b1<<1) =", bin(b1<<1)) # left shift 연산자 <<
print("bin(b1>>3) =", bin(b1>>3)) # right shift 연산자 >>
print()

# boolean (True, False) -> 참과 거짓을 나타내는 자료형 (False = 0, True = 1)
# 비교 연산자 -> >, <. ==, !=, >=, <=
# 논리 연산자 -> and(&): 두 값이 모두 참일 때 참을 반환
#             -> or(|): 둘 중 하나라도 참이면 참을 반환
#             -> not: 반대의 값 반환
t = True
f = False
print(t and f)
print(t and True)
print(int(True))
print(int(False))
print(1>2, 1<2)
print()

a = 3
b = 4
print(a%3 == 0 and b%2 == 0)
print(type(a == 3))
print(bool(1))
print(bool(-1)) # 0을 제외하고는 다 True라고 생각하면 됨 
print(bool(0))
print()

# 실수(float) -> float형은 범위가 다른 floating-point 숫자를 포함
#             -> float형의 숫자는 소수점 또는 지수 표기법(0.0, 4., 5.7, -2.5, -2e9, 8.9e-4 등)으로 나타냄
#             -> 숫자에 소수점이 포함돼있으면 모두 실수로 표현
#             -> 실수는 정수와 마찬가지로 변경이 불가능한 자료형
#             -> 실수끼리 연산을 하면 끝에 작은 오차가 붙어서 나오게 됨 
print(8.9e-4)
pi = 3.14
print("변수 pi의 자료형은", type(pi))
pi = 3
print("변수 pi의 자료형은", type(pi))
print()

a = 10/3
print("a = %f" %a) # 포맷을 맞출 수 있음. %f 자리에 a값 넣기. 소수점 여섯자리까지 나옴 
print("a = %.10f" %a) # 소수점 열자리까지 나옴 
print("a = %.20f" %a) # 소수점 스무자리까지 나옴 
print("a = %.2f" %a) # 소수점 두자리까지 나옴 
print("a = %.1f" %a) # 소수점 한자리까지 나옴

f = 5.15 - 5.05
print(f) # 포맷을 주지 않고 했을 때 너무 작은 숫자는 오차가 발생할 수 있음 
print()

# 복소수(complex) -> a+bi로 나타낼 수 있는 숫자로, 여기에서 a(실수부)와 b(허수부)는 실수, i는 허수 단위로 i^2 = -1을 만족. 파이썬에서는 소문자 j 또는 대문자 J를 사용
# complex(real, imag)로 정의
# 복소수에서 실수부에 접근하기 원할 때 .real을 사용하고 허수부에 접근할 때는 .imag를 사용하며, 켤레복소수를 나타낼 경우 conjugate()를 사용
a = 2+3j
print(a)
b = complex(3, -4)
print(b)

print(a.real, a.imag)
print(b.real, b.imag)

print(1e2j)

a = complex(10, 20)
print(type(a))
print(a)
print(a.real)
print(a.imag)
print(a.conjugate()) # 켤레복소수 -> 허수부분 부호 바꿈 

b = 7 - 2j
print("실수: {}, 허수: {}".format(b.real, b.imag)) # 포맷 사용 
print()

# 부동 소수점(decimal) -> 소수점의 위치를 고정하지 않고 그 위치를 나타내는 수를 별도 표현
# 유효숫자를 나타내는 가수, 소수점의 위치를 풀이하는 지수로 표현
# '[가수]*[밑수]^[지수]'와 같은 형태
# 일반적으로 이진법을 이용해서 밑수를 2로 하고 부호를 나타내는 하나의 비트를 추가
# 부호, 지수부, 가수부 세 부분으로 나누어서 실수 표현
# 십진법에서 decimal 객체의 일반형 -> decimal.Decimal([값[,문자열]])
# 'Infinity', 'Inf'(무한대), '-Infinity', '-Inf'(음의 무한대), 'NaN'(Not a Number), '-0' 형태도 가능

import decimal # decimal 객체를 연결 
print(decimal.Decimal(3))
print(decimal.Decimal('1.1'))
print(decimal.Decimal(str(1/7)))
print(decimal.Decimal((0, (3, 1, 4), -2))) # -2는 소수점 자리 수 나타낸 것 
print(decimal.Decimal("-Infinity"))
print(decimal.Decimal('-0'))
print(decimal.Decimal('NaN'))

d = decimal.Decimal((0, (3, 1, 4), -2))
print(decimal.Decimal(d))
print()

# Decimal 객체의 내장 메소드 종류
# sqrt()            -> Decimal의 제곱근 결과 반환
# exp()             -> 자연상수(e) ** Decimal 결과를 반환
# In()              -> Decimal의 자연로그 결과를 반환
# compare(other)    -> 두 Decimal 객체를 비교하여 결과를 Decimal 객체로 반환. 메서드 호출객체가 더 크면 Decimal('1')을, 같은 경우는 Decimal('0')을, 작은 경우는 Decimal('-1')을 반환
# copy_abs()        -> 원본의 절댓값을 갖는 Decimal 객체를 반환
# copy_negate()     -> 원본의 음수값을 갖는 Decimal 객체를 반환
# copy_sign(other)  -> 원본 값에 인자(other)의 부호를 갖는 Decimal 객체를 반환 
# is_signed()       -> 부호 비트가 설정되어 있으면(즉 음수이면) True를 반환 # is가 붙어있으면 맞냐틀리냐임 (함수 만들 때 참고) 
# is_finite()       -> 유한수인 경우 True 반환
# is_infinite()     -> 무한인 경우 True 반환
# is_zero()         -> '0'(+0, -0)인 경우 True 반환


'''3.2 string'''
# 파이썬의 문자열은 따옴표로 묶인 연속된 문자 집합으로 식별. 문자열은 문자, 단어 등으로 구성된 문자들의 집합을 의미
# 작은 따옴표나 큰 따옴표 허용
title = "우리" '는' "하나다" # 문자열 결합
print(title)
print()

# 특수문자를 나타내는 이스케이프 시퀀스 -> 문자열 내의 일부 문자의 의미를 바꾸어 다른 효과
# \newline  -> 무시(연속 줄)
# \\        -> 백슬래시(\ 하나만 표시)
# \'        -> 작은 따옴표(' 표시)
# \"        -> 큰 따옴표(" 표시)
# \a        -> 벨
# \b        -> Backspace
# \f        -> Formfeed (프린트할 때 다음 페이지로 넘어감)
# \n        -> linefeed (다음 줄로 보냄. 엔터키 역할)
# \r        -> Carriage return (그 줄 맨 앞으로 보냄)
# \t        -> Horizontal tab (가로 탭)
# \v        -> Vertical tab (새로 탭) 
# \xhh      -> hh 16진수 값
# \ooo      -> ooo 16진수 값

S = "p\ty\nt\x00m"
print(S)
print(len(S)) # 문자열 길이

x = "C:\py\code" # 원래는 \\처럼 두 개를 써야하지만 파이썬은 \ 하나만 써도 오류가 나지 않을 수도 있음
print(x)
print(len(x))

print('\tabc')
print('a\tbc')
print('ab\tc')
print('abc\t\n')
print()

# 세 따옴표 다중 행 블록 문자열
mantra = """항상 인생의
밝은 영역만 보아야 합니다."""
print(mantra)
print()

# 문자열 더하기
head = "Python "
tail = "is fun!"
print(head + tail)
print()

# 문자열 곱하기 -> *는 문자열의 반복을 뜻하는 의미로 사용. 출력시 띄어쓰기는 x
a = "python"
print(a*3)
print()

# string의 색인(indexing)과 추출(slicing)
# 문자열에서 색인값을 지정하면 특정 문자들 출력 
# 추출 -> S([i:j]) (i 포함, j 미포함)
#      -> 추출범위는 기본이 0이며 문자열 길이가 생략된 경우 문자열의 기본값
#      -> S[1:3]은 0, 1, 2, 3이 있다면 그 중 1, 2만 추출
#      -> S[1:]은 기준 1에서 끝까지의 문자 추출
#      -> S[:3]은 기준 0에서 3을 포함하지 않는 문자 추출
#      -> S[:-1]은 기준 끝에서 1문자 뺀 나머지 추출
#      -> S[1:10:2]은 기준 1에서 10 전까지 2컬럼의 문자(1, 3, 5, 7, 9)를 추출 (2는 2칸씩 점프하라는 뜻)
a = "Hello Python"
print(a[0] + a[1] + a[2] + a[3] + a[4])
print(a[0:5]) # 0 1 2 3 4
print(a[6:12]) # 6 7 8 9 10 11 
print(a[3:]) # 3부터 끝까지 
print(a[:7]) # 0부터 6까지 
print(a[:]) # 처음부터 끝까지 

a = "Python"
print(a[2:-2]) # 2 3 
print(a[::2]) # 처음부터 끝까지 2칸 단위 
print(a[::-1]) # 거꾸로 출력 (숫자는 간격) 
print() 

# string의 변환
# int(x[,base]) -> 문자를 숫자로 변환. base는 진법을 나타냄
# float(x)      -> 실수 문자를 실수로 변환
# complex(x)    -> 문자를 복소수로 변환
# repr(x)       -> 숫자를 문자열로 변환
# eval(str)     -> 문자열로 된 수식을 연산하여 결과를 나타냄
# chr(x)        -> 아스키코드 값을 문자로 변환
# ord(x)        -> 문자값을 아스키코드값으로 변환
# hex(x)        -> 숫자값을 16진수 문자값으로 변환
# oct(x)        -> 숫자값을 8진수 문자값으로 변환
# bin(x)        -> 숫자값을 2진수 문자값으로 변환
# len(x)        -> 문자열의 길이를 나타냄
# split(x)      -> 분리(x)문자로 문자열을 분리해서 나타냄
# join()        -> 분리된 문자열들을 지정한 결합 문자로 묶어서 나타냄

print(int('64'), int('100', 8), int('40', 16), int('1000000', 2))
print(int('0x40', 16), int('0b1000000', 2))

print(float("1.5"))
text = "1.234E-10"
print(float(text))

print(complex("11"))

print(repr(10))
print(repr(1+2))

print(eval('64'), eval('0o100'), eval('0x40'), eval('0b1000000'))

print(chr(115), chr(97))

print(ord('a'), ord('X'), ord('A'))

print(hex(64), hex(85))

print(oct(255))
x = 10
print(oct(x))

print(bin(15))
x = 10
print(bin(x))

S = 'XYZ'
print(len(S))
print(len("korea"))

b = 'korea'
print(b.split('r'))

B = b'spam'
print(B.split(b'pa'))

print('SPAM'.join(['eggs', 'sausage', 'ham', 'toast']))
line = 'aa bbb c'
print(''.join(x.upper() for x in line.split() if len(x) > 1)) # .split()이므로 공백으로 분리하게 됨. 그럼 aa, bbb, c로 나눠짐. 그것들이 for문에 하나씩 오게 됨. 근데 len(x)>1일 때라는 조건이 붙음. x.upper()가 붙었으므로 대문자로 변환. 그리고 ''.join이므로 사이에 아무것도 없이 붙여쓰라는 뜻   
print() 

# string 메소드
# capitalize()                      -> 첫 문자를 대문자로 변환
# find(keyword,[start,[end]])       -> 문자열 keyword가 나타나는 첫 번째 인덱스를 반환. start, end를 지정하면 검색한 것과 같은 효과, keyword를 찾지 못하면 -1을 반환
# startswith(prefix,[start,[end]])  -> prefix로 문자열이 시작되면 True, 아니면 False
# endswith(postfix,[start,[end]])   -> postfix로 문자열이 끝나면 True, 아니면 False
# count(keyword,[start,[end]])      -> 문자열에 keyword가 몇 번이나 포함되어 있는지 출력
# replace(old,new,[count])          -> old를 new로 치환한 결과를 반환. 여러 개 있다면 count 개수만큼 치
# partition(separator)              -> 문자열을 separator로 나눔
# strip([chars])                    -> 문자열의 양쪽을 잘라냄. chars가 입력되지 않으면 공백문자(Space, Tab, Enter)를 제거하며, chars가 지정된 경우 chars의 모든 조합을 제거
# isalpha()                         -> 알파벳으로만 이루어져 있으면 True, 다른 문자가 포함되어 있으면 False
# isalnum()                         -> 알파벳과 숫자로 이루어져 있으면 True, 다른 문자가 포함되어 있으면 False
# isnumeric()                       -> 숫자로 이루어지면 True, 다른 문자가 있으면 False
# isdecimal(), isdigit()            -> 10진수로 이루어져있으면 True, 다른 문자가 있으면 False
# center(width[,fillchar])          -> width만큼의 공간을 잡고 가운데정렬, fillchar가 지정된 경우 빈공간을 fillchar로 채움

print('hello world!'.capitalize())

s = "python"
print(s.find("t"))

print('python'.startswith('p'))
print('python'.startswith('y'))
print('python'.endswith('p'))
print('python'.endswith('n'))

print('banana'.count("a"))

print('python-파이썬'.partition('-')) # - 를 기준으로 나눔

print(' python '.strip())
print('!@<<Python>>@!'.strip('<>!@')) # 순서 상관없이 제거 

print('python'.isalpha())
print('python1'.isalpha())
print('python1'.isalnum())
print('1234'.isnumeric())
print('3151 '.isnumeric()) # 공백 포함돼서 False 
print('1234'.isdecimal())

print('center'.center(10,' ')) # 'center' 포함해서 10자리이므로 양쪽으로 공백 2개씩 생김
print()

# String format -> 문자열 내에 어떤 값을 삽입하는 방법 
# 숫자 바로 대입(%d) -> 문자열 안에서 숫자를 넣고 싶은 자리에 %d라는 문자를 넣어주고, 삽입할 숫자는 가장 뒤에 있는 % 문자 다음에 입력 (%d는 문자열 포맷 코드)
print("I eat %d apples." %2)

# 문자열 바로 대입(%s)
print("I eat %s apples." %"two")

# 변수 대입
number = 3
print("I eat %d apples." %number)

# 2개 이상의 값 넣기 -> 2개 이상의 값을 넣으려면 마지막 % 다음 괄호 안에 콤마로 구분하여 각각의 변수를 넣어 줌
number = 10
day = "three"
print("I ate %d apples. So I was sick for %s days." %(number, day))
print()

# 문자열 포맷 코드
# %d -> 정수형
# %s -> 문자열형
# %f -> 실수형. 무조건 소수점 여섯자리로 출력되고, 반올림됨. %.3f와 같이 적어주면 소수점 세자리까지 나옴 
# %c -> 문자형
# %o -> 8진수
# %x -> 16진수
# %% -> %문자 자체

# 포맷팅 연산자 %d와 %를 같이 사용할 때는 %%를 선언 
print("Error is %d%%." %98) # %d%와 같이 쓰면 에러 발생
print()

print("%10s" %"hi") # s앞의 숫자는 공백의 개수를 나타냄. 전체 길이가 10개인 문자열 공간에서 hi를 오른쪽으로 정렬하고 그 앞의 나머지는 공백으로 남겨두라는 의미 
print("%-10sjane." %"hi") # s앞의 숫자는 문자열 이후 공백의 개수를 나타냄. 왼쪽 정렬 

print("%0.4f" %3.42134234) # 소수점 네자리까지만 
print("%10.4f" %3.42134234) # 소수점 네자리까지 표시하고, 전체 길이가 10개인 문자열 공간에서 오른쪽으로 정렬 -> 왼쪽 공백 4개

print('%10s' %('python',)) # 문자 앞 공백 4개
print('%.5s' %('python',)) # 5문자만 지정되고 나머지는 잘림
print('%-10.5s'%('python',)) # 5문자만 지정되고 잘리며 이후 5공백

print('%f' %(3.1415926535656,)) # 소수점 일곱번째 자리에서 반올림됨 -> 소수점 여섯자리까지만
print('%06.2f' %(3.14159889,)) # 빈자리를 0으로 채우라는 뜻. 소수점 포함 여섯자리. 소수점 아래 두자리
print('%+d' %42) # 기호 표시하기
print()

data = {'first': 'Hodor', 'last': 'Hodor!'}
print('%(first)s %(last)s' % data) 

print('%.*s = %.*f' %(3, 'Gibberish', 3, 2.7182)) # *부분에 차례로 들어감 
print('%*.*f' %(5, 2, 2.7182))

print('{0}, eggs, and {1}'.format('spam', 'SPAM!')) # 인덱스값 사용
print('{}, eggs, and {}'.format('spam', 'SPAM!')) 

print('{:,.2f}'.format(296999.2567)) # 세 자리씩 끊어서 콤마 찍어줌
print()

#  문자열 format들의 format 함수 이용
print("I eat {0} apples.".format(3)) # 숫자 바로 대입 
print("I eat {0} apples.".format("five")) # 문자열 바로 대입

number = 3
print("I eat {0} apples.".format(number)) # 숫자 값 가진 변수 대입 

number = 10
day = "three"
print("I ate {0} apples. So I was sick for {1} days.".format(number, day)) # 2개 이상의 값 넣기

print("I ate {number} apples. So I was sick for {day} days.".format(number = 10, day = 3)) # 이름으로 넣기
print("I ate {0} apples. So I was sick for {day} dyas.".format(10, day = 3)) # 인덱스와 이름을 혼용해서 넣기
print()

print("{0:<10}".format("hi")) # 왼쪽 정렬
print("{0:>10}".format("hi")) # 오른쪽 정렬
print("{0:^10}".format("hi")) # 가운데 정렬

print("{0:=^10}".format("hi"))
print("{0:!<10}".format("hi"))

y = 3.42134234
print("{0:0.4f}".format(y))

print("{{ and }}".format())
print()

print('{first} {last}'.format(**data)) # *로 입력되는 값의 수를 알려줘야 함

person = {'first': 'Jean-Luc', 'last': 'Picard'}
print('{p[first]} {p[last]}'.format(p=person))

print('{:{align}{width}}'.format('python', align='^', width='10'))
print('{:.{prec}} = {:.{prec}f}'.format('Gibberish', 2.7182, prec=3))
print('{:{}{}{}.{}}'.format(2.7182818284, '>','+',10,3))
print('{:{}{sign}{}.{}}'.format(2.7182818284, '>',10, 3, sign='+'))
print()








