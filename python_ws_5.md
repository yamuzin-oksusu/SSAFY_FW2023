# Data Structure
2023.07.24(Mon)
-----

## Data Structure
정의 : 여러 데이터를 효과적으로 사용, 관리하기 위한 구조 (str,list,dict 등)
### 자료 구조
- 각 데이터의 효율적인 저장, 관리를 위한 구조를 나눠놓은 것

## 메서드
객체에 속한 함수 -> 객채의 상태를 조작하거나 동작을 수행
- 특징
  - 매서드는 class 내부에 정의되ㅣ는 함수
  - 클래스는 파이썬에서 '타입을 표현하는 방법'이며 이미 은연중에 사용해왔음
  - 예를들어 help함수를 통해 str을 호출해보면 class 였다는 것을 확인 가능
- **메서드는 어딘가(class)에 속해있는 함수이며, 각 데이터 타입 별로 다양한 기능을 가진 메서드가 존재**
```
# 문자열 메서드 예시
print('hello'.capitalize()) # >> Hello

#리스트 메서드 예시
numbers = [1,2,3]
numbers.append(4)

print(numbers) # >>[1,2,3,4]

```

## 시퀀스 데이터 구조
Sequence Types: 여러 개의 값들을 순서대로 나열하여 저장하는 자료형(str,list,tuple,range)

### sequence Types 특징
-  Sequence : 값들이 순서대로 저장(정렬 x)
-  Indexing : 각 값에 고유한 인덱스를 가지고 있으며, 인덱스를 사용하여 특정 위치의 값을 선택하거나 수정 가능
-  Slicing : 인덱스 범위를 조절해 부분적인 값을 추출 가능
-  Length : len()함수 사용 가능
-  Iteration : 반복문 사용 가능

## 문자열
### 문자열 조회/탐색 및 검증 메서드
- s.find(x) : x의 첫번째 위치를 반환. 없으면 -1 반환
- s.index(x) : x의 첫번째 위치를 반환. 없으면 오류 발생
- s.isalpha() : 알파벳 문자 여부 (단순 알파벳이 아닌 유니코드 상 letter)
- s.isupper() : 문자열이 모두 대문자로 이루어져 있는지 확인
- s.islower() : 문자열이 모두 소문자로 이루어져 있는지 확인
- s.istitle() : 타이틀 형식 여부

```
print('banana'.find('a')) # >> 1
print('banana'.find('z')) # >> -1
print('banana'.index('a')) # >> 1
print('banana'.index('z')) # >> ValueError
```
find 와 index는 값이 없을 때의 output이 다름

```
string1 = 'HELLO'
string2 = 'Hello'

print(string1.isupper()) # True
print(string2.isupper()) # False
```
문자열 중 한 문자라도 대문자/소문자가 아니면 False

```
string1 = 'HELLO'
string2 = '123'
string3 = '안녕'

print(string1.isalpha()) # True
print(string2.isalpha()) # False
print(string3.isalpha()) # True
```
unicode 상 letter 이면 True

### 문자열 조작 메서드
- s.replace(old,new[,count]) : 문자를 새로운 글자로 변환
- s.strip([chars]) : 공백이나 특정 문자를 제거
- s.split(sep=None,maxsplit=1) : 공백이나 특정 문자를 기준으로 분리
- 'seterater'.joing(iterable) : 구분자로 itereable을 합침 
- s.capitalize() : 가장 첫 글자를 대문자로 변경
- s.title()
-  : 문자열 내 띄어쓰기 기준으로 각 단어의 첫 글자는 대문자로, 나머지는 소문자로 변환
-  s.upper() : 모두 대문자로 변경
-  s.lower() : 모두 소문자로 변경
-  s.swapcase() : 대문자와 소문자 서로 변경

```
text = 'Hello, world!'
new_text = text.replace('world','minjoo')
print(new_text) # >> Hello,minjoo

text = '   Hello, world!   '
new_text = text.strip()
print(new_text) # >> Hello, world!

text = 'Hello, world!'
words = text.split(',')
print(words) # >> ['Hello','World!']

words = ['Hello','World!']
text = "-".join(words)
print(text) # >> 'Hello-world!'

text = 'heLLo, woRld!'

new_text1 = text.capitalize()
new_text2 = text.title()
new_text3 = text.upper()
new_text4 = text.swapcase()

print(new_text1) # >> Hello, world!
print(new_text2) # >> Hello, World!
print(new_text3) # >> HELLO, WORLD!
print(new_text4) # >> HEllO, WOrLD!
```
- 메서드는 이어서 사용 가능
  - e.g. text.swapcase().replace(',' '-')   # 가능!


## 리스트 
### 리스트 값 추가 및 삭제 메서드
- L.append(x) : 리스트 마지막에 항목x를 추가
- L.extend(m) : iterable m의 모든 항목들을 리스트 끝에 추가(+=과 같은 기능)
- L.insert(i,x) : 리스트 인덱스 i에 항목 x를 삽입
- L.remove(x) : 리스트 첫번째 x를 제거
- L.pop(*i*) : 리스트 마지막을 **반환** 후 제거
- L.clear() : 리스트의 모든 항목 삭제

```
numbers = [1,2,3]
numbers2 = [4,5,6]

print(numbers.append(numbers2)) # None
numbers.append(numbers2)
print(numbers) # >> [1,2,3,[4,5,6]]

numbers = [1,2,3]
numbers.extend(numners2)
print(numbers) # >> [1,2,3,4,5,6]

numbers = [1,2,3]
numbers.insert(1,5)
print(numbers) # >> [1,5,2,3]

numbers.remove(5)
print(numbers) # >> [1,2,3]

my_list = [1,2,3,4,5]
item1 = my_list.pop()
item2 = my_list.pop(0)

print(item1) # >> 5
print(item2) # >> 1
print(my_list) # >> [2,3,4]
```
pop 함수 사용 시, **제거한 항목을 할당할 수 있다.**

### 리스트 탐색 및 정렬 메서드
- L.index(x,start,end) : 리스트에 있는 항목 중 첫번째로 일치하는 항목 x의 **인덱스를 반환**
- L.reverse(): 리스트를 거꾸로 정렬
- L.sort() : 리스트를 정렬
- L.count(x) : 리스트에서 항목 x의 개수를 반환

```
my_list = [1,2,3]
index = my_list.index(2)
print(index) # >> 1 

my_list = [1,2,3,3,3]
count = my_list.count(3)
print(count) # >> 3
```
L.index(x)는 항목 x의 인덱스를 반환함 (항목 x자체가 아님)

```
my_list = [3,2,1]
my_list.sort()
print(my_list) # >> [1,2,3]

my_list.sort(reverse=True)
print(my_list) # >> [3,2,1]

my_list = [1,5,2,3]
my_list.reverse()
print(my_list) # >> [3,2,5,1]
```
reverse 는 리스트의 순서를 역순으로 변경할 뿐, 정렬하지 않는다

```
numbers = [3,2,1]
print(numbers.sort()) #None
sorted(numbers) # >> [1,2,3]
```