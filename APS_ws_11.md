# Stack 2
2023.08.14(Mon)
----
## 계산기 1
문자열로 된 계산식이 주어질 때, 스택을 이용하여 이 계산식의 값을 계산할 수 있다.

- 중위 표기법(infix notation) : 연산자를 피연산자의 가운데에 표기
- 후위 표기법(postfix notation) : 연산자를 피연산자 뒤에 표기

- 문자열 수식 계산의 일반적인 방법
    1. 중위표기법의 수식을 후위 표기법으로 변경한다.(스택 이용)
    2. 후위 표기법의 수식을 스택을 이용해 계산한다.

### step 1. 중위 표기법의 수식을 후위 표기법으로 변환

```
'''
(6+5*(2-8)/2)
'''
stack = [0] * 100
top = -1
icp = {'(': 3, '*': 2, '/':2, '+': 1, '-' : 1}
isp = {'(': 0, '*': 2, '/':2, '+': 1, '-' : 1}

fx = '(6+5*(2-8)/2)'
s = ''
for x in fx :
    if x not in '(+-*/)' : 
        s += x
    elif x == ')' :
        while stack[top] != '(':
            s += stack[top]
            top -= 1
        top -= 1
    else :
         if top == -1 or isp[stack[top]] < icp[x]:
            top += 1
            stack[top] = x
        elif isp[stack[top]] >= icp[x]:
            while top > -1 and isp[stack[top]] >= icp[x] :
                s += stack[top]
                top -= 1
            top += 1
            stack[top] =x

print(s)
```

## 계산기 2

### step 2. 후위 표기법의 수식을 스택을 이용하여 계산

```
stack = [0] * 100
top = -1
s = '6528-*2/+'
for x in s :
    if x not in '+-/*':
        top += 1
        stack[top] = int(x)
    else :
        op2 = stack[top]
        top -= 1
        op1 = stack[top]
        top -= 1
        if x == '+' :
            top += 1
            stack[top] = op1 + op2
        elif x == '-':
            top += 1
            stack[top] = op1 - op2
        elif x == '/' :
            top += 1
            stack[top] = op1 // op2
        elif x == '*' :
            top += 1
            stack[top] = op1 *op2
print(stack[top])
```
## 백트래킹
해를 찾는 도중에 '막히면' 되돌아가서 다시 해를 찾아 가는 기법
optimization 문제와 decision 문제를 해결할 수 있다.
- decision(결정) 문제 : 문제의 조건을 만족하는 해가 존재하는지의 여부를 Yes/No로 답하는 문제
    - 미로 찾기
    - n-Queen 문제
    - Map coloring
    - 부분 집합의 합(Subset Sum)문제 등

- 백트래킹과 깊이우선탐색과의 차이
    - 어떤 노드에서 출발하는 경로가 해결책으로 이어질 것 같지 않으면 더 이상 그 경로를 따라가지 않음으로써 시도의 횟수를 줄임(Prunning 가지치기)
    - 깊이우선탐색이 모든 경로를 추적하는데 비해 백트래킹은 불필요한 경로를 조기에 차단
    - 깊이 우선 탐색을 가하기에는 경우의 수가 너무 많음. 즉 N! 가지의 경우의 수를 가진 문제에 대해 깊이우선탐색을 가하면 당연히 처리 불가능한 문제
    - 백트래킹 알고리즘을 적용하면 일반적으로 경우의 수가 줄어들지만 이 역시 최악의 경우 여전히 지수함수 시간(Exponential Time)을 요하므로 처리 불가능
- 모든 후보를 검사하지 않음
- 백트래킹 기법
    - 어떤 노드의 유망성을 점검한 후에 유망(promising)하지 않다고 결정되면 그 노드의 부모로 되돌아가(backtracking)다음 자식 노드로 감
    - 어떤 노드를 방문하였을 때 그 노드를 포함한 경로가 해답이 될 수 없으면 그 노드는 유망하지 않다고 하며, 반대로 해답의 가능성이 있으면 유망하다고 한다.
    - 가지치기(pruning): 유망하지 않은 노드가 포함되는 경로는 더 이상 고려하지 않는다.
- 백트래킹 알고리즘의 진행 절차
    1. 상태 공간 트리의 깊이 우선 검색을 실시한다.
    2. 각 노드가 유망한지를 점검한다.
    3. 만일 그 노드가 유망하지 않으면 그 노드의 부모 노드로 돌아가서 검색을 계속한다.

