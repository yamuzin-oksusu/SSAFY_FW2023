##################
## backtracking ##
##################

# # {1, 2, 3} 집합에서 3개의 숫자를 선택하는 기본적인 예제
# # 이미 사용한 숫자는 사용하지 않음
# arr = [i for i in range(1,4)]
# path = [0] * 3
# def backtracking(cnt):
#     # 기저 조건
#     # 숫자 3개를 골랐을 때 종료
#     if cnt == 3 :
#         print(*path)
#         return

#     for num in arr :
#         # 가지치기 : 중복 제거
#         if num in path :
#             continue    
#         # 들어가기 전 로직 : 경로 저장
#         path[cnt] = num
#         # 다음 재귀 함수 호출
#         backtracking(cnt+1)
#         # 돌아와서 할 로직 : 초기화
#         path[cnt] = 0

# backtracking(0)



#################
## Binary Tree ##
#################

## 개발용
arr = [1, 2, 1, 3, 2, 4, 3, 5, 3, 6, 4, 7, 5, 8, 5, 9, 6, 10, 6, 11, 7, 12, 11, 13]


class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def insert(self, child):
        if(not self.left):
            self.left = child
            return
        if(not self.right):
            self.right = child
            return
        return

    def preorder(self):
        if self != None:
            print(self.value, end=' ')
            if self.left:
                self.left.preorder()
            if self.right:
                self.right.preorder()

    # 중위 순회
    def inorder(self):
        if self != None:
            if self.left:
                self.left.inorder()
            print(self.value, end=' ')
            if self.right:
                self.right.inorder()

    # 후위 순회
    def postorder(self):
        if self != None:
            if self.left:
                self.left.postorder()
            if self.right:
                self.right.postorder()
            print(self.value, end=' ')

# 이진 트리 만들기
nodes = [TreeNode(i) for i in range(0, 14)]
for i in range(0, len(arr), 2):
    parentNode = arr[i]
    childNode = arr[i + 1]
    nodes[parentNode].insert(nodes[childNode])

nodes[1].preorder()
print()
nodes[1].inorder()
print()
nodes[1].postorder()


## 문제 풀이용

arr = [1, 2, 1, 3, 2, 4, 3, 5, 3, 6]
# arr = [1, 2, 1, 3, 2, 4, 3, 5, 3, 6, 4, 7, 5, 8, 5, 9, 6, 10, 6, 11, 7, 12, 11, 13]


# 이진 트리 생성
nodes = [[] for _ in range(14)]
for i in range(0, len(arr), 2):
    parentNode = arr[i]
    childNode = arr[i + 1]
    nodes[parentNode].append(childNode)

# 자식이 없다는 걸 표현하기 위해 None 을 삽입
for li in nodes:
    for _ in range(len(li), 2):
        li.append(None)

# 전위 순회
def preorder(nodeNum):
    if nodeNum == None:
        return
    # print(nodeNum, end=' ')
    preorder(nodes[nodeNum][0])
    # print(nodeNum, end=' ')
    preorder(nodes[nodeNum][1])
    # print(nodeNum, end=' ')

preorder(1)


## 이진 탐색 트리
class TreeNode:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.value = key


def insert(root, key):
    if root is None:
        return TreeNode(key)
    else:
        if key < root.value:
            root.left = insert(root.left, key)
        else:
            root.right = insert(root.right, key)
    return root


def search(root, key):
    if root is None or root.value == key:
        return root
    if root.value < key:
        return search(root.right, key)
    return search(root.left, key)


def inorder_traversal(root):
    if root:
        print(root.value, end=" ")
        inorder_traversal(root.left)
        inorder_traversal(root.right)


def find_min_node(node):
    current = node
    while current.left is not None:
        current = current.left
    return current


def delete_node(root, key):
    if root is None:
        return root

    if key < root.value:
        root.left = delete_node(root.left, key)
    elif key > root.value:
        root.right = delete_node(root.right, key)
    else:
        # 삭제하려는 노드가 리프 노드이거나 하나의 자식만 가지는 경우
        if root.left is None:
            temp = root.right
            root = None
            return temp
        elif root.right is None:
            temp = root.left
            root = None
            return temp

        # 삭제하려는 노드가 두 개의 자식을 가지는 경우
        # 1. 왼쪽 서브 트리의 가장 큰 값
        # 2. 오른쪽 서브 트리의 가장 작은 값
        # 두 가지가 가능한 후보
        temp = find_min_node(root.right)
        root.value = temp.value
        root.right = delete_node(root.right, temp.value)

    return root


# 이진 탐색 트리 생성 및 사용 예제
arr = [8, 3, 10, 2, 5, 14]
root = insert(None, arr[0])
for el in arr[1:]:
    insert(root, el)

# 특정 값 검색 예제
key_to_search = 10
result = search(root, key_to_search)
if result:
    print(f"{key_to_search}를 찾았습니다.")
else:
    print(f"{key_to_search}를 찾을 수 없습니다.")

# 노드 삭제 예제
key_to_delete = 5
inorder_traversal(root)
print()
root = delete_node(root, key_to_delete)
inorder_traversal(root)

test = 1


############
### heap ###
############

from heapq import heappop, heappush, heapify

arr = [69, 30, 10, 2, 16, 8, 32, 21]

H = [] # 힙 저장소

# 힙 정렬

for val in arr :
    heappush(H, val)

# heapq가 prioirtyq보다 빠름
while H :
    print(heappop(H), end = ' ')


# 최대힙

for val in arr :
    heappush(H, (-val))

while H :
    print(-heappop(H),end=' ')

# 힙 구조가 아닌 걸 이진 힙으로 만듦
# 잘 쓰이지 않으므로 heappop, heappush 만 알아두자
heapify(arr)

print(arr)