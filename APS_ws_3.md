# String
2023.08.07(Mon) ~
-----
## 문자열
- for 문을 이용한 문자열 뒤집기
    ```
    def is_palindrome(word):
    N = len(word)
    for i in range(N // 2):
        if word[i] != word[N - 1 - i]:
            return False
    return True
    ```
- for 문을 이용한 문자열 비교
    ```
    def is_pa(pattern, text):
    N,M = len(text), len(pattern)
    for s in range(N-M + 1):
        # text[s: s+m] == pattern
        # 패턴의 길이만큼 비교
        for i in range(M):
            if text[s + i] != pattern[i]:
                break
        else:
            return True
    ```
- int()와 같은 atoi 함수 만들기
    ```
    def atoi(s):
        i = 0
        for x in s : 
            i = i* 10 + ord(x) - ord('0')
        return i 
    ```
## 패턴 매칭
### 고지식한 패턴 검색 알고리즘(Brute Force)
- 본문 문자열을 처음부터 끝까지 차례대로 순회하면서 패턴 내의 문자들을 일일히 비교하는 방식으로 동작
```
p = 'is' # 찾을 패턴
t = 'This is a book~!' #전체 텍스트
M = len(p)
N = len(t)

def BruteForce(p, t) :
    i = 0 # t의 인덱스
    j = 0 # p의 인덱스
    while j < M and i <N :
        if t[i] != p[j] :
            i = i-j
            j = -1
        i = i + 1
        j = j + 1
    if j == M : return i - M # 검색 성공
    else : return -1 #검색 실패    
```
- 최악의 경우 시간 복잡도는 텍스트의 모든 위치에서 패턴을 비교해야 하므로 O(MN)이 됨

### 카프-라빈 알고리즘
### KMP 알고리즘
- 불일치가 발생한 text string의 앞 부분에 어떤 문자가 있는지를 미리 알고 있으므로, 불일치가 발생한 앞 부분에 대해 다시 비교하지 않고 매칭을 수행
- 패턴을 전처리하여 next(M) 배열을 구해 잘못된 시작을 최소화함
    - next[M] : 불일치가 발생했을 경우 이동할 다음 위치
- 시간 복잡도 : O(M+N)
```
def kmp(t, p):
    N = len(t)
    M = len(p)
    lps = [0] * (M+1)
    # preprocessing
    j = 0  # 일치한 개수 == 비교할 패턴 위치
    lps[0] = -1
    for i in range(1, M):
        lps[i] = j  # p[i] 이전에 일치한 개수
        if p[i] == p[j]:
            j += 1
        else :
    lps[M] = j
    print(lps)
```
### 보이어=무어 알고리즘
- 오른쪽에서 왼쪽으로 비교
- 패턴의 오른쪽 끝에 있는 문자가 불일치하고 이 문자가 패턴 내에 존재하지 않는 경우, **패턴의 길이만큼 이동**
- 최악의 경우 수행시간은 O(MN)이지만, 일반적으로 O(N)보다 시간이 덜 든다.

