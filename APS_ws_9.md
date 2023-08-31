# 완전 검색 & 그리디
2023.08.30(Wed) ~ 2023.08.31(Thu)
----
## 반복(Iteration)과 재귀(Recursion)
### 반복과 재귀
- 반복과 재귀는 유사한 작업을 수행할 수 있음
- 반복 : 수행하는 작업이 완료될때 까지 계속 반복 
  - 루프(for, while)로 구현
- 재귀는 주어진 문제의 해를 구하기 위해 동일하면서 더 작은 문제의 해를 이용하는 방법
  - 하나의 큰 문제를 해결할 수 있는(해결하기 쉬운) 더 작은 문제로 쪼개고 결과들을 결합한다
  - 재귀함수로 구현
### 반복구조
- 초기화
  - 반복되는 명령문을 실행하기 전에 (한번만) 조건 검사에 사용할 변수의 초기값 설정
- 조건검사(check control expression)
- 반복할 명령문 실행(action)
- 업데이트(loop update)
  - 무한루프가 되지 않게 조건이 거짓이 되게 한다.
- 반복을 이용한 선택정렬
    ```
    def SelectionSort(A):
        n = len(A)
        for i in range(n-1):
            minI = i
            for j in range(i+1,n):
                if A[j] < A[minI]:
                    minI = j
            A[minI] , A[i] = A[i], A[minI]
    ```
### 재귀적 알고리즘
- 재귀적 정의는 두 부분으로 나뉨
- 하나 또는 그 이상의 기본 경우(basis case or rule)
  - 집합에 포함되어있는 원소로 induction을 생성하기 위한 seed역할
- 하나 또는 그 이상의 유도된 경우(icductive case or rule)
  - 새로운 집합의 원소를 생성하기 위해 결합되어지는 방법

## 재귀 함수
- 함수 내부에서 직간접적으로 자기 자신을 호출하는 함수
- 일반적으로 재귀적 정의를 이용해서 재귀 함수를 구현함
- 따라서, 기본 부분(basis part)와 유도부분(inductive part)로 구성됨
- 함수 호출은 프로그램 메모리 구조에서 스택을 사용한다. 따라서 재귀 호출은 반복적인 스택의 사용을 의미하며 메모리 및 속도에서 성능 저하가 발생 -> **입력 값 n이 커질수록 재귀 알고리즘은 반복에 비해 비효율적일 수 있음**
- 재귀 함수 예시
    ```
    def f(i, N, key, arr):
        if i == N:
            return 0 # key가 없는 경우
        elif arr[i] == key:
            return 1
        else :
            return f(i+1, N, key, arr)

    N = 5
    A = [1,2,3,4,5]
    key = 10
    print(f(0,N,key,A))

    ```

|특징|재귀|반복|
|---|---|---|
|종료|재귀 함수 호출이 종료되는 base case|반복문의 종료 조건|
|수행 시간|(상대적) 느림|빠름|
|메모리 공간|(상대적) 많이 사용|적게 사용|
|소스 코드 길이|짧고 간결|길다|
|소스 코드 형태|선택 구조 (if - else)|반복 구조 (for, while)|
|무한 반복시|스택 오버플로우|CPU를 반복해서 점유|

## 완전검색기법
### Brute-Force
- 대부분의 문제에 적용 가능하다.
- 상대적으로 빠른 시간에 알고리즘 설계를 할 수 있음
- 문제에 포함된 자료(요소, 인스턴스)의 크기가 작다면 유용
- 학술적 또는 교육적 목적을 위해 알고리즘의 효율성을 판단하기 위한 척도로 사용됨

### 완전 검색
- 완전 검색은 조합적 문제에 대한 brute-force 방법

## 순열
- 서로 다른 것들 중 몇 개를 뽑아서 한줄로 나열
- N개의 요소들에 대해서 n!개의 순열들이 존재
    ```
    def f(i,N,K): # i : 고른 개수
        if i == K : # 순열 완성
            print(p)
            return
        else : # card[i]에 들어갈 숫자를 결정
            for j in range(N):
                if used[j] == 0 : # 아직 사용 X
                    p[i] = card[j]
                    used[j] = 1
                    f(i+1, N,K)
                    used[j] = 0


    card = list(map(int, input()))
    N = 5
    K = 3
    used = [0] * N
    p = [0] * K
    f(0, N, K)
    ```
## 부분 집합
- 집합에 포함된 원소를 선택
- N개의 원소를 포함한 집합
  - 자기 자신과 공집합을 포함한 모든 부분집합의 개수는 2<sup>n</sup>
- 부분집합 구하기
    ```
    a = [1,2,3,4,5,6]
    N = 6
    for i in range(1, 1<<N): # (1<<N)//2 : 절반만 , (1<<N) -1 : 공집합 제외하고 출력
        subset1 = []
        subset2 = []
        for j in range(N):
            if i&(1<<j): # j번 비트가 0이 아니면
                subset1.append(a[j])
            else :
                subset2.append(a[j])
        print(subset1, subset2)
    ```
## 조합
서로 다른 n개의 원소 중 r개를 순서 없이 골라낸 것
- 재귀를 이용한 조합 구현
    ```
    def ncr(n, r):
        if r == 0 :
            print(tr)
        elif n<r :
            return
        else :
            tr[r-1] = a[n-1]
            ncr(n-1, r-1)
            ncr(n-1, r)

    N = 5
    R = 3
    a = [1,2,3,4,5]
    tr = [0] * R
    print(ncr(N,R))
    ```
- 재귀와 for문을 이용한 조합 구현
    ```
    def nCr(n,r,s):
        if r == 0 :
            print(*comb)
        else :
            for i in range(s,n-r+1):
                comb[r-1]  = A[i]
                nCr(n, r-1, i+1)

    A = [1,2,3,4,5]
    N = len(A)
    R = 3
    comb = [0] * R
    nCr(N,R,0)
    ```

## 탐욕 알고리즘
### 탐욕 알고리즘
- 최적해를 구하는데 사용되는 근시안적인 방법
- 일반적으로 머릿속에 떠오르는 생각을 검증 없이 바로 구현하면 Greedy 접근이 된다

### 탐욕 기법 VS 동적 계획법
|탐욕 기법|동적 계획법|
|---|---|
|매 단계에서, 가장 좋게 보이는 것을 빠르게 선택한다. -> 지역 최적 선택(local optimal choice) |매 단계의 선택은 해결한 하위 문제의 해를 기반으로 한다.|
|하위 문제를 풀기 전에 (탐욕적)선택이 먼저 이루어진다|하위 문제가 우선 해결된다.|
|Top-down 방식|Bottom-up 방식|
|일반적으로, 빠르고 간결하다|좀 더 느리고, 복잡하다|
