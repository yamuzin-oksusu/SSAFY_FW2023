# Basic syntax of JavaScript

2023.10.24 (Tue)
-----
## 변수
[JS 권장 스타일 가이드](https://standardjs.com/rules-en)
### 식별자(변수명) 작성 규칙
- 반드시 문자, 달러($)또는 밑줄(_)로 시작
- 대소문자를 구분
- 예약어 사용 불가 : for, if, function 등
- 카멜 케이스(CamelCase) : 변수, 객체, 함수에 사용
- 파스칼 케이스(PascalCase) : 클래스, 생성자에 사용
- 대문자 스네이크 케이스(SNAKE_CASE) : 상수(constants)에 사용
### 변수 선언 키워드 : let, const, var
- let 
  - 블록 스코프(block scope)를 갖는 지역 변수를 선언
  - 재할당 가능
  - 재선언 불가능
  - ES6에서 추가
    ```
    let number // undefined 
    number = 20 //재할당 가능, number에 값을 할당하지 않고 이후에 할당이 가능
    console.log(number)
    let number = 20 // 재선언 불가능
    ```
- const
  - 블록 스코프(block scope)를 갖는 지역 변수를 선언
  - 재할당 불가능
  - 재선언 불가능
  - ES6에서 추가
    ```
    const number1 = 10
    number1 = 15 // 재할당 불가능
    const number1 // 재선언 불가능 Cannot redeclare block-scoped variable 'number1'
    console.log(number1)
    ```
- block scope
  - if, for, 함수 등의 '중괄호({})내부'를 가리킴
  - 블록 스코프를 가지는 변수는 블록 바깥에서 접근 불가능<br>
    ```
    let x = 1
    if (x === 1) {
    let x = 2
    console.log(x) // 2
    }
    console.log(x) // 1
    ```

- 변수 선언 키워드 정리
  - 기본적으로 const 사용을 권장
  - 재할당이 필요한 변수는 let으로 변경해서 사용

## 데이터 타입
### 데이터 타입
- 원시 자료형 (Primitive type) : Number, String, Boolean, undefined, null
  - 변수에 값이 직접 저장되는 자료형 (불변, 값이 복사)
  - 변수 간 서로 영향을 미치지 않음

- 참조 자료형 (Reference type) : Objects(Object, Array, Function)
  - 객체의 (메모리) 주소가 저장되는 자료형 (가변, 주소가 복사)
  - 변수 간에 서로 영향을 미침

### 원시 자료형
- Number : 정수 또는 실수형 숫자를 표현하는 자료형
- String : 텍스트 데이터를 표현하는 자료형
  - '+' 연산자를 사용해 문자열끼리 결합
  - 곱셈, 나눗셈, 뺄셈 불가능
- Template literals
  - 내장된 표현식을 허용하는 문자열 작성 방식
  - Backtick(``)을 이용하며, 여러 줄에 걸쳐 문자열을 정의할 수도 있고 JavaScript의 변수를 문자열 안에 바로 연결할 수 있음
  - 표현식은 $ 와 중괄호 ( ${expression} ) 로 표기
  - ES6+ 부터 지원
    ```
    const age = 100
    const message = `홍길동은 ${age}세 입니다.`
    console.log(message)
    ```
- null과 undefined
  - null : 변수의 값이 없음을 의도적으로 표현할 때 사용
    ```
    let a = null
    console.log(a) // null
    ```
  - undefined : 변수 선언 이후 직접 값을 할당하지 않으면 자동으로 할당됨
    ```
    let b
    console.log(b) // undefined
    ```
  - '값이 없음'에 대한 표현이 null과 undefined 2가지인 이유
    - JavaScript의 설계 실수
    - null이 원시자료형임에도 불구하고 object로 출력되는 이유는 JavaScript 설계 당시의 버그를 해결하지 않은 것
    - 해결하지 못하는 이유는 이미 null 타입에 의존성을 띄고 있는 수 많은 프로그램들이 망가질 수 있기 때문 (하위 호환 유지)

- Boolean (true/false)
  - 조건문 또는 반복문에서 Boolean이 아닌 데이터 타입은 '자동 형변환 규칙'에 따라 true 또는 false로 변환됨

- 자동 형변환

    | 데이터 타입 | false | true |
    |:---:|:---:|:---:|
    |undefined|항상 false|X|
    |null|항상 false|X|
    |Number|0 , -0 , NaN|나머지 모든 경우|
    |String|빈 문자열|나머지 모든 경우|
## 연산자
### 할당 연산자
- 오른쪽에 있는 피연산자의 평가 결과를 왼쪽 피연산자에 할당하는 연산자
- 단축 연산자 지원
```
```
### 증가 & 감소 연산자
- 증가 연산자(++)
  - 피연산자를 증가(1을 더함)시키고 연산자의 위치에 따라 증가하기 전이나 후의 값을 반환
- 감소 연산자(--)
  - 피연산자를 감소(1을 뺌)시키고 연산자의 위치에 따라 감소하기 전이나 후의 값을 반환
```
// 전위 연산자
let a = 3
const b = ++a
console.log(a, b) // 4 4



// 후위 연산자
let x = 3
const y = x++
console.log(x, y) // 4 3
```
> +=또는 +=와 같이 더 명시적인 표현으로 작성하는 것을 권장
### 비교 연산자
- 피연산자들(숫자, 문자, Boolean 등)을 비교하고 결과값을 boolean으로 반환하는 연산자
### 동등 연산자 (==)
- 두 피연산자가 같은 값으로 평가되는지 비교 후 boolean값을 반환
- '암묵적 타입 변환'을 통해 타입을 일치시킨 후 같은 값인지 비교
- 두 피연산자가 모두 객체일 경우 메모리의 같은 객체를 바라보는지 판별
### 일치 연산자 (===)
- 두 피연산자의 값과 타입이 모두 같은 경우 true를 반환
- 같은 객체를 가리키거나, 같은 타입이면서 같은 값인지를 비교
- 엄격한 비교가 이뤄지며 암묵적 타입 변환이 발생하지 않음
- 특수한 경우를 제외하고는 동등 연산자가 아닌 **일치 연산자** 사용 권장

### 논리 연산자
- and 연산 : &&
- or 연산 : ||
- not 연산 : !
- 단축 평가 지원 

## 조건문
### if
조건 표현식의 결과값을 boolean 타입으로 변환 후 참/거짓을 판단

```
const name = 'minjoo'

if (name === 'admin') {
    console.log('1')
} else if (name === 'minjoo') {
    console.log('2')
} else {
    console.log('3')
} 

// output : 2
```
### 조건 (삼항) 연산자
- 세 개의 피연산자를 받는 유일한 연산자
- 앞에서부터 조건문, 물음표(?), 조건문이 참일 경우 실행할 표현식, 콜론(:), 조건문이 거짓일 경우 실행할 표현식이 배치
```
const person = 100

if (person > 17) {
    return 'YES'
} else {
    return 'NO'
}

// 위 표현식을 조건 연산자로 표현

person > 17 ? 'YES' : 'NO'
```
## 반복문
### while 
조건문이 참이면 문장을 계속해서 수행
```
let i = 0
while (i < 6) {
    console.log(i)
    i += 1
}

// 0
// 1
// 2
// 3
// 4
// 5
```
### for
특정한 조건이 거짓으로 판별될 때까지 반복
```
for ([초기문]; [조건문]; [증감문]) {
    //do something
}
```
```
for (let i = 0 ; i < 6 ; i ++) {
    console.log(i)
}
```
### for...in
객체의 열거 가능한 속성(property)에 대해 반복
```
for (variable in object) {
    statement
}
```
```
const fruits = {
    a : 'apple',
    b : 'banana'
}

for (const property in fruits) {
    console.log(fruits[property])
}

// apple
// banana
```
### for...of
반복 가능한 객체(배열, 문자열 등)에 대해 반복
```
for (variable of iterable) {
    statement
}
```
```
const numbers = [0,1,2,3]
for (const number of numbers) {
    console.log(number)
}

// 0
// 1
// 2
// 3
```
### 배열 반복과 for...in
- 배열의 인덱스는 정수 이름을 가진 열거 가능한 속성
- for...in은 정수가 아닌 이름과 속성을 포함하여 **열거 가능한 모든 속성**을 반환
- 내부적으로 for...in은 배열의 반복자 대신 속성 열거를 사용하기 때문에 특정 순서에 따라 인덱스를 반환하는 것을 보장할 수 없음
> 인덱스의 순서가 중요한 배열에서는 사용하지 않음 <br>
> 배열에서는 **for 반복, for...of 반복**을 사용
```
// wrong
const numbers2 = ['a','b','c','d']
for (const number in numbers2){
    console.log(number)
}
// 0
// 1
// 2
// 3

// right
const numbers2 = ['a','b','c','d']
for (const number of numbers2){
    console.log(number)
}
// a
// b
// c
// d
```
### 반복문 사용 시 const 사용 여부
for 문
- `for (let i = 0 ; i <arr.length; i++) {...}`의 경우에는 최초 정의한 i를 "재할당"하면서 사용하기 때문에 **const를 사용하면 에러 발생**

for...in, for...of
- 재할당이 아니라, 매 반복마다 다른 속성 이름이 변수에 지정되는 것이므로 **const를 사용해도 에러가 발생하지 않음**
- 단, const 특징에 따라 블록 내부에서 변수를 수정할 수 없음

### 반복문 종합
| 키워드 | 연관 키워드 | 스코프 |
|:---:|:---:|:---:|
|while|break, continue|블록 스코프|
|for|break, continue|블록 스코프|
|for...in|object 순회|블록 스코프|
|for...of|iterable 순회|블록 스코프|
### 참고
- 세미콜론 (semicolon)
  - JS는 세미콜론을 선택적으로 사용 가능
  - 세미콜론이 없으면 ASI에 의해 자동으로 세미콜론이 삽입됨
    - ASI(Automatic Semicolon Insertion, 자동 세미콜론 삽입 규칙)
- 변수 선언 키워드 - 'var'
  - ES6 이전 변수 선언에 사용했던 키워드
  - 재할당 가능 & 재선언 가능
  - '호이스팅'되는 특성으로 인해 예기치 못한 문제 발생 가능
    - 따라서 ES6 이후부터는 var 대신 const와 let을 사용하는 것을 권장
  - 함수 스코프(function scope)를 가짐
  - 변수 선언 시 var, const, let 키워드 중 하나를 사용하지 않으면 자동으로 var로 선언됨

- 함수 스코프(function scope)
  - 함수의 중괄호 내부를 가리킴
  - 함수 스코프를 가지는 변수는 함수 바깥에서 접근 불가능

- 호이스팅
  - 변수를 선언 이전에 참조할 수 있는 현상
  - 변수 선언 이전의 위치에서 접근 시 undefined를 반환
  - JS에서 변수들은 실제 실행시에 코드의 최상단으로 끌어올려지게 되며(hoisted)이러한 이유 때문에 var로 선언된 변수는 선언 시에 undefined로 값이 초기화되는 과정이 동시에 발생
    ```
    console.log(name) //undefined
    var name = '홍길동'

    console.log(age) // ReferenceError: Cannot access 'age' before initialization
    let age = 30

    console.log(height) // ReferenceError: Cannot access 'height' before initialization
    const height = 170
    ```
- NaN을 반환하는 경우 예시
  - 숫자로서 읽을 수 없음 (Number(undefined))
  - 결과가 허수인 수학 계산식 (Math.sqrt(-1))
  - 피연산자가 NaN (7**NaN)
  - 정의할 수 없는 계산식(0*Infinity)
  - 문자열을 포함하면서 덧셈이 아닌 계산식('가'/3)
