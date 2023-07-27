# Classes 상속

2023.07.27(Thu)<br>

-----

## 상속 Inheritance
기존 클래스의 속성과 메서드를 물려받아 새로운 하위 클래스를 생성하는 것
- 상속이 필요한 이유
  - 코드 재사용
    - 상속을 통해 기존 클래스의 속성과 메서드 재사용 가능
    - 새로운 클래스를 작성할때 기존 클래스의 기능을 활용하여 코드의 중복을 줄임
  - 계층 구조
    - 상속을 통해 클래스들 간의 계층 구조를 형성할 수 있음
    - 부모 클래스와 자식 클래스 간의 관계를 표현하고 더 구체적인 클래스를 만들 수 있음
  - 유지 보수의 용이성
    - 상속을 통해 필요한 클래스만 수정
    - 코드의 일관성 유지, 수정이 필요한 범위 최소화

### 클래스 상속
상속을 사용한 계층구조 변경 예
```
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def talk(self) : # 메서드 재사용
        print(f'반갑습니다. {self.name}입니다.')


class Professor(Person): # 괄호 안에 부모 클래스의 이름 사용!
    def __init__(self, name , age, department):
        self.name = name
        self.age = age
        self.department = department


class Student(Person):
    def __init__(self, name, age, gpa):
        self.name = name
        self.age = age
        self.gpa = gpa


p1 = Professor('박교수', 49, '통계학과')
s1 = Student('김학생', 20, 3.5)

p1.talk() # >> 반갑습니다. 박교수입니다.
s1.talk() # >> 반갑습니다. 김학생입니다.
```
상속을 이용하면 부모  Person 클래스의 talk 메서드를 자식 클래스안에서 사용할 수 있음

- super()
  - 부모 클래스의 메서드를 호출하기 위해 사용되는 내장 함수
  - 사용 전
    ```
    class Person:
        def __init__(self, name, age , number , email):
            self.name = name
            self.age = age
            self.number = number
            self.email = email


    class Student(Person):
        def __init__(self, name, age, number, email, student_id):
            self.name = name
            self.age = age
            self.number = number
            self.email = email
            self.student_id = student_id
    ```
  - 사용 후
    ```
    class Person:
        def __init__(self, name, age , number , email):
            self.name = name
            self.age = age
            self.number = number
            self.email = email


    class Student(Person):
        def __init__(self, name, age, number, email, student_id):
            # 부모클래스의 init 메서드 호출
            super().__init__(name, age, number, email)
            self.student_id = student_id
    ```

### 다중 상속
- 다중 상속
  - 두 개 이상의 클래스를 상속 받는 경우
  - 상속받은 모든 클래스의 요소를 활용 가능함
  - 중복된 속성이나 메서드가 있는 경우 **상속 순서에 의해 결정**됨
  ```
  class Person:
      def __init__(self, name):
          self.name = name

      def greeting(self) : 
          return f'안녕, {self.name}'


  class Mom(Person):
      gene = 'XX'
      
      def __init__(self, name #, age): 
          super().__init__(name)
          # (case 1) 만약 age를 mom에게만 추가한다면
          # self.age = age

      def swim(self):
          return '엄마가 수영'


  class Dad(Person):
      gene = 'XY'

      def __init__(self, name, age):  
          super().__init__(name)
        
      def walk(self):
          return '아빠가 걷기'


  class FirstChild(Dad, Mom):
      def __init(self, name):
          super().__init(name)
          # (case 1) 상속 순서가 낮은 Mom의 age를 받기 위해 super() 대신 __init__을 직접 사용해야함
          # Mom.__init__(self, name , age)

      def swim(self):
          return '첫째가 수영'
      
      def cry(self):
          return '첫째가 응애'


  baby1 = FirstChild('아기') # 최상위 class인 Person에 초기값으로 name이 필요
  print(baby1.cry()) # >> 첫째가 응애
  print(baby1.swim()) # >> 첫째가 수영
  print(baby1.walk()) # >> 아빠가 걷기
  print(baby1.gene) # >> XY
  ```
    - 각각의 부모 클래스에 gene 속성이 모두 들어있는 경우 , 상속 순서가 빠른 Dad 의 gene 속성을 가짐
    - 만약 Mom의 유전자 정보를 받고 싶다면? 내부에서 직접 속성 호출
      ```
      class FirstChild(Dad, Mom):
        mom_gene = Mom.gene
        def swim(self):
          return '첫째가 수영'
        
        def cry(self):
          return '첫째가 응애'  
      ``` 
  - 상속 관련 함수와 메서드
  - mro() 메서드
    - Method Resolution Order
    - 해당 인스턴스의 클래스가 어떤 부모 클래스를 가지는지 확인하는 메서드
    - 기존의 인스턴스 -> 클래스 순으로 이름 공간을 탐색하는 과정에서 **상속 관계에 있으면 인스턴스 -> 자식 클래스 -> 부모 클래스로 확장**
    ```
    print(FirstChild.mro())

    # >> [<class '__main__.FirstChild'>, <class '__main__.Dad'>, <class '__main__.Mom'>, <class '__main__.Person'>, <class 'object'>]
    ```
    - 이 순서가 상속에 의한 탐색의 순서

## 에러와 예외 Errors & Exception

