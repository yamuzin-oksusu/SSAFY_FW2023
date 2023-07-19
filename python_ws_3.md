# Functions
2023.07.19 (Wed)
-----

## 함수

### 함수 구조
```
def make_sum(pram1, pram 2) :
  """이것은 두 수를 받아
  두 수의 합을 반환하는 함수입니다."""
  return pram1 + pram 2
```
- 함수 정의
  - 반드시 def 키워드로 시작
  - 괄호 안에 매개변수를 정의할 수 있음
  - 매개변수는 함수에 전달되는 값을 나타냄

- 함수 body
  - 함수가 실행 될 때 수행되는 코드를 정의
  - Docstring : 함수의 설명서

- 함수 반환 값
  - 필요할 경우 사용. 반환값이 없을 수 도 있음   e.g. print()
  - return 키워드 이후 반환 값을 명시 

```
def greet(name):
  message = 'Hello, ' + name
  return message

result = greet('Alice')
print(result)
```

만약 위의 함수가 반환 값이 없다면, result에는 None이 들어감. 


## 매개변수와 인자

### Positional Arguments
```
def greet(name,age):
  print(f'안녕하세요, {name}님! {age}살이시군요.')

greet('Bob',30) #correct
greet('Bob') # wrong
```
함수 호출 시 인자의 위치에 따라 전달됨<br>
**위치인자는 함수 호출 시 반드시 값을 전달해야 함**

### Default Argument Values 
```
def greet(name,age=30):
  print(f'안녕하세요, {name}님! {age}살이시군요.')

greet('Bob') #correct
greet('Bob',45) #correct
```
함수 호출 시 인자를 전달하지 않으면 기본값이 매개변수에 할당됨

### Keyword Argument
```
def greet(name,age=30):
  print(f'안녕하세요, {name}님! {age}살이시군요.')

greet(name='Bob',age=35) #correct
greet(age=35,name='Bob') #correct
greet(age=35,'Bob') #wrong
```
함수 호출 시 인자의 이름과 함께 값을 전달하는 인자<br>
매개변수와 인자를 일치시키지 않고, 특정 매개변수에 값을 할당할 수 있음<br>
인자의 순서는 중요하지 않으며, 인자의 이름을 명시하여 전달<br>
**단, 호출 시 키워드 인자는 위치 인자 뒤에 위치해야 함**

### Arbitraty Argument Lists
```
def calculate_sum(*args):
  print(args)
  total = sum(args)
  print(f'합계: {total}')

calculate_sum(1,2,3)

# >> (1,2,3)
# >> 합계 : 6
```
정해지지 않은 개수의 인자를 처리하는 인자<br>
함수 정의 시 매개변수 앞에 '*'를 붙여 사용, 여러 개의 인자를 tuple 로 처리

### Arbitraty Keyword Arhument Lists
```
def print_info(**kwargs):
  print(kwargs)

print_info(name='coffee',calories=0)

# >> {'name':'coffee','calories': 0}
```
정해지지 않은 개수의 키워드 인자를 처리하는 인자<br>
함수 정의 시 매개변수 앞에 '**'를 붙여 사용, 여러 개의 인자를 dictionary 로 처리

### 함수 인자 권장 작성순서
**위치 *(always first)* > 기본 > 가변 > 키워드 > 가변키워드**<br>
절대적 규칙 X, 상황에 따라 조정

## 함수와 Scope
### Python의 scope
함수는 코드 내부에 local scope를 생성하며, 그 외의 공간인 global scope로 구분
- scope 
  - global scope: 코드 어디에서든 참조 가능
  - local scope : 함수가 만든 scope (함수 내부에서만 참조 가능)
- variable 
  - global variable : global scope에 정의된 변수
  - local variable : local scope에 정의된 변수
  
### 변수의 lifecycle

변수의 수명주기는 변수가 선언되는 위치와 scope에 따라 결정
1. bulit-in scope : python 실행 이후 ~ 영원히 유지
2. global scope : 모듈 호출 시점 이후 or 인터프리터가 끝날때 까지 유지
3. local scope : 함수가 호출될 때 생성, 함수 종료될 때 유지

### 이름 검색 규칙 (Name Resolution)
파이썬에서 사용되는 이름(식별자)들은 특정한 이름공간(namespace)에 저장<br>
**LEGB Rule**
1. Local Scope 
2. Enclosed Scope (중첩된 함수 영역)
3. global Scope
4. Built-in Scope : 모든 것을 담고 있는 범위

