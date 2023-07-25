# Data Structure (2)

2023.07.24(Tue)
-----
## 비시퀀스 데이터 구조
### set
고유한 항목들의 정렬되지 않은 컬렉션
### 세트 메서드
- s.add(X) : 세트에 항목 x를 추가. 이미 x가 있다면 변화 없음
- s.clear() : 세트의 모든 항목 제거
- s.remove(x) : 세트의 항목 x를 제거. 이미 없다면 Key error
- s.pop() : 세트에서 랜덤하게 항목을 반환하고, 해당 항목 제거
- s.discard(x) : 세트에서 항목 x를 제거
- s.update(iterable) : 세트에 다른 iterable요소 추가
```
my_set = {1, 2, 3}
my_set.add(4)
print(my_set) # >> {1, 2, 3, 4}
my_set.clear()
print(my_set) # >> set()
my_set = {1, 2, 3}
my_set.remove(10) # KeyError
my_set.discard(10)
``` 
세트에서 항목을 제거할때, discard는 remove와 달리 없는 항목을 제거해도 error 없음

```
my_set = {1, 2, 3}
element = my_set.pop()
print(element) # >> 1
print(my_set) # >> {2, 3}

my_set.update([2, 4, 5])
print(my_set) # >> {2, 3, 4, 5}
```
pop은 set에서 **임의의 요소를 제거하고 반환**

### Hash
- **Hash Table**
  - 데이터를 효율적으로 저자하고 검색하기 위해 사용되는 자료 구조
  - 키-값 쌍을 연결하여 저장하는 방식
  - 키를 해시 함수를 통해 해시 값으로 변환하고, 이 해시 값을 인덱스로 사용하여 데이터를 저장하거나 검색함
    - Why? 데이터의 검색 속도 향상
  - 파이썬에서 세트의 요소와 딕셔너리의 키는 해시 테이블을 이용하여 중복되지 않는 고유한 값을 저장
  - 세트 내의 각 요소는 해시 함수를 통해 해시 값으로 변환되고, 이 해시 값을 기반으로 해시 테이블에 저장됨
  - 마찬가지로 딕셔너리의 키는 고유해야 하므로, 키를 해시 함수를 통해 해시 값으로 반환하여 해시 테이블에 저장
  - 따라서 세트와 딕셔너리의 키는 매우 빠른 탐색 속도를 제공하며, 중복된 값을 허용하지 않음

- **Hash**
  - 임의의 크기를 가진 데이터를 고정된 크기의 고유한 값으로 변환하는 것
  - 이렇게 생성된 고유한 값은 해당 데이터를 식별하는데 사용될 수 있음
  - 일종의 '지문'과 같은 역할
  - 지문은 개인을 고유하게 식별하는 것처럼, 해시 값은 데이터를 고유하게 식별
  - 파이썬에서는 해시 함수를 사용하여 데이터를 해시 값으로 변환하며, 이 해시 값은 정수로 표현됨
  ```
  # 정수

  my_set = {1, 2, 3, 9, 100, 4, 87, 39, 10, 52}

  print(my_set.pop())
  print(my_set.pop())
  print(my_set.pop())
  print(my_set.pop())
  print(my_set.pop())
  print(my_set.pop())
  print(my_set.pop())
  print(my_set.pop())
  print(my_set.pop())
  print(my_set.pop())
  print(my_set)
  ```
  - 정수 값 자체가 곧 해시 값

  ```
  # 문자열

  my_str_set = {'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j'}

  print(my_str_set.pop())
  print(my_str_set.pop())
  print(my_str_set.pop())
  print(my_str_set.pop())
  print(my_str_set.pop())
  ```
  - 문자열의 경우 반환 값이 매번 다름
  ```
  print(hash(1))  # 1
  print(hash(1))  # 1
  print(hash('a'))  # 실행시마다 다름
  print(hash('a'))  # 실행시마다 다름
  ```
  - 파이썬에서 해시 함수의 동작 방식은 객체의 타입에 따라 달라짐
  - 정수와 문자열은 서로 다른 타입이며, 이들의 해시 값을 계산하는 방식도 다름
  - 정수 타입의 경우, 정수 값 자체가 곧 해시 값
    - 같은 정수는 항상 같은 해시 값을 가짐
    - 해시 테이블에 정수를 저장할 때 효율적인 방법
    - e.g. hash(1)과 hash(2)는 항상 서로 다른 해시 값을 갖지만, hash(1)은 항상 동일한 해시 값을 갖게 됨.
  - 반면에 문자열은 가변적인 길이를 갖고 있고, 문자열에 포함된 각 문자들의 유니코드 코드 포인트 등을 기반으로 해시 값을 계산
    - 이로 인해 문자열의 해시 값은 문자열의 내용에 따라 다르게 계산됨