### 일반 백트래킹 
```
def checknode(v) : # node
    if promising(v) :
        if there is a solution at v :
            write the solution
        else :
            for u in each child of v :
                checknode(u)
```


## 부분집합, 순열

### 재귀적 접근
```
def f(i,N) :
    if i == N:
        return
    else :
        B[i] = A[i]
        f(i+1,N)
        return

N = 3
A = [1,2,3]
B = [0] * N

f(0, N)
print(B) # >> [1,2,3]
```

### 재귀 호출을 기반으로 한 부분집합 구현
- 부분집합 출력하기
```
def f(i, N):
    if i==N :
        '''
        print(bit) 할 경우
        [1, 1, 1]
        [1, 1, 0]
        [1, 0, 1]
        [1, 0, 0]
        [0, 1, 1]
        [0, 1, 0]
        [0, 0, 1]
        [0, 0, 0]
        '''
        for j in range(N):
            if bit[j] :
                print(A[j], end = ' ')
        print() # enter 역할
        '''
        1 2 3 
        1 2 
        1 3 
        1 
        2 3 
        2 
        3 
        '''
        return
    else :
        bit[i] = 1
        f(i+1,N)
        bit[i] = 0
        f(i+1, N)
        return
A = [1,2,3]
bit = [0]*3
f(0,3)
```
- 부분집합의 합을 구해보자!
```
def f(i, N):
    if i==N :
        s = 0
        for j in range(N):
            if bit[j] :
                s += A[j]
                print(A[j], end= ' ')
        print(f' : {s}')
        '''
        1 2 3  : 6
        1 2  : 3
        1 3  : 4
        1  : 1
        2 3  : 5
        2  : 2
        3  : 3
        : 0
        '''
        return
    else :
        bit[i] = 1
        f(i+1,N)
        bit[i] = 0
        f(i+1, N)
        return
A = [1,2,3]
bit = [0]*3
f(0,3)
```
- s: i-1원소까지 부분집합의 합
```
def f(i, N, s):
    if i==N :
        print(bit, end = ' ')
        print(f' : {s}')
        '''
        [1, 1, 1]  : 6
        [1, 1, 0]  : 3
        [1, 0, 1]  : 4
        [1, 0, 0]  : 1
        [0, 1, 1]  : 5
        [0, 1, 0]  : 2
        [0, 0, 1]  : 3
        [0, 0, 0]  : 0
        '''
        return
    else :
        bit[i] = 1 # 부분집합에 A[i] 포함 
        f(i+1,N, s+A[i])
        bit[i] = 0 # 부분집합에 A[i] 미포함
        f(i+1, N, s)
        return
A = [1,2,3]
bit = [0]*3
f(0,3,0)
```

- 연습문제 : {1,2,3,4,5,6,7,8,9,10}의 powerset중 원소의 합이 10인 부분집합을 구하시오
```
def f(i, N, s):
    if i==N :
        if s == 10 :
            print(bit)
        '''
        [1, 1, 1, 1, 0, 0, 0, 0, 0, 0]
        [1, 1, 0, 0, 0, 0, 1, 0, 0, 0]
        [1, 0, 1, 0, 0, 1, 0, 0, 0, 0]
        [1, 0, 0, 1, 1, 0, 0, 0, 0, 0]
        [1, 0, 0, 0, 0, 0, 0, 0, 1, 0]
        [0, 1, 1, 0, 1, 0, 0, 0, 0, 0]
        [0, 1, 0, 0, 0, 0, 0, 1, 0, 0]
        [0, 0, 1, 0, 0, 0, 1, 0, 0, 0]
        [0, 0, 0, 1, 0, 1, 0, 0, 0, 0]
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 1]
        '''
        return
    else :
        bit[i] = 1 # 부분집합에 A[i] 포함
        f(i+1,N, s+A[i])
        bit[i] = 0 # 부분집합에 A[i] 미포함
        f(i+1, N, s)
        return

N = 10
A = [i for i in range(1,N+1)]
bit = [0]*N
f(0,N,0)
```

