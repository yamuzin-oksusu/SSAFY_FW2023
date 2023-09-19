#############
## 분할정렬 ##
#############
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


################
## Quick Sort ##
################

arr = [3, 2, 4, 6, 9, 1, 8, 7, 5]


def hoare_partition(left, right):
    pivot = arr[left]
    left += 1

    while True:
        while arr[left] < pivot:
            left += 1
        while arr[right] > pivot:
            right -= 1

        print(f'left = {left} / right = {right} / arr = {arr}')

        # 엇갈린 경우 right 가 pivot 의 위치
        if left >= right:
            return right

        arr[left], arr[right] = arr[right], arr[left]

def quick_sort(left, right):
    # left 가 right 보다 커지면 종료
    if left >= right:
        return

    pivot = hoare_partition(left, right)
    arr[left], arr[pivot] = arr[pivot], arr[left]

    quick_sort(left, pivot)
    quick_sort(pivot + 1, right)


quick_sort(0, len(arr) - 1)
print(arr)

arr = [3, -100, 1000, -300, 12, 5, 2, 1, 2, 3, 5, 7, 8, 10, 9]


def lomuto_partition(left, right):
    pivot = arr[right]
    # i = 작은 요소들을 추적
    i = left - 1

    for j in range(left, right):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]

    # 피벗 위치 교환
    arr[i + 1], arr[right] = arr[right], arr[i + 1]
    # 피벗의 새 위치를 반환
    return i + 1


def quick_sort(left, right):
    if left < right:
        pivot = lomuto_partition(left, right)
        quick_sort(left, pivot - 1)
        quick_sort(pivot + 1, right)


quick_sort(0, len(arr) - 1)
print(arr)

###################
## Binary Search ##
###################

# 이진 검색(Binary Search) - 반복문 (loop)

arr = [2, 4, 7, 9, 11, 19, 23]

arr.sort()

def binarySearch(target):
    low = 0
    high = len(arr) - 1
    # 탐색 횟수 카운팅
    cnt = 0

    while low <= high:
        mid = (low + high) // 2
        cnt += 1

        if arr[mid] == target:
            return mid, cnt
        elif arr[mid] > target:
            high = mid - 1
        else:
            low = mid + 1
    return "해당 데이터는 없습니다", cnt

print(f'9 = {binarySearch(9)}')
print(f'2 = {binarySearch(2)}')
print(f'20 = {binarySearch(20)}')


# 이진 검색(Binary Search) - 재귀

arr = [2, 4, 7, 9, 11, 19, 23]


def binarySearch(low, high, target):
    # 기저조건
    # target 을 발견하지 못하면 종료
    if low > high:
        return -1

    mid = (low + high) // 2

    # 발견했다면
    if target == arr[mid]:
        return mid
    # target 이 mid 보다 작다 == target 이 mid의 왼쪽에 존재한다 == high 를 mid - 1로
    elif target < arr[mid]:
        return binarySearch(low, mid - 1, target)
    else:
        return binarySearch(mid + 1, high, target)


print(f'9 = {binarySearch(0, len(arr) - 1, 9)}')
print(f'2 = {binarySearch(0, len(arr) - 1, 2)}')
print(f'20 = {binarySearch(0, len(arr) - 1, 20)}')


