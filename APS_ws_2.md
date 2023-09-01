# Array 1
2023.08.02(Wed) ~ 2023.08.03(Thu)
-----
## 2차원 배열


### 2차원 배열의 선언
- 1차원 List를 묶어놓은 List
- 2차원 이상의 다차원 List는 차원에 따라 Index를 선언
- 2차원 List의 선언 : 세로길이(행의 개수), 가로길이(열의 개수)를 필요로 함
- Python에서는 데이터 초기화를 통해 변수 선언과 초기화가 가능
```
N = int(input())
arr = [list(map(int,input().split())) for _ in range(N)]

N = int(input())
arr = [list(map(int,input().split())) for _ in range(N)]
```
- 배열 순회 : n x m 배열의 n*m개의 모든 원소를 빠짐없이 조사하는 방법
- 행 우선 순회
    ```
    # i 행의 좌표
    # j 열의 좌표

    for i in range(n):
        for j in range(m):
            f(Array[i][j]) #필요한 연산 수행
    ```
- 열 우선 순회
    ```
    # i 행의 좌표
    # j 열의 좌표

    for j in range(m):
        for i in range(n):
            f(Array[i][j]) #필요한 연산 수행
    ```
- 지그재그 순회
    ```
    # i 행의 좌표
    # j 열의 좌표

    for i in range(n):
        for j in range(m):
            f(Array[i][j + (m-1-2*j)*(1%2)]) #필요한 연산 수행
    ```
- delta를 이용한 2차 배열 탐색
    - 2차 배열의 한 좌표에서 **4방향의 인접 배열 요소**를 탐색하는 방법
    ```
    arr[0...N-1][0...N-1] # NxN 배열
    di[] <- [0, 1, 0, -1]
    dj[] <- [1, 0, -1, 0]
    for i : 0 -> N-1
        for j : 0 -> N-1 :
            for k in range(4) :
                ni <- i +di[k]
                nj <- j +dj[k]
                if 0 <= ni < N and 0 <= nj < N # 유효한 인덱스면 
                    f(arr[ni][nj])
    ```
    - 만약 대각 인덱스라면
    ```
    di[] <- [-1, -1, 1, 1]
    dj[] <- [-1, 1, -1, 1]
    ```
    - 상하좌우 p개의 요소를 출력해야 한다면
    ```
    di[] <- [0, 1, 0, -1]
    dj[] <- [1, 0, -1, 0]
    for p in range(P):
        ni, nj = i+di*p, j+dj*p
    ```
    - 전치행렬
    ```
    # i : 행의 좌표, len(arr)
    # 2 : 열의 좌표, len(arr[0])
    arr = [[1,2,3],[4,5,6],[7,8,9]] # 3*3 행렬
    for i in range(3):
        for j in range(3) : 
            if i < j :
                arr[i][j], arr[j][i]  = arr[j][i], arr[i][j] 
    ```
    - 대각행렬의 합
    ```
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    total1 = 0
    for i in range(N):
        total1 +=arr[i][i]
    
    # c.f. 거꾸로 
    for i in range(N):
        total2 += arr[i][N-i-1]
    ```
## 부분집합 생성
- 부분집합 합 문제
> 유한 개의 정수로 이루어진 집합이 있을때, 이 집합의 부분집합 중에서 그 집합의 원소를 모두 더한 값이 0이 되는 경우가 있는지를 알아내는 문제
> e.g. [-7, -3, -2, 5, 8] 라는 집합이 있을때 [-3, -2, 5] 는 부분집합 이면서 합이 0
    - 완전검색 기법으로 부분집합 합 문제를 풀기 위해선 우선 집합의 모든 부분집합을 생성한 후 각 부분집합의 합을 계산해야함.

