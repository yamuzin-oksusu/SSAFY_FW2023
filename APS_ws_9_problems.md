# 완전탐색 & Greedy 보충 학습

----

## SWEA 문제들
### 11802. [완전검색_최소합](https://swexpertacademy.com/main/talk/solvingClub/problemView.do?contestProbId=AXjJL-EqQHADFAW9&solveclubId=AYlJBdPaI40DFASe&problemBoxTitle=0830_%EC%99%84%EC%A0%84%ED%83%90%EC%83%89&problemBoxCnt=4&probBoxId=AYpDs1JaQmUDFAQI)
![Alt text](image-5.png)
>그림처럼 NxN 칸에 숫자가 적힌 판이 주어지고, 각 칸에서는 오른쪽이나 아래로만 이동할 수 있다.<br>맨 왼쪽 위에서 오른쪽 아래까지 이동할 때, 지나는 칸에 써진 숫자의 합계가 최소가 되도록 움직였다면 이때의 합계가 얼마인지 출력하는 프로그램을 만드시오.<br>그림의 경우 1, 2, 3, 4, 5순으로 움직이고 최소합계는 15가 된다. 가능한 모든 경로에 대해 합을 계산한 다음 최소값을 찾아도 된다.


>[입력]<br> 첫 줄에 테스트케이스의 수 T가 주어진다. 1<=T<=50 <br> 다음 줄부터 테스트 케이스의 별로 첫 줄에 가로 세로 칸 수 N이 주어지고, 다음 줄부터 N개씩 N개의 줄에 걸쳐 10이하의 자연수가 주어진다. 3<=N<=13
 

>[출력]<br>각 줄마다 "#T" (T는 테스트 케이스 번호)를 출력한 뒤, 답을 출력한다.


```
from collections import deque
 
dz = [(0, 1), (1, 0)] # 갈수 있는 경로는 왼쪽 한칸 or 아래로 한칸 뿐
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    visited = [[0]*N for _ in range(N)]
    visited[0][0] = arr[0][0]
    queue = deque()
    queue.append((0, 0))
    while queue:
        si, sj = queue.popleft()
        for di, dj in dz:
            ni = si + di
            nj = sj + dj
            if 0 <= ni < N and 0 <= nj < N:
                if not visited[ni][nj]:
                    visited[ni][nj] = visited[si][sj] + arr[ni][nj]
                    queue.append((ni, nj))
 
                elif visited[ni][nj] > visited[si][sj] + arr[ni][nj]:
                    visited[ni][nj] = visited[si][sj] + arr[ni][nj]
                    queue.append((ni, nj))
 
    print(f'#{tc} {visited[N-1][N-1]}')
```
by.진성님

### 화물도크


### 2817. 부분수열의 합
>A<sub>1</sub>, A<sub>1</sub>, ... , A<sub>N</sub>의 N개의 자연수가 주어졌을 때, 최소 1개 이상의 수를 선택하여 그 합이 K가 되는 경우의 수를 구하는 프로그램을 작성하시오.


>[입력]<br>첫 번째 줄에 테스트 케이스의 수 T가 주어진다.<br> 각 테스트 케이스의 첫 번째 줄에는 2개의 자연수 N(1 ≤ N ≤ 20)과 K(1 ≤ K ≤ 1000)가 주어진다.<br>두 번째 줄에는 N개의 자연수 수열 A가 주어진다. 수열의 원소인 N개의 자연수는 공백을 사이에 두고 주어지며, 1 이상 100 이하임이 보장된다.


>[출력]<br>각 테스트 케이스마다 ‘#x ’(x는 테스트케이스 번호를 의미하며 1부터 시작한다)를 출력하고, 부분 수열의 합이 K가 되는 경우의 수를 출력한다.

```
```