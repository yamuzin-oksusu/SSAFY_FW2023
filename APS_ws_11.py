#########
## DFS ##
#########

# 인접행렬
# 장점: 구현이 쉽다
# 단점: 메모리 낭비
#      0도 표시를 하기 때문에
graph = [
    [0, 1, 0, 1, 0],
    [1, 0, 1, 1, 1],
    [0, 1, 0, 0, 0],
    [1, 1, 0, 0, 1],
    [0, 1, 0, 1, 0]
]

# DFS
# stack 버전
def dfs_stack(start):
    visited = []
    stack = [start]

    while stack:
        now = stack.pop()
        # 이미 방문한 지점이라면 continue
        if now in visited:
            continue

        # 방문하지 않은 지점이라면, 방문 표시
        visited.append(now)

        # 갈 수 있는 곳들을 stack 에 추가
        # for next in range(5):
        # 작은 번호 부터 조회
        for next in range(4, -1, -1):
            # 연결이 안되어 있다면 continue
            if graph[now][next] == 0:
                continue

            # 방문한 지점이라면 stack 에 추가하지 않음
            if next in visited:
                continue

            stack.append(next)
    # 출력을 위한 반환
    return visited

print("dfs stack = ", end='')
print(*dfs_stack(0))

# DFS - 재귀
# MAP 크기(길이)를 알 때 append 형식이 말고 아래와 같이 사용하면 훨씬 빠르다
visited = [0] * 5
path = []   # 방문 순서 기록

def dfs(now):
    visited[now] = 1    # 현재 지점 방문 표시
    print(now, end=' ')

    # 인접한 노드들을 방문
    for next in range(5):
        if graph[now][next] == 0:
            continue

        if visited[next]:
            continue

        dfs(next)

print('dfs 재귀 = ', end=' ')
dfs(0)

##############################

# 인접리스트
# 갈 수 있는 지점만 저장하자
# 주의사항
# - 각 노드마다 갈 수 있는 지점의 개수가 다름
#   -> range 쓸 때 index 조심
# 메모리가 인접 행렬에 비해 훨씬 효율적이다.
graph = [
    [1, 3],
    [0, 2, 3, 4],
    [1],
    [0, 1, 4],
    [1, 3],
]

# 파이썬은 딕셔너리로도 구현할 수 있다.
graph_dict = {
    '0': [1, 3],
    '1': [0, 2, 3, 4],
    '2': [1],
    '3': [0, 1, 4],
    '4': [1, 3]
}

# DFS
# stack 버전
def dfs_stack(start):
    visited = []
    stack = [start]

    while stack:
        now = stack.pop()
        # 이미 방문한 지점이라면 continue
        if now in visited:
            continue

        # 방문하지 않은 지점이라면, 방문 표시
        visited.append(now)

        # 작은 번호 부터 조회
        for to in range(len(graph[now]) - 1, -1, -1):
            # 이제 연결이 안되어있다는 건 애초에 저장하지 않았으므로
            # 체크할 필요 없음
            # if graph[now][next] == 0:
            #    continue

            next = graph[now][to]
            # 방문한 지점이라면 stack 에 추가하지 않음
            if next in visited:
                continue

            stack.append(next)
    # 출력을 위한 반환
    return visited

print("dfs stack = ", end='')
print(*dfs_stack(0))

# DFS - 재귀
# MAP 크기(길이)를 알 때 append 형식이 말고 아래와 같이 사용하면 훨씬 빠르다
visited = [0] * 5
path = []   # 방문 순서 기록

def dfs(now):
    visited[now] = 1    # 현재 지점 방문 표시
    # print(now, end=' ')
    path.append(now)

    # 인접한 노드들을 방문
    for to in range(len(graph[now])):
        next = graph[now][to]
        if visited[next]:
            continue

        dfs(next)

print('dfs 재귀 = ', end=' ')
dfs(0)
print(*path)



#########
## BFS ##
#########

## 인접 행렬

graph = [
    [0, 1, 0, 1, 0],
    [1, 0, 1, 1, 1],
    [0, 1, 0, 0, 0],
    [1, 1, 0, 0, 1],
    [0, 1, 0, 1, 0]
]

def bfs(start):
    visited = [0] * 5

    # 먼저 방문 했던 것을 먼저 처리해야 한다 = queue
    queue = [start]
    visited[start] = 1

    while queue:
        # queue 의 맨 앞 요소를 꺼냄
        now = queue.pop(0)
        print(now, end=' ')

        # 방문 체크 + 방문한 지점은 pass

        # 인접한 노드들을 queue 에 추가
        for next in range(5):
            # 연결이 안되어 있다면 continue
            if graph[now][next] == 0:
                continue

            # 방문한 지점이라면 queue 에 추가하지 않음
            if visited[next]:
                continue

            queue.append(next)
            # bfs 이므로 여기서 방문 체크를 해도 상관없다.
            visited[next] = 1

print('bfs = ', end=' ')
bfs(0)

############################

# 인접 리스트
graph = [
    [1, 3],
    [0, 2, 3, 4],
    [1],
    [0, 1, 4],
    [1, 3],
]


# 큐 bfs
def bfs(start):
    # 노드의 방문 여부를 저장하는 리스트
    visited = [0] * 5

    # 시작 노드를 큐에 추가하고 방문 표시
    queue = [start]
    visited[start] = 1

    while queue:
        # 큐에서 노드를 하나 꺼내고 출력
        now = queue.pop(0)
        print(now, end=' ')

        # 인접한 노드 중에서 방문하지 않은 노드를 큐에 추가하고 방문 표시
        for i in range(len(graph[now])):
            to = graph[now][i]
            if not visited[to]:
                queue.append(to)
                visited[to] = 1


# 0부터 시작하는 BFS를 호출
print("bfs queue = ", end=' ')
bfs(0)


################
## 서로소 집합 ##
################

# 0 ~ 9
# make set - 집합을 만들어 주는 과정
# 각 요소가 가리키는 값이 부모
parent = [i for i in range(10)]

# find-set
def find_set(x):
    if parent[x] == x:
        return x

    # return find_set(parent[x])

    # 경로 압축
    parent[x] = find_set(parent[x])
    return parent[x]

# union
def union(x, y):
    # 1. 이미 같은 집합인 지 체크
    x = find_set(x)
    y = find_set(y)

    # 대표자가 같으니, 같은 집합이다.
    if x == y:
        print("싸이클 발생")
        return

    # 2. 다른 집합이라면, 같은 대표자로 수정
    if x < y:
        parent[y] = x
    else:
        parent[x] = y

union(0, 1)

union(2, 3)

union(1, 3)

# 이미 같은 집합에 속해 있는 원소를 한 번 더 union
# 싸이클이 발생
union(0, 2)

# 대표자 검색
print(find_set(2))
print(find_set(3))

# 같은 그룹인 지 판별
t_x = 0
t_y = 2

if find_set(t_x) == find_set(t_y):
    print(f"{t_x} 와 {t_y} 는 같은 집합에 속해 있습니다.")
else:
    print(f"{t_x} 와 {t_y} 는 다른 집합에 속해 있습니다.")

