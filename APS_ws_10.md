# 분할정복 & 백트래킹

2023.09.18(Mon) ~ 2023.09.19(Tue)

-----

## 분할정복
```
arr = [69, 10, 30, 2, 16, 8, 31, 22]


def merge(left, right):
    result = []

    # 한 쪽이 빌 때까지 반복
    while len(left) > 0 or len(right) > 0:
        # 둘 다 남아 있으면, 두 리스트의 가장 앞에 있는 것 중 작은 것을 선택하여 result 에 추가
        if len(left) > 0 and len(right) > 0:
            if left[0] <= right[0]:
                result.append(left.pop(0))
            else:
                result.append(right.pop(0))
        # 한 쪽만 남아있으면, 남은것을 모두 result 에 추가
        elif len(left) > 0:
            result.append(left.pop(0))
        elif len(right) > 0:
            result.append(right.pop(0))

    return result

def merge_sort(unordered_list):
    # 길이가 1인 배열까지 나누면 stop
    if len(unordered_list) == 1:
        return unordered_list

    left = []
    right = []
    middle = len(unordered_list) // 2
    # 왼쪽을 따로 리스트에 저장
    for el in unordered_list[:middle]:
        left.append(el)

    # 오른쪽을 따로 리스트에 저장
    for el in unordered_list[middle:]:
        right.append(el)

    left = merge_sort(left)
    right = merge_sort(right)

    return merge(left, right)

arr = merge_sort(arr)
print(arr)
```

## 퀵 정렬

## 이진 검색

## 백트래킹
### N-Queen 문제
> n x n 서양 장기판에서 배치한 Queen들이 서로 위협하지 않도록 n개의 Queen을 배치하는 문제
- 어떤 두 Queen도 서로를 위협하지 않아야 한다.
- Queen을 배치한 n개의 위치는?

### Backtracking
- 여러가지 선택지(option)들이 존재하는 상황에서 한가지를 선택한다.
- 선택이 이루어지면 새로운 선택지들의 집합이 생성된다.
- 이러한 선택을 반복하면서 최종 상태에 도달한다.
  - 올바른 선택을 계속하면 목표 상태(goal state)에 도달한다.

- 당첨 리프 노드 찾기
![leaf node](https://github.com/yamuzin-oksusu/SSAFY_FW2023/blob/master/images/image-21.png)
  - 루트에서 갈 수 있는 노드를 선택한다
  - 꽝 노드까지 도달하면 최근의 선택으로 되돌아와서 다시 시작한다.
  - 더 이상의 선택지가 없다면 이전의 선택지로 돌아가서 다른 선택을 한다
  - 루트까지 돌아갔을 경우 더 이상 선택지가 없다면 찾는 답이 없다.

- 백트래킹과 깊이 우선 탐색과의 차이
  - 어떤 노드에서 출발하는 경로가 해결책으로 이어질 것 같지 않으면 더 이상 그 경로를 따라가지 않음으로써 시도의 횟수를 줄임. (Prunning 가지치기)
  - 깊이 우선 탐색이 모든 경로를 추적하는데 비해 백트래킹은 불필요한 경로를 조기에 차단
  - 깊이 우선 탐색을 가하기에는 경우의 수가 너무나 많음. 즉 **N!**가지의 경우의 수를 가진 문제에 대해 깊이 우선 탐색을 가하면 당연히 처리 불가능한 문제
  - **백트래킹 알고리즘을 적용하면 일반적으로 경우의 수가 줄어들지만 이 역시 최악의 경우에는 여전히 지수함수 시간(Exponential Time)을 요하므로 처리 불가능**


- {1, 2, 3} 집합에서 3개의 숫자를 선택하는 백트래킹 알고리즘

```
# 이미 사용한 숫자는 사용하지 않음
arr = [i for i in range(1,4)]
path = [0] * 3
def backtracking(cnt):
    # 기저 조건
    # 숫자 3개를 골랐을 때 종료
    if cnt == 3 :
        print(*path)
        return

    for num in arr :
        # 가지치기 : 중복 제거
        if num in path :
            continue    
        # 들어가기 전 로직 : 경로 저장
        path[cnt] = num
        # 다음 재귀 함수 호출
        backtracking(cnt+1)
        # 돌아와서 할 로직 : 초기화
        path[cnt] = 0

backtracking(0)
```

## 트리
### 계산기
> 수식 2+3*4를 다음과 같은 그래프로 표현하고 그래프를 순회하여 수식을 계산하시오
![leaf node](https://github.com/yamuzin-oksusu/SSAFY_FW2023/blob/master/images/image-22.png)
### 트리
- 트리는 싸이클이 없는 무향 연결 그래프이다.
  - 두 노드(or 정점) 사이에는 유일한 경로가 존재한다
  - 각 노드는 최대 하나의 부모 노드가 존재할 수 있다
  - 각 노드는 자식 노드가 없거나 하나 이상이 존재할 수 있다

- 비선형 구조
  - 원소들 간에 1:n 관계를 가지는 자료구조
  - 원소들 간에 계층관계를 가지는 계층형 자료구조

- 한 개 이상의 노드로 이루어진 유한 집합이며 다음 조건을 만족한다.
  - 노드 중 부모가 없는 노드를 root라 한다
  - 나머지 노드들은 n(>=0)개의 분리 집합 T1 , ... , TN 으로 분리될 수 있다.
- 이들 T1 , ... , TN은 각각 하나의 트리가 되며(재귀적 정의) 루트의 서브트리라 한다.
- 트리 용어
  - node : 트리의 원소이고 정점(vertex)이라고도 한다
  - edge(간선) : 노드를 연결하는 선
  - root node : 트리의 시작 노드
  - 형제 노드 : 같은 부모 노드의 자식 노드들
  - 조상 노드 : 간선을 따라 루트 노드까지 이르는 경로에 있는 모든 노드들
  - 서브 트리 : 부모 노드와 연결된 간선을 끊었을 때 생성되는 트리
  - 자손 노드 : 서브 트리에 있는 하위 레벨의 노드들
  - 차수
- 이진 트리
  - 자식 노드가 둘 이하인 트리