함수 내에서는 바깥 scope의 변수에 접근은 가능하나 수정은 불가
- e.g.1 
```
sum = 5 # global scope에서 built-in scope의 변수 sum을 쓰면
print(sum) # >> 5
print(sum(range(3))) 
# wrong , why? LEGB rule에 따라 global에서 먼저 sum을 찾기 때문

# sol: del sum 으로 sum 변수 삭제 후 진행 必
```
- e.g.2 (매우 지저분, 이렇게 짜지 말자)
```
 a = 1
 b = 1

 def enclosed():
    a = 10
    c = 3
    def local(c):
        print(a,b,c) 
    local(500) # >> 10 2 500
    print(a,b,c) 
enclosed() # >> 10 2 3
print(a,b) # >> 1 2
```
### 'global' 키워드
함수 내에서 전역 변수를 수정하려는 경우 global 사용 
```
num = 0

def increment():
    global num
    num += 1
```
코드 유지 보수 측면에서 파이썬에서 권장하는 사항은 아님. <br>
매개변수에 global 사용 불가
```
## wrong example

num = 0

def increment(num): 
    global num 
    num +=1
```

## 재귀 함수
함수에서 자기 자신을 호출하는 함수<br>

```
def factorial(n):
    if n == 0:
        return 1
    # 재귀 호출
    return n * factorial(n - 1)
```

- 주의사항
  - 종료 조건을 명확히
  - 반복되는 호출이 종료 조건을 향하도록 

## 유용한 함수들
### map
map(funcion, iterable) : 순회 가능한 데이터 구조의 모든 ㅇ소에 함수를 적용하고, 그 결과를 map object 로 반환
```
numbers = [1,2,3]
result = map(str, numbers)
print(list(result)) # >> ['1','2','3']

```

### zip
zip(*iterables)
임의의 iterable을 모아 튜플을 원소로 하는 zip object를 반환
```
bread =['A','B']
won =[2000, 3000]
print(zip(bread,won)) # >> <zip object at 0x000002096C2D7F00>
print(list(zip(bread,won))) # >> [('A', 2000), ('B', 3000)]
#
print(dict(zip(bread,won)))
```

## lambda 함수 
**lambda 매개변수 : 표현 식 <br>**
간단한 연산이나 함수를 한 줄로 표현할 때 사용<br>
함수를 매개변수로 전달하는 경우에도 유용하게 활용
```
# map + lambda 사용 예

num = [1,2,3,4,5] # 각각의 값을 두 배로 바꾸고 싶을 때
result =list(map(lambda x : x*2, numbers))
# >> [2,4,6,8,10]
```

## Packing
여러 개의 값을 하나의 변수에 묶어서 담는 것 <br>
변수에 담기긴 값들은 tuple 형태로 묶임
```
packed_values = 1,2,3,4,5
print(packed_values) = # >> (1,2,3,4,5)

# using *
numbers = [1,2,3,4,5]
a, *b, c = numbers

print(a) # 1
print(b) # [2,3,4]
print(c) # 5
```
*b는 남은 요소들을 리스트로 패킹하여 할당


## Unpacking
튜플이나 리스트 등의 객체의 요소들을 개별 변수에 할당<br>
*는 리스트의 요소를 언패킹<br>
**는 딕셔너리의 키-값 쌍을 함수의 키워드 인자로 언패킹<br>
```
packed_values = 1,2,3,4,5
a,b,c,d,e = packed_values
print(a, b, c, d, e) # >> 1 2 3 4 5

# using *
names = ['a','b','c']
print(*names) # >> a b c

# using **
def my_function(x,y,z):
    print(x,y,z)

my_dict = {'x':1, 'y':2 , 'z':3}
my_function(**my_dict) # >> 1 2 3
```
튜플이든 리스트든 호출 시 앞에 *을 붙이면 unpacking됨
```
def func(*args) :
    return args

print(func([1,2,3,4])) # >> ([1, 2, 3, 4],)
print(func(*[1,2,3,4])) # >> (1,2,3,4)
```
## Module
한 파일로 묶인 변수와 함수의 모음<br>
특정한 기능을 하는 코드가 작성된 python 파일<br>

## Package
관련된 모듈들을 하나의 디렉토리에 모아 놓은 것<br>
구조 예시
```
my_package
  L math
    L my_math.py
  L statstics
    L tools.py
```
이것은 패키지 3개, 모듈 2개 구조이다.

```
def add(x, y):
    return x + y

if __name__ = '__main__':
    print('main 모듈 실행')
```

## Tips
* Python에서는 함수를 변수에 저장 가능

