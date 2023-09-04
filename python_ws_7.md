# Classes

2023.07.26(Wed)
-----
## 객체지향 프로그래밍

### 절차 지향 프로그래밍 Procedural Programming
- 프로그램을 '데이터'와 '절차'로 구성하는 방식의 프로그래밍 패러다임<br>
- '데이터'와 해당 데이터를 처리하는 '함수'가 분리되어 있으며, 함수 호출의 흐름이 중요 <br>
- 코드의 순차적인 흐름과 함수 호출에 의해 프로그램이 진행<br>
- 실제로 실행되는 내용이 무엇이 무엇인가가 중요<br>
- 데이터를 다시 재사용하기 보다는 처음부터 끝까지 실행되는 결과물이 중요
- 소프트웨어 위기
  - 하드웨어의 발전으로 컴퓨터 계산 용량과 문제의 복잡성이 급격히 증가함에 따라 소프트웨어에 발생한 충격

### 객체 지향 프로그래밍 Object Oriented Programming
- 데이터와 해당 데이터를 조작하는 메서드를 하나의 객체로 묶어 관리하는 방식의 프로그래밍 패러다임<br>
- 데이터와 해당 데이터를 처리하는 메서드(메시지)를 하나의 객체(클래스)로 묶음<br>
- 객체 간 상호작용과 메시지 전달이 중요



## 객체
클래스에서 정의한 것을 토대로 메모리에 할당된 것 <br>
**속성과 행동으로 구성된 모든 것**<br>


### 클래스와 객체
- 클래스로 만든 객체를 인스턴스라고 함

