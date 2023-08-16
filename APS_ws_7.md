# Stack 1
2023.08.09(Wed) ~ 2023.08.10(Thu)
-----
## 스택
### 스택의 특성
- 물건을 쌓아 올리듯 자료를 쌓아 올린 형태의 자료구조
- 스택에 저장된 자료는 선형 구조를 갖는다.
    - 선형구조 : 자료 간의 관계가 1:1 관계를 가짐
    - 비선형구조 : 자료 간 1:N의 관계를 가짐(ex. Tree)
- 스택에 자료를 삽입하거나 스택에서 자료를 꺼낼 수 있다.
- 후입선출
### 스택을 프로그램에서 구현하기 위해 필요한 자료 구조의 연산
- 자료 구조: 자료를 선형으로 저장할 저장소
    - 배열 사용 가능
    - 저장소 자체를 스택이라 부르기도 함
    - 스택에서 마지막으로 삽입된 원소의 위치를 top이라고 부름
- 연산 
    - 삽입 : 저장소에 자료를 저장 ; Push
        - append 메소드를 통해 리스트의 마지막에 데이터를 삽입
        ```
        def push(item):
            s.append(item)
        ```
        ```
        def push(item, size):
            global top
            top += 1
            if top == size : 
                print('overflow!') # 디버깅 목적
            else :
                stack[top] = item
        size = 10
        stack = [0] * size
        top = -1
        push(10,size)   # stack : [10, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        top += 1        # push(20)
        stack[top] = 20 # stack : [10, 21, 0, 0, 0, 0, 0, 0, 0, 0]
        ```
    - 삭제 : 삽입한 자료의 연순으로 꺼냄 ; Pop
        ```
        def pop() :
            if len(s) == 0 :
            # underflow
            return
            else : 
                return s.pop()
        ```
        ```
        def pop() : 
            global top
            if top == -1 :
                print('underflow')
            else : 
                top -= 1
                return stack[top+1]
        print(pop())
        if top > -1 :  # pop()
            top -= 1
            print(stack[top+1])
        ```
    - 스택이 공백인지 아닌지를 확인하는 연산 ; isEmpty
    - 스택의 top에 있는 item을 반환하는 연산 ; peek
### 스택 구현 고려 사항
- 1차원 배열을 사용하여 구현할 경우 구현이 용이하다는 장점이 있지만 스택의 크기를 변경하기 어렵다는 단점 있음
- 해결 : 저장소를 동적으로 할당하여 스택을 구현. 구현이 복잡하지만 메모리를 효율적으로 사용 가능함.

