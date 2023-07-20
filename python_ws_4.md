# Control of flow
2023.07.20 (Thu)
-----

## 조건문
주어진 조건식을 평가하여 해당 조건이 참(T)인 경우에만 코드 블록을 실행하거나 건너뜀 <br>
복수 조건문은 조건식을 동시에 검사하는 것이 아니라 순차적으로 비교

## Loop Statement

### for
임의의 시퀀스 항목들을 그 시퀀스에 들어있는 순서대로 반복 <br>
itarable한 항목 : sequence, dict , set ,etc.
- 중첩된 반복문

```
outers = ['A','B']
inners = ['c','d']
for outer in outers:
    for inner in inners:
        print(outer,inner)

# >> A c
# >> A d
# >> B c
# >> B d

```
print가 호출되는 횟수 : len(outers) * len(inners) <br>
- 중첩 리스트 순회

```
elements = [['A','B'],['c','d']]

for elem in elements: 
    for item in elem :
        print(item)

# >> A 
# >> B
# >> c
# >> d
```
안쪽 리스트 요소에 접근하려면 바깥 리스트를 순회하면서 중첩 반복을 사용해 각 안쪽 반복을 순회

### while
주어진 조건식이 거짓(F)이 될 때 까지 코드를 반복해서 실행<br>
**while 문은 반드시 종료 조건이 필요**
```
number = int(input('양의 정수를 입력해주세요 : '))
while number <= 0 :
    if number < 0 :
        print('음수를 입력했습니다.')
    else : 
        print('0은 양의 정수가 아닙니다.')
    number = int(input('양의 정수를 입력해주세요 : '))

print('good job!')
```
반복 횟수가 불명확하거나 조건에 따라 반복을 종료해야 할 때 유용 <br>
e.g. 사용자의 입력을 받아서 특정 조건이 충족될 때까지 반복하는 경우

### 반복 제어
일부의 반복문만 실행이 필요할 때, **break**나 **continue**를 사용<br>
- break : 반복 즉시 중지
- continue : 다음 반복으로 건너뜀
```
## break 

while number <= 0 :
    if number == -9999:
        print('프로그램을 종료합니다.')
        break
    if number < 0 :
        print('음수를 입력했습니다.')
    else : 
        print('0은 양의 정수가 아닙니다.')
    number = int(input('양의 정수를 입력해주세요 : '))\
print('good job!')


## continue
numbers = [1,2,3,4,5,6,7]

for num in numbers :
    if num % 2 == 0:
        continue
    print(num)
```

### List Comprehension
간결하고 효율적인 리스트 생성법 <br>
- 구조
  - list(expression for 변수 in iterable)
  - [expression for 변수 in iterable]


```
numbers = [1, 2, 3, 4, 5]

## To-Be
squared_numers = [num**2 for num in numbers]

## As-Is
squared_numers = []
for i in range(numbers):
    num = i**2 
    square_numbers.append(num)

print(square_numbers) # >> [1, 4, 9, 16, 25]
```
- List Comprehension + if
  - list(expression for 변수 in iterable if 조건식)
  - [expression for 변수 in iterable if 조건식] 

```
result = [ i for i in range(10) if i % 2 == 1]
```

### 참고
- pass
  - 아무런 동작도 수행하지 않고 넘어가는 역할
  - 문법적으로 필요하지만 프로그램 실행에는 영향을 주지 않아야 할때 사용
  - 사용 예
    - 코드 작성 중 미완성한 부분
    - 조건문에서 아무런 동작을 수행하지 않아야 할 때
    -  무한루프에서 조건이 충족되지 않을때 pass를 사용하여 루프를 계속 진행
<br>
<br>
- enumerate 
  - enumerate(iterable, start = 0)
  - iterable 객체의 각 요소에 대해 인덱스와 함께 반환하는 내장함수

```
fruits = ['a','b','c']
for idx , name in enumerate(fruits):
    print(f'{index + 1}번째 과일은 {}이다.')

# >> 1번째 과일은 a이다.
# >> 2번째 과일은 b이다.
# >> 3번째 과일은 c이다.
```
