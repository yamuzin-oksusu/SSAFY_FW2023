def mydecorator(func):

    def wrapper(name):
        print('호출 전')
        func(name) # 함수 호출
        print('호출 후')
    
    return wrapper

@mydecorator
def printHello(name):
    print(f'{name}님 환영합니다.')

# wrapper(printHello,'이지은') >> 이것을 decorator 사용해서
printHello('홍길동') # 이렇게 실행 가능