- 부분집합의 수
    - 집합의 원소가 n개일때, 공집합을 포함한 부분집합의 수는 2^n개
    - 각 원소를 부분집합에 포함시키거나 포함시키지 않는 2가지 경우를 모든 원소에 적용한 경우의 수와 같음
    ```
    def print_subset(bit,arr,n) :
        total = 0 # 부분집합의 합
        for i in range(n):
            if bit[i]:
                print(arr[i], end= ' ')
                total += arr[i]
        print(bit)
    arr = [1, 2, 3, 4]
    bit = [0, 0, 0, 0]
    for i in range(2) :
        bit[0] = i
        for j in range(2) :
            bit[1] = j
            for k in range(2):
                bit[2] = k
                for l in range(2) :
                    bit[3] = 1
                    print_subset(bit, arr, 4)
    ```

- 비트 연산자 
    |연산자|설명|
    |---|---|
    | & | 비트 단위로 AND 연산을 한다.|
    | \| | 비트 단위로 OR 연산을 한다.|
    | << |피연산자의 비트 열을 왼쪽으로 이동시킨다.|
    | >> |피연산자의 비트 열을 오른쪽으로 이동시킨다|
    | 1 << n | 2^n , 원소가 n개일 경우 의 모든 부분집합의 수를 의미 |
    | i & (1<<j) | i의 j번째 비트가 1인지 아닌지를 검사|
    - [추가자료](https://dojang.io/mod/page/view.php?id=2460)

    ```
    arr = [1,2,3]

    n = len(arr)

    for i in range(1<<n): # 1<<n : 부분집합의 개수
        for j in range(n): # 원소의 수만큼 비트를 비교
            if i & (i<<j): # i의 j번 비트가 1인 경우
                print(arr[j], end=", ") # j번 원소 출력 
    ```
## 검색

- 저장되어 있는 자료 중에서 원하는 항목을 찾는 작업
- 목적하는 탐색 키를 가진 항목을 찾는 것
    - 탐색 키 : 자료를 구별하여 인식할 수 있는 키
- 검색의 종류
    1. 순차 검색 (Sequential search)
    2. 이진 검색 (binary search)
    3. 해쉬(hash)

### Sequential Search

- 일렬로 되어 있는 자료를 순서대로 검색하는 방법
    - 가장 간단하고 직관적인 검색 방법
    - 배열이나 연결 리스트 등 순차구조로 구현된 자료구조에서 원하는 항목을 찾을 때 유용
    - 알고리즘이 단순하여 구현이 쉽지만, 검색 대상의 수가 많은 경우에는 수행시간이 급격히 증가하여 비효율적임

- 정렬되어 있지 않은 경우
    - 검색 과정
        - 첫 번째 원소부터 순서대로 검색 대상과 키 값이 같은 원소가 있는지 비교하며 찾는다.
        - 키 값이 동일한 원소를 찾으면 그 원소의 인덱스를 반환한다.
        - 자료구조의 마지막에 이를 때까지 검색 대상을 찾지 못하면 검색 실패
    - 찾고자 하는 원소의 순서에 따라 비교 회수가 결정됨
        - 첫번째 원소를 찾을 때는 1번 비교, 두번째 원소를 찾을때는 2번 비교
        - 정렬되지 않은 자료에서 순차 검색의 평균 비교 회수 = (1/n)*(1+2+3+4+...+n) = (n+1)/2
        - 시간 복잡도 : O(n)
    ```
    def sequentialSearch_Unsorted(a, n, key)
        i <- 0
        while i<n and a[i] != key :
            i <- i+1
        if i<n : return i
        else : return -1
    ```
- 정렬되어 있는 경우
    - 검색 과정
        - 자료가 오름차순으로 정렬된 상태에서 자료를 순차적으로 검색하며 키값을 비교
    - 찾고자 하는 원소의 순서에 따라 비교 회수가 결정됨
        - 정렬이 되어있으므로, 검색 실패를 반환하는 경우 평균 비교 회수가 반으로 줄어듦
        - 시간 복잡도 : O(n)
    ```
    def sequentialSearch_Sorted(a, n, key)
        i <- o
        while i<n and a[i] < key :
            i <- i + 1
        if i<n and a[i] == key:
            return i
        else : 
            return -1
    ```

### 바이너리 서치

**자료의 가운데에 있는 항목의 키 값과 비교하여 다음 검색의 위치를 결정하고 검색을 계속 진행하는 방법**
- 목적 키를 찾을 때까지 이진 검색을 순환적으로 반복 수행함으로써 검색 범위를 반으로 줄여가면서 보다 빠르게 검색을 수행
- 이진 검색을 위해서는 자료가 정렬된 상태여야 한다.
- 구현
    - 검색 범위의 시작점과 종료점을 이용하여 검색을 반복 수행
    - 이진 검색의 경우, 자료에 삽입이나 삭제가 발생했을때 배열의 상태를 항상 정렬 상태로 유지하는 추가 작업이 필요함
- 시간 복잡도 : O(log n)
```
def binarySearch(a, N, key)
    start = 0
    end = N-1
    while start <= end :
        middle = (start + end) //2
        if a[middle] ==key : # 검색 성공
            return true
        elif a[middle] > key : 
            end = middle - 1
        else :
            start = middle + 1
    return false # 검색 실패
```
- 재귀 함수를 이용한 이진 검색 구현도 가능
    ```
    def binarySearch_myself(a, low, high, key) :
        if low > high : # 검색 실패
            return False
        else : 
            middle = (low + high) // 2
            if key == a[middle] : # 검색 성공
                return True
            elif key < a[middle] :
                return binarySearch_myself(a, low, middle-1, key)
            elif key > a[middle] :
                return binarySearch_myself(a, middle+1, high, key)
    ```

## 선택 정렬 Selection Sort
- 주어진 자료들 중 가장 작은 값의 원소부터 차례대로 선택하여 위치를 교환하는 방식
- 정렬과정 
    - 주어진 리스트 중 최소값을 찾음
    - 그 값을 리스트의 맨 앞에 위치한 값과 교환
    - 맨 처음 위치를 제외한 나머지 리스트를 대상으로 위의 과정을 반복
- 시간 복잡도 : O(n^2)
```
def SelectionSort(a, N):
    for i in range(N-1):
        minIdx = i
        for j in range(i+1, N) :
            if a[minIdx] > a[j]:
                minIdx = j
        a[i], a[minIdx] = a[minIdx], a[i]
```
### Selection Algorithm
- 저장되어 있는 자료로부터 k번째로 큰/작은 원소를 찾는 방법
- 선택 과정
    - 정렬 알고리즘을 이용하여 자료 정렬
    - 원하는 순서에 있는 원소 가져오기
- k번째로 작은 원소를 찾는 알고리즘
    - 1번부터 k번째까지 작은 원소들을 찾아 배열의 앞쪽으로 이동시키고, 배열의 k번째를 반환
    - k가 비교적 작을 때 유용
    - 수행시간 : O(kn)
    ```
    def select(arr, k) :
        for i in range(0, k) :
            minIdx = i
            for j in range(i+1, len(arr)) :
                if arr[minIdx] > arr[j]:
                    minIdx = j
            arr[i], arr[minIdx] = arr[minIdx] , arr[i]
        return arr[k-1]
    ```
    - **bubble sort와 구분해서 구현하기**
**알고리즘 특성 비교**

|알고리즘|평균 수행시간|최악 수행시간|알고리즘 기법|비고|
|---|---|---|---|---|
|버블 정렬|O(n^2)|O(n^2)|비교와 교환|코딩이 가장 손쉽다.|
|카운팅 정렬|O(n+k)|O(n+k)|비교환 방식|n이 비교적 작을 때만 가능하다.|
|선택 정렬|O(n^2)|O(n^2)|비교와 교환|교환의 횟수가 버블, 삽입 정렬보다 작다.|