- **해시 함수**
  - 주어진 객체의 해시 값을 계산하는 함수
  - 해시 값은 객체의 고유한 식별자로 사용될 수 있으며, 해시 테이블과 같은 자료 구조에서 빠른 검색을 위해 사용됨
  ```
  # TypeError: unhashable type: 'list'
  my_set = {[1, 2, 3], 1, 2, 3, 4, 5}
  # TypeError: unhashable type: 'list
  my_dict = {[1, 2, 3]: 'a'}
  ```
  - `hasha` 는 객체를 딕셔너리 키나 세트의 요소로 사용할 수 있게 함
  - list 가 딕셔너리의 키나 세트의 요소로 사용될 수 없는 이유는 이들을 고유한 식별자로 사용할 수 없기 때문이다. 즉, 내부적으로 해시가능성이 없기 때문


### 세트의 집합 메서드
|메서드|설명|연산자|
|---|---|----|
| **set1.difference(set1)** | set1에 대한 set2dml 차집합 | set1 - set2 |
| **set1.intersection(set2)** | set1과 set2 의 교집합 | set1 & set2 |
| **set1.issubset(set2)** | set1이 set2의 부분집합이면 True | set1 <= set2 |
| **set1.issuperset(set2)** | set2가 set1의 부분집합이면 True | set1 >= set2 |
| **set1.union(set2)** | set1과 set2의 합집합 | set1 \| set2 |

### 딕셔너리 메서드
- D.clear() : 딕셔너리의 모든 키/값 쌍을 제거
- D.get(k) : 키 K에 연결된 값을 반환 (키가 없으면 None)
- D.get(k,v) : 키 k에 연결된 값을 반환 (키가 없으면 v 반환)
- D.keys() : 딕셔너리의 키를 모은 객체 반환
- D.values() : 딕셔너리의 값을 모은 객체 반환
- D.items() : 딕셔너리의 키/값 쌍을 모은 객체 반환
- D.pop(k) : 딕셔너리에서 키를 제거하고 연결되었던 값을 반환 (없으면 오류)
- D.pop(k,v) : 딕셔너리에서 키 k를 제거하고 연결되었던 값을 반환 (없으면 v 반환)
- D.setdefault(k) : 딕셔너리에서 키 k와 연결된 값을 반환
- D.setdefault(k,v) : 딕셔너리에서 키 k와 연결된 값을 반환 (k가 D의 키가 아니라면 값 v와 연결한 키 k를 D에 추가 후 v 반환)
- D.updatd(other) : other 내 각 키에 대해 D에 있는 키면 D에 있는 그 키의 값을 other에 있는 값으로 대체. other에 있는 각 키에 대해 D에 없는 키면 키/값 쌍을 D에 추가
```
# 찾고자 하는 키가 없을때
print(my_dict['age'])
print(my_dic.get('age')) # >> None
print(my_dict.get('age','unknown')) # >>unknown
```
찾고자 하는 키가 없을때 get을 사용하면 error가 아닌 None 이 출력
```
person = {'name' : 'Alice' , 'age' : 25}
print(person.pop('age')) # 25
print(person) # {'name': 'Alice'}
print(person.pop('country', None)) # >> None
print(person.pop('country')) # >> KeyError
```
없는 key를 입력하면 default 값이나 KeyError 반환 (default 값 설정 필요)
```
person = {'name' : 'Alice' , 'age' : 25}

print(person.setdefault('country','KOREA')) # >> KOREA
print(person) # >> person = {'name' : 'Alice' , 'age' : 25 , 'country','KOREA'}
```
**setdefault는 pop과 달리 키가 없을때 연결한 key와 default 값을 딕셔너리에 추가하고 default 값 반환**
```
person = {'name' : 'Alice' , 'age' : 25}
other_person = {'name' : 'Alice' , 'gender': 'F'}

person.update(other_person) = {'name' : 'Alice' , 'age' : 25 , 'gender' : 'F'}
```
update 시 기존 key는 덮어씀
```
# [], get(), setdefault() 사용한 bloodtype counting 문제 풀이

```

## 복사
파이썬에서는 데이터의 분류에 따라 복사가 달라짐
### 할당 (Assignment)
- 할당 연산자(=)를 통한 복사는 해당 객체에 대한 객체 참조를 복사

### 얕은 복사 (Shallow copy)
- Slicing 을 통해 생성된 객체는 원본 객체와 독립적으로 존재
- copy를 이용해 shallow copy 가능
```
a = [1, 2, 3]
b = a[:]
b[0] = 1000
print(a, b) # >> [1, 2, 3] [100, 2, 3]

# copy
import copy
c = a.copy()
c[0] = 100
print(a, c) # >> [1, 2, 3] [100, 2, 3]

# limitation
a = [1, 2, [1, 2]]
b = a[:]
b[2][0] = 999
print(a, b) # >> [1, 2, [999, 2]] [1, 2, [999, 2]]
```
a와 b의 주소는 다르지만 내부 객체의 주소가 같기 때문에 변경가능한 객체 안의 변경 가능한 객체는 함께 변경됨

### 깊은 복사 (Deep copy) 
```
import copy
a = [1, 2, [1, 2]]
c = copy.deepcopy(a)
c[2][0] = 100
print(a, c) # >> [1, 2, [1, 2]] [1, 2, [999, 2]]
```
copy.deepcopy 사용 시 내부에 중첩된 모든 객체까지 새로운 객체 주소 참조하도록 함.