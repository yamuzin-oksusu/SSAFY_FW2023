# Stack 1
2023.08.09(Wed) 
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
## DP
## DFS