- 찾으려는 합 t가 주어질 떄
    ```
    def f(i, N, s , t):
        global cnt
        cnt += 1
        if s == t:
            print(bit)
            '''
            [1, 1, 1, 1, 0, 0, 0, 0, 0, 0]
            [1, 1, 0, 0, 0, 0, 1, 0, 0, 0]
            [1, 0, 1, 0, 0, 1, 0, 0, 0, 0]
            [1, 0, 0, 1, 1, 0, 0, 0, 0, 0]
            [1, 0, 0, 0, 0, 0, 0, 0, 1, 0]
            [0, 1, 1, 0, 1, 0, 0, 0, 0, 0]
            [0, 1, 0, 0, 0, 0, 0, 1, 0, 0]
            [0, 0, 1, 0, 0, 0, 1, 0, 0, 0]
            [0, 0, 0, 1, 0, 1, 0, 0, 0, 0]
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 1]
            '''
        elif i == N :
            return
        elif s > t :
            return
        else :
            bit[i] = 1 # 부분집합에 A[i] 포함
            f(i+1,N, s+A[i])
            bit[i] = 0 # 부분집합에 A[i] 미포함
            f(i+1, N, s)
            return

    N = 10
    A = [i for i in range(1,N+1)]
    bit = [0]*N
    cnt = 0
    f(0,N,0,10)
    print(cnt) # >> 349
    ```
    - 이 경우 t가 얼마인지에 따라 백트래킹이 가능해진다 (재귀 호출 수가 줄어듦)
    - 만약 t == 55라면 ? 똑같이 1047번을 돌 것

### 순열
```
def f(i, N):
    if i==N: # 순열 완성
        print(A)
    else:
        for j in range(i,N): #자신부터 오른쪽 끝까지
            A[i], A[j] = A[j], A[i]
            f(i+1, N)
            A[i], A[j] = A[j], A[i]


A = [0,1,2]
f(0,3)
```

## 분할정복
둘 이상의 부분 문제로 나눈 뒤, 각 문제에 대한 답을 재귀 호출을 이용해 계산하고 각 부분 문제의 답으로부터 전체 문제의 답을 계산 ([참고](https://velog.io/@turtle601/%EB%B6%84%ED%95%A0%EC%A0%95%EB%B3%B5))

- 거의 같은 크기의 부분 문제로 나눈다는 것에 있어서 일반 재귀 호출과 차이가 있음

- 설계 전략
    - 분할 : 해결할 문제를 여러 개의 작은 부분으로 나눈다.
    - 정복 : 나눈 작은 문제를 각각 해결한다.
    - 통합 : (필요하다면) 해결된 해답을 모은다.

- 거듭제곱(Exponentation)
    - O(n)
    ```
    def Power(Base , Exponent):
        if Base == 0 :
            return 1
        result = 1 # Base^0 은 1이므로
        for i in range(Exponent):
            result *= Base
        return result
    ```
    - 분할정복 기반 알고리즘 : O(log<sub>2</sub>n)
        - C<sup>n</sup> = C<sup>n/2</sup> * C<sup>n/2</sup> (if n이 짝수일 때), C<sup>(n-1)/2</sup> * C<sup>(n-1)/2</sup> * C (else)
    ```
    def Power(Base, Exponent):
        if Exponent == 0 or Base == 0 :
            return 1
        if Exponent %2 == 0 : #짝수면
            NewBase = Power(Base, Exponent/2)
            return NewBase * NewBase
        else : 
            NewBase = Power(Base,(Exponent-1)/2)
            return (NewBase * NewBase) * Base
    ```

### 퀵 정렬
```
def quickSort(a, begin, end):
    if begin < end :
        p = partition(a,begin, end)
        quickSort(a, begin, p-1)
        quickSort(a, p+1, end)
```


**알고리즘 특성 비교**

|알고리즘|평균 수행시간|최악 수행시간|알고리즘 기법|비고|
|---|---|---|---|---|
|버블 정렬|O(n<sup>2</sup>)|O(n<sup>2</sup>)|비교와 교환|코딩이 가장 손쉽다.|
|카운팅 정렬|O(n+k)|O(n+k)|비교환 방식|n이 비교적 작을 때만 가능하다.|
|선택 정렬|O(n<sup>2</sup>)|O(n<sup>2</sup>)|비교와 교환|교환의 횟수가 버블, 삽입 정렬보다 작다.|
|퀵 정렬|O(nlogn)|O(n<sup>2</sup>)|분할 정복|최악의 경우 O(n<sup>2</sup>)이지만, 평균적으로 가장 빠르다|