### Function call
- 프로그램에서 함수 호출과 복귀에 따른 수행 순서를 관리 [(참고)](https://dojang.io/mod/page/view.php?id=2341) 
    - 후입선출 구조의 스택을 이용하여 수행 순서를 관리
    - 함수 호출이 발생하면 호출한 함수 수행에 필요한 지역변수, 매개 변수 및 수행 후 복귀할 주소 등의 정보를 stack frame에 저장하여 시스템 스택에 삽입
    - 함수의 실행이 끝나면 시스템 스택의 top 원소(stack frame)를 삭제(pop)하면서 프레임에 저장되어 있던 복귀주소를 확인하고 복귀
    - 함수 호출과 복귀에 따라 이 과정을 반복하여 전체 프로그램 수행이 종료되면 시스템 스택은 공백 스택이 된다.

## 재귀호출
- 자기 자신을 호출하여 순환 수행되는 것
- 피보나치 수를 구하는 재귀함수
    ```
    def fibo(n):
        if n < 2 :
            return n
        else :
            return fibo(n-1) + fibo(n-2)
    ```
## Memoization
- 컴퓨터 프로그램을 실행할 때 이전에 계산한 값을 메모리에 저장해서 매번 다시 계산하지 않도록 하여 전체적인 실행속도를 빠르게 하는 기술
- 앞의 피보나치 수를 구하는 알고리즘에서 fibo(n)의 값을 계산하자마자 저장하면 실행시간을 O(n)으로 줄일 수 있다.
    ```
    # memo를 위한 배열을 할당하고, 모두 0으로 초기화 한다
    # memo[0]을 0으로, memo[1]은 1로 초기화 한다.
    def fibo1(n):
        global memo
        if n >= 2 and memo[n] == 0 :
            memo[n] = (fibo1(n-1)+ fibo1(n-2))
        return memo[n]
    memo = [0] * (n+1)
    memo[0] = 0
    memo[1] = 0
    ```
## DP (Dynamic Programming)
최적화 문제를 해결하는 알고리즘<br>
입력 크기가 작은 부분 문제들을 모두 해결한 후에 그 해들을 이용하여 보다 큰 크기의 부분 문제들을 해결하여, 최종적으로 원래 주어진 입력의 문제를 해결하는 알고리즘
### 피보나치 수의 DP 적용 방법
피보나치 수는 부분 문제의 답으로부터 본 문제의 답을 얻을 수 있으므로 최적 부분 구조로 이루어져 있다.
-  문제를 부분 문제로 분할한다
    - Fibo(n)함수는 Fibo(n-1)과 Fibo(n-2)의 합
    - Fibo(n-1)은 Fibo(n-2)과 Fibo(n-3)의 합
    - Fibo(2)는 Fibo(1)과 Fibo(0)의 합
    - Fibo(n)은 Fibo(n-1), Fibo(n-2), ... , Fibo(2), Fibo(1), Fibo(1)의 부분집합으로 나뉜다.
- 가장 작은 부분 문제부터 해를 구한다
- 그 결과는 테이블에 저장하고 테이블에 저장된 부분 문제의 해를 이용하여 상위 문제의 해를 구한다.
    |테이블인덱스|저장되어 있는 값|
    |----|----|
    | <center> [0] </center> | <center> 0 </center> |
    | <center> [1] </center> | <center> 1 </center> |
    | <center> [2] </center> | <center> 1 </center> |
    | <center> [3] </center> | <center> 2 </center> |
    | <center> [4] </center> | <center> 3 </center> |
    | <center> ... </center> | <center> ... </center> |
    | <center> [n] </center> | <center> fibo(n) </center> |
- 피보나치 수 DP 적용 알고리즘
    ```
    def fibo2(n):
        f = [0] * (n+1)
        f[0] = 0
        f[1] = 1
        for i in range(2,n+1):
            f[i] = f[i-1] + f[i=2]
        
        return f[n]
    ```
### DP의 구현 방식
1. recursive 방식 : fib1()
2. iterative 방식 : fib2()
- memozation을 재귀적 구조에 사용하는 것보다 반복적 구조로 DP를 구현한 것이 성능 면에서 보다 효율적임
- 재귀적 구조는 내부에 시스템 호출 스택을 사용하는 오버헤드가 발생하기 때문

## DFS(Depth First Search)
비선형 구조인 그래프 구조는 그래프로 표현된 모든 자료를 빠짐없이 검색하는 것이 중요함.
- 두가지 방법 
    1. 깊이 우선 탐색 (Depth First Search ,DFS)
    2. 너비 우선 탐색 (Breadth First Search, BFS)

- 시작 정점의 한 방향으로 갈 수 있는 경로가 있는 곳 까지 깊이 탐색해가다가 더 이상 갈 곳이 없게 되면, 가장 마지막에 만났던 갈림길 간선이 있는 정점으로 되돌아와서 다른 방향의 정점으로 탐색을 계속 반복하여 결국 모든 정점을 방문하는 순회 방법<br>
- 가장 마지막에 만났던 갈림길의 정점으로 되돌아가서 다시 깊이 우선 탐색을 반복해야 하므로 **후입선출 구조의 스택 사용**
### DFS 알고리즘
1. 시작 정점 v를 결정하여 방문한다.
2. 정점 v에 인접한 정점 중에서
    - 방문하지 않은 정점 w가 있으면, 정점 v를 스택에 push하고 정점 w를 방문한다. 그리고 w를 v로 하여 다시 2. 를 만복한다.
    - 방문하지 않은 정점이 없으면, 탐색의 방향을 바꾸기 위해서 스택을 pop하여 받은 가장 마지막 방문 정점을 v로 하여 다시 2. 를 반복한다.
3. 스택이 공백이 될 때까지 2.를 반복한다.
-Pseudo-code
```
visited[] , stack[] 초기화
DFS(v)
    시작점 v 방문 ;
    visited[v] <- true ;
    while {
        if (v의 인접 정점 중 방문 안 한 정점 w가 있으면)
            push(v);
            v <- w; (w에 방문)
            visited[w] <- true ;
        else 
            if (스택이 비어 있지 않으면)
                v <- pop(stack) ;
            else 
                break
    }
end DFS()
```
### Python 구현 (재귀)
[출처](https://velog.io/@bbirong/3-1.-DFSBFS-%EA%B0%9C%EB%85%90-%EC%8B%A4%EC%A0%84-%EB%AC%B8%EC%A0%9C)
```
# DFS 메서드 정의
def dfs(graph, v, visited):
	# 현재 노드를 방문 처리
    visited[v] = True
    print(v, end=' ')
    # 현재 노드와 연결된 다른 노드를 재귀적으로 방문
    for i in graph[v]:
    	if not visited[i]:
        	dfs(graph, i, visited)

# 각 노드가 연결된 정보를 리스트 자료형으로 표현 (2차원 리스트)
graph = [
	[],
    [2, 3, 8],
    [1, 7],
    [1, 4, 5],
    [3, 5],
    [3, 4],
    [7],
    [2, 6, 8],
    [1, 7]
]

# 각 노드가 방문된 정보를 리스트 자료형으로 표현 (1차원 리스트)
visited = [False] * 9

# 정의된 DFS 함수 호출
dfs(graph, 1, visited)

# 1 2 7 6 8 3 4 5
```

### Python 구현(iteration)
[출처](https://juhee-maeng.tistory.com/25)
```
def dfs_iteration(graph, root):
    # visited = 방문한 꼭지점들을 기록한 리스트
    visited = []
    # dfs는 stack, bfs는 queue개념을 이용한다.
    stack = [root]
    
    while(stack): #스택에 남은것이 없을 때까지 반복
        node = stack.pop() # node : 현재 방문하고 있는 꼭지점
        
        #현재 node가 방문한 적 없다 -> visited에 추가한다.
        #그리고 해당 node의 자식 node들을 stack에 추가한다.
        if(node not in visited):
            visited.append(node)
            stack.extend(graph[node])
    return visited
```
- stack에 다 넣어놓고 하나씩 pop해서 비교하는 꼼수 st

### Python 구현 (인접 행렬 이용)
```
'''
V E
v1 w1 v2 w2 ...
7 8
1 2 1 3 2 4 2 5 4 6 5 6 6 7 3 7
'''
def dfs(n, V, adj_m):
    # stack 생성
    stack = []
    # visited 생성
    visited = [0] * (V+1)
    # 시작점 방문 표시
    visited[n] = 1
    # do[n]
    print(n)
    while True : 
        for w in range(1,V+1): # 현재 정점 n에 인접하고 미방문 w 찾기
            if adj_m[n][w] == 1 and visited[w] == 0 :
                stack.append(n) # push(n), v = w
                n = w
                print(n) # do(w)
                visited[n] = 1 # w 방문 표시
                break # for w, n 에 인접인 w c 찾은 경우 
        else :
            if stack : # 스택에 지나온 정점이 남아있으면
                n = stack.pop() # pop해서 다시 다른 w 찾을 n 준비
            else : 
                break
    return dfs


V, E = map(int, input().split()) # 1번 부터 v번 정점, E개의 간선
arr = list(map(int, input().split()))
adj_m = [[0]*(V+1) for _ in range(V+1)]
for i in range(E):
    v1, v2 = arr[i*2], arr[i*2+1]
    adj_m[v1][v2] = 1
    adj_m[v2][v1] = 1
# print() # 배열로 나타내기

dfs(1, V, adj_m)
```