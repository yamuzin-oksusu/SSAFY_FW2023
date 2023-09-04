# Fundamentals of HTML and CSS


2023.09.04(Mon) ~ 
-----

## Web 소개
**World Wide Web** : 인터넷으로 연결된 컴퓨터들이 정보를 공유하는 거대한 정보 공간<br>
**Web** : Web site, Web application등을 통해 사용자들이 정보를 검색하고 상호작용하는 기술<br>
**Website** :인터넷에서 여러 개의 Web page가 모인 것으로 사용자에게 정보나 서비스를 제공하는 공간<br>
**Web page** : HTML, CSS 등의 웹 기술을 이용하여 만들어진, **Web site를 구성하는 하나의 요소**<br>
- Web page 구성 요소 
  - HTML(Structure) / CSS(Styling) / JS(Behavior)


## Web 구조화

### HTML
HyperText Markup Language : 웹 페이지의 의미와 **구조**를 정의하는 언어
- Hypertext : 웹 페이지를 다른 페이지로 연결하는 링크, 참조를 통해 사용자가 한 문서에서 다른 문서로 즉시 접근할 수 있는 텍스트
- Markup Launguage : 태그 등을 이용하여 문서나 데이터의 구조를 명시하는 언어 ex. HTML, Markdown

### HTML의 구조
[<참고>](https://tcpschool.com/html-tags/meta)
- `<!DOCTYPE html>` 
  - 해당 문서가 html 문서라는 것을 나타냄
- `<html></html>`
  - 전체 페이지의 콘텐츠를 포함
- `<title></title>`
  - 브라우저 탭 및 즐겨찾기 시 표시되는 제목으로 사용
- `<head></head>`
  - HTML 문서에 관련된 설명, 설정 등
  - **사용자에게 보이지 않음**
  - `<meta>`
    - 해당 문서에 대한 정보인 메타데이터를 정의할 때 사용
    - 언제나 `<head>`요소 내부에 위치
- `<body></body>` 
  - **페이지에 표시되는 모든 콘텐츠**
  - `<a></a>` 
    - 하이퍼텍스트를 만드는 태그
    - `<a href= '../../'>` 와 같이 Tag 속성에 링크 주소 작성
  - `<img src = '이미지 경로' alt = ''>` 
    - 이미지 삽입하는 태그 
    - alt를 꼭 사용할것( for universal reason)
```
## Tip ) ! + Tab >> 자동완성
<!DOCTYPE html>
<html lang="en"> # 해당 문서의 언어 명시함

<head>
  <meta charset="UTF-8">
  <meta http-equiv="X-UA-Compatible" content="IE=edge">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Document</title>
  <style>
  </style>
</head>

<body>
  <h1>Heading</h1>
  <h2>선택자</h2>
  <h3>연습</h3>
  <h4>반가워요</h4>
  <p>과목 목록</p>
  <ul>
    <li>파이썬</li>
    <li>알고리즘</li>
    <li>웹
      <ol>
        <li>HTML</li>
        <li>CSS</li>
        <li>PYTHON</li>
      </ol>
    </li>
  </ul>
  <p>Lorem, <span>ipsum</span> dolor.</p>
</body>

</html>
```
- HTML Element(요소)

    ![HTML Element](https://github.com/yamuzin-oksusu/SSAFY_FW2023/blob/master/images/image-5.png)
  - 하나의 요소는 여는 태그와 닫는 태그 그리고 그 안의 내용으로 구성됨
  - 닫는 태그는 태그 이름 앞에 슬래시가 포함되며 닫는 테그가 없는 태그도 존재

- HTML Attributes(속성)
    ![HTML Attributes](https://github.com/yamuzin-oksusu/SSAFY_FW2023/blob/master/images/image-6.png)
  - 규칙
    - 속성은 요소 이름과 속성 사이에 공백이 있어야 함
    - 하나 이상의 속성들이 있는 경우엔 속성 사이에 공백으로 구분함
    - 속성 값은 열고 닫는 따옴표로 감싸야 함
  - 목적
    - 나타내고 싶지 않지만 추가적인 기능, 내용을 담고 싶을 때 사용
    - CSS에서 해당 요소를 선택하기 위한 값으로 활용됨
### 텍스트 구조
HTML의 주요 목적 중 하나는 텍스트 구조와 의미를 제공하는 것
```
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>
    <h1>main heading</h1>
    <h2>sub heading</h2>
    <p>This is my page</p>
    <p>This is <em>emphasis</em></p>
    <p>hi my name is <strong>MinjooKim</strong></p>
    <ol>
        <li>파이썬</li>
        <li>알고리즘</li>
        <li>웹</li>
    </ol>
    <ul>
        <li>이것은</li>
        <li>unordered list</li>
        <li>입니다.</li>
    </ul>
    <p>Tag의 들여쓰기는 HTML 문법에 영향을 주지 않지만 편의를 위해 사용함</p>
    <p>HTML은 구조를 눈으로 찾으면서 Debugging 필요함. 항상 <strong>개발자 도구를 이용해서 확인</strong></p>
</body>
</html>
```
## Web 스타일링

### CSS
- CSS (Cascading Style Sheet)
  - 웹 페이지의 디자인과 레이아웃을 구성하는 언어
- CSS 구문
![CSS 구문](https://github.com/yamuzin-oksusu/SSAFY_FW2023/blob/master/images/image-7.png)
  - CSS 적용 방법
    1. Inline 스타일
       - THML 요소 안에 style 속성 값으로 작성
       - 거의 사용하지 않음
        ```
        <body>
            <h1 style="color: blueviolet; background-color: burlywood;">main heading</h1>
        </body>
        ```
    2. Internal 스타일 시트
        - head 태그 내부 style 태그에 작성
        ```
        <style>
            /* 모든 h2 요소의 txt 색을 주황색으로 변경 */
            h2 {
                color : orange;
            }
        ```

    3. External 스타일 시트
        - 별도의 CSS 파일 생성 후 HTML link 태그를 사용해 불러오기

        ```
        <head>
            ...
            <link rel = 'stylesheet' href = 'style.css'>
        </head>
        ```
        ```
        /* style.css */
        h1 {
            color : blue;
            background-color : yellow;
        }
        ```


### CSS 선택자
- CSS Selectors 
  - HTML 요소를 선택하여 스타일을 적용할 수 있도록 하는 선택자
- CSS Selectors 종류
  - 기본 선택자
    - 전체(*) 선택자
      - HTML 모든 요소를 선택
    - 요소(tag) 선택자
      - 지정한 모든 태그를 선택
    - **클래스(class) 선택자 ('.' (dot))**
      - 주어진 클래스 속성을 가진 모든 요소를 선택
    - 아이디(id) 선택자 ('#')
      - 주어진 아이디 속성을 가진 요소 선택
      - 문서에는 주어진 아이디를 가진 요소가 하나만 있어야 함
    - 속성(attr) 선택자 등

    ```
    <head>
        ...
        <style>
            * {
                color: aquamarine; background-color: black;
            }
            /* 모든 h2 요소의 txt 색을 주황색으로 변경 */
            h2 {
                color : orange;
            }
            h3, h4 {
                color: beige;
            }
            .green {
                color: greenyellow;
            }
            #purple {
                color: purple;
            }
        </style>
    </head>
    <body>
        <h1>main heading</h1>
        <h2>sub heading</h2>
        <h3>점점 더 깊어지는</h3>
        <h4 class = 'green'>headings</h4>
        ...
        <p class = 'green'>hi my name is <strong id="purple">MinjooKim</strong></p>
        ...
    </body>
    ```

  - 결합자 (Combinatiors)
    - 자손 결합자 ("" (space))
      - 첫번째 요소의 자손 요소들 선택
      - ex. p span은 <p>안에 있는 모든 <span>을 선택 **(하위 레벨 상관 없이)**
    - 자식 결합자 (">")
      - 첫번째 요소의 직계 자식만 선택
      - ex. ul > li 은 <ul> 안에 있는 모든 <li>를 선택 **(한단계 아래 자식들만)**
### CSS 상속
기본적으로 CSS는 상속을 통해 부모 요소의 속성을 자식에게 상속해 재사용성을 높임
= 상속 여부
    - 상속되는 속성
      - Text 관련 요소(font, color, text=align), opacity, visibility 등
    - 상속되지 않는 속성
      - Box model 관련 요소(width, height, border, box-sizing ...)
      - position 관련 요소(position, top/right/bottom/left, z-index) 등

### 우선순위
- Specificity
  - 동일한 요소에 적용 가능한 같은 스탇일을 두 가지 이상 작성했을 때 어떤 규칙이 적용되는지 결정하는 것
  - **Cascade**(계단식) Style Sheet
    - 동일한 우선순위를 갖는 규칙이 적용될 때 CSS에서 마지막에 나오는 규칙이 사용됨
- 우선순위가 높은 순 
  1. Importance
     - !importance : 다른 우선순위 규칙보다 우선하여 적용하는 키워드 (구조를 무시하고 강제로 스타일을 적용하므로 사용 권장하지 않음)
  2. Inline 스타일
  3. 선택자
     - id 선택자 > class 선택자 > 요소 선택자
  4. 소스 코드 순서
- web 구성이 복잡해질 수록 우선순위를 고려한 구성이 어렵기 때문에 Clss 선택자만 사용하는 것을 권장
- head 내의 style 코드의 순서가 규칙이 적용되는 순서임. (not class= " ... " 에서의 순서)

### HTML 관련 권장 사항
- 요소(Tag)이름은 대소문자를 구분하지 않지만 소문자 사용을 권장
- 속성의 따옴표는 작은 따옴표와 큰 따옴표를 구분하지 않지만 큰따옴표 사용권장
- HTML은 프로그래밍 언어와 달리 에러를 반환하지 않기 때문에 작성 시 주의
- inline style은 구조 정보 혼합의 위험이 있으므로 코드를 이해하기 어렵게 만듦
- CSS의 모든 속성을 외우는 것이 아님. 개발하며 필요할 때마다 검색해서 학습 후 사용

[표준 문서 MDN](https://developer.mozilla.org/en-US/)