### 디버깅
- 버그 : 소프트웨어에서 발생하는 오류 또는 결함, 프로그램의 예상된 동작과 실제 동작 사이의 불일치
- Debugging : 소프트웨어에서 발생하는 버그를 찾아내고 수정하는 과정

### 에러
- Syntax Error : 프로그램의 구문이 올바르지 않은 경우 발생
  - Invalid syntax : 문법 오류
  - assign to literal : 잘못된 할당
  - EOL : End of Line 
  - EOF : End of File

### 예외 Exception
- 프로그램 실행 중 감지되는 에러
- 내장 예외 : 예외 상황을 나타내는 예외 클래스들
  - ZeroDevisionError: division by zero 인 경우 발생
  - NameError: 지역/전역 이름을 찾을 수 없을 때 발생
  - TypeError 
    - 타입 불일치 
      ```
      '2' + 2
      ```
    - 인자 누락
      ```
      sum()
      ```
    - 인자 초과
      ```
      sum(1, 2, 3)
      ```
    - 인자 타입 불일치
      ```
      import random
      random.sample(1,2)
      ```
  - ValueError : 연산, 함수에 문제가 없지만 부적절한 값을 가진 인자를 받았고, 상황이 IndexError 처럼 더 구체적인 예외로 설명되지 않는 경우 발생
    ```
    int('1.5')
    range(3).index(6)
    ```

  - IndexError : 시퀀스 인덱스가 범위를 벗어날 때 발생
    ```
    empty_list = []
    empty_list[2]
    ``` 
  - KeyError : 딕셔너리에 해당 키가 존재하지 않는 경우
  - ModuleNotFoundError : 모듈을 찾을 수 없을때 발생
  - ImportError : 임포트 하려는 이름을 찾을 수 없을때 발생
  - Keyboardinterrupt : 사용자가 ctrl-c 또는 Delete를 누를 때 (무한루프 시 강제 종료)
  - IndentationError : 잘못된 들여쓰기와 관련된 문법 오류

### 예외 처리
try - except 구조
- try 블록 안에는 예외가 발생할 수 있는 코드를 작성
- except 블록 안에는 예외가 발생했을 때 처리할 코드를 작성
- 예외가 발생하면 try 블록을 빠져나와 해당 예외에 대응하는 except 블록으로 이동

  ```
  # (e.g.1)

  try : 
      result = 10 / 0 
  except ZeroDivisionError :
      print('0으로 나눌 수 없습니다.')

  # >> 0으로 나눌 수 없습니다.


  # (e.g.2)
  try :
      result = int(input('숫자입력 : '))
  except ValueError :
      print('숫자가 아닙니다')

  # >> 숫자 입력 : a
  # >> 숫자가 아닙니다.


  # (e.g.3)
  try :
      num = int(input('100으로 나눌 값을 입력하시오 : '))
      print(100/num)
  except ZeroDivisionError :
      print('0으로는 나눌수 없자나요')
  except ValueError :
      print('숫자로 입력하세요 짱나게 하지 말고')
  except : 
      print('에러가 발생했습니다')
  ```
- 발생가능한 에러를 모두 명시하기도 가능
  ``` 
  try :
      num = int(input('100으로 나눌 값을 입력하시오 : '))
      print(100/num)
  except (ValueError, ZeroDivisionError) :
      print('에러가 발생했습니다')
  ```
- 내장 예외의 상속 계층구조 주의
  - 내장 예외 클래스는 상속 계층구조를 가지기 때문에 반드시 **하위 클래스를 먼저 확인할 수 있도록 작성해야 함**
  - [이곳](https://docs.python.org/3/library/exceptions.html#exception-hierarchy)에서 Exception hierachy 확인 가능
  ```
  # Bad
  try :
      num = int(input('100으로 나눌 값을 입력하시오 : '))
      print(100/num)
  except BaseException :
      print('숫자를 넣어줘')
  except ZeroDivisionError :
      print('0으로는 나눌수 없자나요')
  except : 
      print('에러가 발생했습니다')

  # good
  try :
      num = int(input('100으로 나눌 값을 입력하시오 : '))
      print(100/num)
  except ZeroDivisionError :
      print('0으로는 나눌수 없자나요')
  except BaseException :
      print('숫자를 넣어줘')
  except : 
      print('에러가 발생했습니다')
  ```

## EAFP & LBYL
예외처리와 값 검사에 대한 2가지 접근 방식
### EAFP
Easier to Ask for Forgiveness than Permission<br>
예외처리를 중심으로 코드를 작성하는 접근 방식(try-except)
```
try : 
    result = my_dict['key']
except KeyError: 
    print('Key가 존재하지 않습니다.')
```
예외 상황을 예측하기 어려운 경우에 유용
### LBYL
Look Before You Leap<br>
값 검사를 중심으로 코드를 작성하는 접근 방식(if-else)<br>
```
if 'key' in my_dict:  
    result = my_dict['key']
    print(result)
else:
  print('Key가 존재하지 않습니다.')
```
예외 상황을 미리 방지하고 싶을 때 유용  

## 참고
### as 키워드
- as 키워드를 활용하여 에러 메시지를 except 블록에서 사용할 수 있음
```
my_list = []

try : 
    result = my_list[1]
except IndexError as error : 
    print(f'{error}가 발생했습니다.')

# >> list index out of range가 발생했습니다.
```