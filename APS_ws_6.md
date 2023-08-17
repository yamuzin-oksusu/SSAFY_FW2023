# Queue
2023.08.17(Thu)
-----
## 큐
- 특성
    - 스택과 마찬가지로 삽입과 삭제의 위치가 제한적인 자료구조 
        - 큐의 뒤에서 삽입만, 큐의 앞에서 삭제만
    - 선입선출구조(First In First Out)
        - 머리(Front) : 저장된 원소 중 첫 번째 원소 (또는 삭제된 위치)
        - 꼬리(Rear): 저장된 원소 중 마지막 원소
- 큐의 기본 연산
    - 삽입 : enQueue
    = 삭제 : deQueue
### 큐의 주요 연산

|연산|기능|
|---|---|
|enQueue(item)|큐의 뒤쪽(rear 다음)에 원소를 삽입하는 연산|
|deQueue()|큐의 앞쪽(front)에서 원소를 삭제하고 반환하는 연산|
|createQueue()|공백 상태의 큐를 생성하는 연산|
|isEmpty()|큐가 공백상태인지를 확인하는 연산|
|isFull()|큐가 포화상태인지를 확인하는 연산|
|Qpeek()|큐의 앞쪽(front)에서 원소를 삭제 없이 반환하는 연산|
## 선형 큐
1차원 배열을 이용한 큐
- 특징 
    - 큐의 크기 = 배열의 크기
    - front : 저장된 첫 번째 원소의 인덱스
    - rear : 저장된 마지막 원소의 인덱스
- 상태 표현
    - 초기 상태 : front = rear = -1
    - 공백 상태 : front == rear
    - 포화 상태 : rear == n-1 (n: 배열의 크기, n-1: 배열의 마지막 인덱스)
- 초기 공백 큐 생성
    - 크기가 n인 1차원 배열 생성
    - front와 rear를 -1로 초기화
### 큐의 구현

**enQueue , deQueue**
```
def enQ(data):
    global rear
    if rear == Qsize -1 :
        print('Q is full')
    else : 
        rear += 1
        Q[rear] = data
        print(Q)

def deQ():
    global front 
    front += 1
    return Q[front]

Qsize = 3
Q = [0] * Qsize
rear = -1
front = -1
enQ(1) # >> [1, 0, 0]
print(deQ()) # >>
```
- deQueue 사용 예
    ```
    while front != rear : #큐가 비어있지 않으면
        front += 1
        print(Q[front])
    ```
### 선형 큐 이용시의 문제점
- 잘못된 포화상태 인식
    - 선형 큐를 이용하여 원소의 삽입과 삭제를 계속할 경우, 배열의 앞부분에 활용할 수 있는 공간이 있음에도 불구하고 rear = n-1인 상태, 즉 포화상태로 인식하여 더 이상의 삽입을 수행하지 않게 됨
    - 해결방법
        1. 매 연산이 이루어질 때 마다 저장된 원소들을 배열의 앞부분으로 모두 이동시킴. 단, 원소 이동에 많은 시간이 소요되어 큐의 효율성이 급격히 떨어짐
        2. 1차원 배열을 사용하되, 원형 형태의 큐를 이룬다고 가정하고 사용

## 원형 큐
- 초기 공백 상태 : front = rear = 0
- Index의 순환 : front와 rear의 위치가 배열의 마지막 인덱스인 n-1을 가리킨 후 , 그 다음에는 논리적 순환을 이루어 배열의 처음 인덱스인 0으로 이동해야 함.
    - 이를 위해 나머지 연산자 mod(%) 를 사용함
- front 변수 : 공백 상태와 포화 상태 구분을 쉽게 하기 위해 front가 있는 자리는 사용하지 않고 항상 빈자리로 둠
**삽입 위치 및 삭제 위치**
|구분|삽입 위치|삭제 위치|
|---|---|---|
|선형큐| rear = rear + 1 | front = front + 1 |
|원형큐| rear = (rear + 1) mod(%) n | front = (front+1) mod(%) n |

### 원형 큐의 구현

**삽입 및 삭제**
```
def enQ(data):
    global rear
    if (rear+1) % cQsize == front:
        print('Full')
    else :
        rear = (rear+1) % cQsize
        cQ[rear] = data
        print(cQ)

def deQ():
    global front
    front = (front+1)%cQsize
    return cQ[front]

cQsize = 4
cQ = [0] * cQsize
front = 0
rear = 0

enQ(1) # [0, 1, 0, 0]
enQ(2) # [0, 1, 2, 0]
enQ(3) # [0, 1, 2, 3]
enQ(4) # Full

print(deQ()) # 1
print(deQ()) # 2
print(cQ , front, rear) # [0, 1, 2, 3] , 2, 3
```
- 꽉 찼을 때 밀고 나가면서 저장하려면?
```
def enQ(data):
    global rear
    global front
    if (rear+1) % cQsize == front: # Full 일때
        front = (front+1)%cQsize # front의 위치 조정 > deQ()시 선입선출 가능함.

    rear = (rear+1) % cQsize
    cQ[rear] = data
    print(cQ)

cQsize = 4
cQ = [0] * cQsize
front = 0
rear = 0

enQ(1) # [0, 1, 0, 0]
enQ(2) # [0, 1, 2, 0]
enQ(3) # [0, 1, 2, 3]
enQ(4) # [4, 1, 2, 3]

```
**공백상태 및 포화상태 검사**
- 공백상태 : front == rear
- 포화상태 : 삽입할 rear의 다음 위치 == 현재 front 
    - (rear + 1) mod n == front

## 우선순위 큐
- 우선순위를 가진 항목들을 저장하는 큐
- FIFO 순서가 아니라 우선순위가 높은 순서대로 먼저 나가게 됨
### 배열을 이용한 우선순위 큐 구현
- 배열을 이용하여 자료 저장
- 원소를 삽입하는 과정에서 우선순위를 비교하여 적절한 위치에 삽입하는 구조
- 가장 앞에 최고 우선순위의 원소가 위치하게 됨
### 문제점
- 배열을 사용하므로, 삽입이나 삭제 연산이 일어날 때 원소의 재배치가 발생함
## 큐의 활용 : 버퍼
데이터를 한 곳에서 다른 한곳으로 전송하는 동안 일시적으로 그 데이터를 보관하는 메모리의 영역
- 버퍼의 자료 구조
    - 순서대로 입력, 출력, 전달 되어야 하므로 FIFO 방식의 자료구조인 큐가 활용됨

## BFS

## BFS 예제