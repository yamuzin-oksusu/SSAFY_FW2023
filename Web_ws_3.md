# Fundamentals of Bootstrap

2023.09.06.(Wed) 
-----
## Bootstrap
### 개요
> CSS 프론트엔드 프레임워크(Toolkit)

[실습코드](https://github.com/yamuzin-oksusu/SSAFY_FW2023/blob/master/Web_ws_3_1.html)<br>

**미리 만들어진 다양한 디자인 요소들을 제공하여 웹 사이트를 빠르고 쉽게 개발할 수 있도록 함**<br>

[공식문서](https://getbootstrap.com/)

- Bootstrap에서 클래스 이름으로 Spacing을 표현하는 방법
  - Property
    |약어|의미|
    |:---:|:---:|
    |m|margin|
    |p|padding|
  - Sides
    |약어|의미|
    |:---:|:---:|
    |t|top|
    |b|bottom|
    |s|left|
    |e|right|
    |y|top, bottom|
    |x|left, right|
    |blank|4 sides|
  - Size
    |bootstrap Size|rem|Original Size|
    |:---:|:---:|:---:|
    |0|0 rem|0px|
    |1|0.25 rem|4px|
    |2|0.5 rem|8px|
    |3|1 rem|16px|
    |4|1.5 rem|24px|
    |5|3 rem|48px|
    |auto|auto|auto|

**Bootstrap에는 특정한 규칙이 있는 클래스 이름으로 이미 스타일 및 레이아웃이 작성되어 있음**


**Bootstrap Component**<br>
Bootstrap에서 제공하는 UI 관련 요소 (버튼, 네비게이션 바, 카드, 폼, 드롭다운 등)

## Semantic Web

### 개요
> **웹 데이터를 의미론적으로 구조화된 형태로 표현하는 방식**<br> 검색엔진 및 개발자가 웹 페이지 콘텐츠를 이해하기 쉽도록
### Semantic in HTML
- semantic element
  - header
  - nav
  - main
  - article
  - section
  - aside
  - footer
### Semantic in CSS
OOCSS(Object Oriented CSS)
- 객체 지향적 접근법을 적용하여 CSS를 구성하는 방법론

CSS 방법론
- CSS를 효율적이고 유지 보수가 용이하게 작성하기 위한 일련의 가이드라인

OOCSS 기본 원칙
1. 구조와 스킨을 분리
   - 구조와 스킨을 분리함으로써 재사용 가능성을 높임
   - 모든 버튼의 공통 구조를 정의 + 각각의 스킨(배경색과 폰트 색상)을 정의  
2. 컨테이너와 콘텐츠를 분리
   - 객체에 직접 적용하는 대신 객체를 둘러싸는 컨테이너에 스타일을 적용
   - 스타일을 저으이할 때 위치에 의존적인 스타일을 사용하지 않도록 함
   - 콘텐츠를 다른 컨테이너로 이동시키거나 재배치할 때 스타일이 깨지는 것을 방지 