![클래스와 객체](\https://github.com/yamuzin-oksusu/SSAFY_FW2023/blob/master/images/image.png)
- 붕어빵은 객체다(O) 
- 붕어빵은 인스턴스다 (X)
- 붕어빵은 붕어빵틀의 인스턴스다 (O)

- 클래스를 만든다 == **타입**을 만든다
  ```
  name = 'Alice'
  print(type(name)) #<class 'str'>
  ```
  - 변수 name의 타입은 str 클래ㅅ다.
  - 변수 name은 str 클래스의 인스턴스이다. 
  - 우리가 사용해왔던 데이터 타입은 사실 모두 클래스였다.
- 'hello' , '파이썬' : 문자열 타입(클래스)의 객체(인스턴스)
- [1,2,3] , [] , ['hi'] : 리스트 타입(클래스)의 객체(인스턴스)

### 인스턴스와 메서드 
- 'hello'.upper() == 문자열.대문자로() == 객체.행동() == 인스턴스.메서드() 
- 하나의 객체(object)는 특정 타입의 인스턴스(instance)이다.
  - 130, 900, 5 : 모두 int의 인스턴스
  - [1,63,30] , []  : list의 인스턴스

### 객체(object)의 특징
- type : 어떤 연산자(operator)와 조작(method)이 가능한가?
- attribute : 어떠 상태(데이터)를 가지는가?
- method : 어떤 행위(함수)를 할 수 있는가?


## 클래스
파이썬에서 타입을 표현하는 방법<br>
객체를 생성하기 위한 설계도<br>
데이터와 기능을 함께 묶는 방법을 제공<br>

- 클래스 기본 활용
```
# 클래스 정의
class Person:
    blood_color = 'red'

    def __init__(self,name):
        self.name = name
    
    def singing(self):
        return f'{self.name}가 노래합니다.'

#인스턴스 생성
singer1 = Person('iu')

#메서드 호출
print(singer1.singing()) # >> iu가 노래합니다.

#속성(변수) 접근
print(singer1.blood_color) # >> red 

```

- \_\_init\_\_ 함수
  - 생성자 함수, 객체의 initialization(초기화)를 담당
  - 개발자가 직접 호출하지 않으며 instance 만들때 자동으로 호출됨.
  - 생성자 함수를 통해 instance를 생성하고 필요한 초기값을 설정

- self.name = name : 인스턴스 변수
  - 인스턴스(객체)마다 별도로 유지되는 변수
  - 인스턴스마다 독립적인 값을 가지며, **인스턴스가 생성될때마다 초기화됨**
  ```
  # 인스턴스 생성
  singer2 = Person('MJ') # 똑같은 클래스로 만든 다른 인스턴스
  ```

- blood_color = 'red' : 클래스 속성 / 클래스 변수
  - 클래스 내부에 선언된 변수
  - 클래스로 생성된 모든 인스턴스들이 공유하는 변수
  ```
  print(singer1.blood_color) # red
  print(singer2.blood_color) # red  
  ```

- singing(self): 인스턴스 메서드
  - 각각의 인스턴스에서 호출할 수 있는 메서드
  - 인스턴스 변수에 접근하고 수정하는 등의 작업을 수행

  ```
  #메서드 호출
  print(singer1.singing()) # >> iu가 노래합니다.
  print(singer2.singing()) # >> MJ가 노래합니다.
  ``````

- 인스턴스와 클래스 간의 이름공간(namespace)
  - 클래스를 정의하면, 클래스와 해당하는 이름 공간 생성
  - 인스턴스를 만들면, 인스턴스 객체가 생성되고 **독립적인**이름 공간 생성
  - 인스턴스에서 특정 속성에 접근하면 인스턴스 >> 클래스 순으로 탐색
  ```
  # Person 정의
  class Person :
      name = 'unknown'

      def talk(self) :
          print(self.name)
  
  p1 = Person()
  p1.talk() # >> unknown

  p2 = Person()
  p2 = talk() # >> unknown
  p2.name = 'Kim'
  p2.talk() # >> Kim

  print(Person.name) # >> unknown
  print(p1.name) # >> unknown
  print(p2.name) # >> Kim
  ```
- Class에 정의하지 않은 변수는 어떻게 출력될까?
  ```
  p1.address = 'korea'
  print(p1.address) # >> korea
  ```
  - address를 클래스에 정의하지 않더라도 p1.address가 출력된다
  - why? address는 instance 변수로서 정의되었기 때문에 클래스와는 무관하게 출력이 가능함.
- 독립적인 이름공간을 가지는 이점
  - 각 인스턴스는 독립적인 메모리 공간을 가지며, 클래스와 다른 인스턴스 간에는 서로의 데이터나 상태에 직접적인 접근이 불가능
  - 객체 지향 프로그래밍의 중요한 특성 중 하나, 클래스와 인스턴스를 모듈화하고 각각의 객체가 독립적으로 동작하도록 보장
  - 클래스와 인스턴스는 다른 객체들과의 상호작용에서 서로 충돌이나 영향을 주지 않으면서 독립적으로 동작할 수 있음
  - **코드의 가독성, 유지보수성, 재사용성을 높이는데 도움을 줌**


 
### instance 변수와 class 변수
- 클래스 변수 활용
  - 인스턴스가 생성 될 때마다 클래스 변수가 늘어나도록 설정할 수 있음
```
class Person:
    count = 0

    def __init__(self,name):
        self.name = name
        Person.count += 1

singer1 = Person('iu')
singer2 = Person('MJ')

print(Person.count) # >> 2
```
- 클래스 변수와 인스턴스 변수
  - 클래스 변수를 변경할때는 항상 클래스.클래스변수 형식으로 변경
```
class Circle():
    pi = 3.14
    def __init__(self.r):
        self.r = r

c1 = Circle(5)
c2 = Circle(10)

print(Circle.pi) # >> 3.14
print(c1.pi) # >> 3.14
print(c2.pi) # >> 3.14

Circle.pi = 5 # 클래스 변수 변경
print(Circle.pi) # >> 5
print(c1.pi) # >> 5
print(c2.pi) # >> 5

c2.pi = 5 # 인스턴스 변수 변경
print(Circle.pi) # >> 3.14
print(c1.pi) # >> 3.14
print(c2.pi) # >> 5
```

## 메서드

### 인스턴스 메서드
클래스로부터 생성된 각 인스턴스에서 호출할 수 있는 메서드<br>
인스턴스의 상태를 조작하거나 동작을 수행

- 인스턴스 메서드 구조
  - 클래스 내부에 정의되는 메서드의 기본
  - **반드시 첫번째 매개변수로 인스턴스 자신(self)를 전달받음**
  ```
  class MyClass :
      def instance_method(self, arg1, ...):
          pass
  ```
- self 동작 원리
  - upper메서드를 사용해 문자열 'hello'를 대문자로 변경하기
    ```
    # 인스턴스.메서드()
    'hello'.upper() 
    ```
  - 하지만 실제 파이썬 내부 동작은 다음과 같이 이루어진다.
    ```
    # 클래스.메서드(인스턴스 자기자신)
    str.upper('hello')
    ```
    - str 클래스가 upper 메서드를 호출했고, 그 첫번째 인자로 문자열 인스턴스가 들어간 것이다.
    - **인스턴스 메서드의 첫번째 매개변수가 반드시 인스턴스 자기 자신인 이유**
  - **인스턴스.메서드()** 는 클래스.메서드(인스턴스)를 객체 지향 방식의 메서드로 호출하는 표현이다.(단축형 호출)
  - 'hello'라는 문자열 객체가 단순히 어딘가의 함수로 들어가는 인자가 아닌 객체 스스로 메서드를 호출하여 코드를 동작하는 객체 지향적 표현

### 생성자 메서드 constructor method
- 인스턴스 객체가 생성될 때 자동으로 호출되는 메서드
- 인스턴스 변수들의 초기값을 설정
- 생성자 메서드 구조
  ```
  class Person:

      def __init(self):
          print('인스턴스가 생성되었습니다.')

  person1 = Person('MJ') # 인스턴스가 생성되었습니다.
  ```
### 클래스 메서드
- 클래스가 호출하는 메서드
- 클래스 변수를 조작하거나 클래스 레벨의 동작을 수행
- 클래스메서드 구조
  - @classmethod 데코레이터를 사용하여 정의
  - 호출 시, 첫번째 인자로 호출하는 클래스(cls)가 전달됨
  ```
  Class MyClass:

      @classmethod
      def class_method(cls,arg1, ...):
          pass
  ```
- e.g.
  ```
  class Person:
      count = 0

      def __init__(self,name):
          self.name = name
          Person.count += 1

      @classmethod
      def class_method(cls):
          print(f'인구수는 {cls.count}입니다.')

  singer1 = Person('iu')
  singer1 = Person('MJ')

  Person.number_of_population() # >> 인구수는 2입니다.
  ```
### 정적 메서드
- 클래스와 인스턴스 상관없이 독립적으로 동작하는 메서드
- 주로 클래스와 관련이 있지만 인스턴스와 상호작용이 필요하지 않은 경우에 사용
- 스태틱 메서드 구조
  - @staticmethod 데코레이터를 사용하여 정의
  - 호출 시, **필수적으로 작성해야 할 매개변수가 없음**
  - 객체 상태나 클래스 상태를 수정할 수 없으며 단지 기능(행동)만을 위한 메서드로 사용
  ```
  class MyClass:

      @staticmethod
      def static_method(arg1, ...):
          pass
  ```
- static method 예시
  ```
  class StringUtils:
      @staticmethod
      def reverse_string(string):
          return string[::-1]

      @staticmethod
      def capitalize_string(string):
          return string.capitalize()

  text = 'hello, world'

  reversed_text = StringUtils.reverse_string(text)
  print(reversed_text) # >> dlrow ,olleh

  capitalized_text = StringUtils.capitalize_string(text)
  print(capitalized_text) # >> Hello, world
  ```

### 메서드 정리
- instance method
  - 인스턴스의 상태를 변경하거나, 해당 인스턴스의 특정 동작을 수행
- class method 
  - 인스턴스 상태에 의존하지 않는 기능을 정의
  - 클래스 변수를 조작하거나 클래스 레벨의 동작을 수행
- static method
  - 클래스 및 인스턴스와 관련이 없는 일반적인 기능 수행
```
class MyClass:

    def instance_method(self):
        return 'instance method' , self
    
    @classmethod
    def class_method(cls):
        return 'class method' , cls
    
    @staticmethod
    def static_method():
        return 'static method'
```
- 클래스가 할 수 있는 것
  -  클래스는 모든 메서드를 호출할 수 있음
  - **하지만 클래스는 class method와 static method만 사용하도록 한다**
  ```
  instance = MyClass()

  print(MyClass.instance_method(instance)) 
  print(MyClass.class_method())
  print(MyClass.static_method())

  # >> ('instance method', <__main__.MyClass object at 0x000001FF4C7F3DC0>)
  # >> ('class method', <class '__main__.MyClass'>)
  # >> static method
  ```
- instance가 할 수 있는 것
  - 인스턴스는 모든 메서드를 호출할 수 있음
  - **하지만 instance는 instance method만 사용하도록 한다**
  ```
  instance = MyClass()

  print(instance.instance_method()) 
  print(instance.class_method())
  print(instance.static_method())
  # >> ('instance method', <__main__.MyClass object at 0x000001B665653DC0>)
  # >> ('class method', <class '__main__.MyClass'>)
  # >> static method
  ```

### 참고
- 매직 메서드
  - 특정 상황에 자동으로 호출되는 메서드
  ```
  class Circle:
      def __init__(self, r):
          self.r = r
      
      def area(self):
          return 3.14 * self.r * self.r

      def __str__(self):
          return f'[원] radius : {self.r}'
  
  c1 = Circle(10)
  c2 = Circle(1)

  print(c1) # >> [원] radius : 10
  print(c2) # >> [원] radius : 1
  ```
- 데코레이터 Decorator
  - 다른 함수의 코드를 유지한 채로 수정하거나 확장하기 위해 사용되는 함수
- 절차 지향과 객체 지향은 대조되는 개념이 아님
  - 객체 지향은 절차 지향을 기반으로 두고 보완하는 패러다임