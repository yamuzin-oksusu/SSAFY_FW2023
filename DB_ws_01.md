# SQL1

2023.10.10 (Tue)
-----

## Database
데이터베이스 역할 : 데이터를 저장하고 조작 (CRUD)
## Relational Database
- 관계형 데이터베이스 
  - 데이터 간에 관계가 있는 데이터 항목들의 모음
  - 테이블, 행, 열의 정보를 구조화하는 방식
  - 서로 관련된 데이터 포인터를 저장하고 이에 대한 엑세스를 제공
- 관계 
  - 여러 테이블 간의 (논리적) 연결
  - 관계로 인해 두 테이블을 사용하여 데이터를 다양한 형식으로 조회할 수 있음
### 관계형 데이터베이스 관련 키워드
- TABLE (aka RELATION)
  - 데이터를 기록하는 곳
- FIELD (aka COLUMN, ATTRIBUTE)
  - 각 필드에는 고유한 데이터 형식(타입)이 지정됨
- RECORD (aka ROW, TUPLE)
  - 각 레코드에는 구체적인 데이터 값이 저장됨
- DATABASE (aka SCHEMA)
  - 테이블의 집합
- PRIMARY KEY (기본 키)
  - 각 레코드의 고유한 값
  - 관계형 데이터베이스에서 레코드의 식별자로 활용
- FOREIGN KEY (외래 키)
  - 테이블의 필드 중 다른 테이블의 레코드를 식별할 수 있는 키
  - 다른 테이블의 기본 키를 참조
  - 각 레코드에서 서로 다른 테이블 간의 관계를 만드는 데 사용
### RDBMS
- DBMS(Database Management System): 데이터베이스를 관리하는 소프트웨어 프로그램
  - 데이터 저장 및 관리를 용이하게 하는 시스템
  - 데이터베이스와 사용자 간의 인터페이스 역할
  - 사용자가 데이터 구성, 업데이트, 모니터링, 백업, 복구 등을 할 수 있도록 도움
- RDBMS(Relational Database Management System): 관계형 데이터베이스를 관리하는 소프트웨어 프로그램   
  - 서비스 종류 : SQLite, MySQL, PostgreSQL, Oracle Database
    - SQLite : 경량의 오픈소스 데이터베이스 관리 시스템, 컴퓨터나 모바일 기기에 내장되어 간단하고 효율적인 데이터 저장 및 관리를 제공
- 데이터베이스 정리
  - Table은 데이터가 기록되는 곳
  - Table에는 행에서 고유하게 식별 가능한 기본 키라는 속성이 있으며, 외래 키를 사용하여 각 행에서 서로 다른 테이블 간의 관계를 만들 수 있음
  - 데이터는 기본 키 또는 외래 키를 통해 결합(join)될 수 있는 여러 테이블에 걸쳐 구조화 됨

## SQL
### SQL(Structure Query Language)
> 데이터베이스에 정보를 저장하고 처리하기 위한 프로그래밍 언어

### SQL Statements
> SQL을 구성하는 가장 기본적인 코드 블록
- 수행 목적에 따른 SQL Statements 4가지 유형

|유형|역할|SQL 키워드|
|:---:|:---:|:---:|
|DDL<br>(Data Definition Language)| 데이터의 기본 구조 및 형식 변경 |CREATE<br>DROP<br>ALTER|
|DQL<br>(Data Query Language)| 데이터 검색 |SELECT|
|DML<br>(Data Manipulation Language)| 데이터 조작 <br> (추가, 수정, 삭제) |INSERT<br>UPDATE<br>DELETE|
|DCL<br>(Data Control Language)| 데이터 및 작업에 대한 사용자 권한 제어 |COMMIT<br>ROLLBACK<br>GRANT<br>REVOKE|

### 참고
- Query
  - '데이터베이스로부터 정보를 요청'하는 것
  - 일반적으로 SQL로 작성하는 코드를 쿼리문(SQL문)이라 함
- SQL 표준
  - SQL은 미국 국립 표준 협회(ANSI)와 국제 표준화 기구(ISO)에 의해 표준이 채택됨
  - 모든 RDBMS에서 SQL 표준을 지원
  - 다만 각 RDBMS마다 독자적인 기능에 따라 표준을 벗어나는 문법이 존재하니 주의

## Singl Table Queries
> SQL Statements 유형 중 DQL에 해당함
### Querying data
- SELECT statement : 테이블에서 데이터를 조회
    ```
    -- 01. Querying data
    SELECT 
    LastName
    FROM
    employees;

    SELECT 
    LastName, FirstName
    FROM
    employees;

    SELECT 
    *
    FROM
    employees;

    SELECT 
    FirstName AS '이름'
    FROM
    employees;

    SELECT
    Name, 
    Milliseconds / 60000 AS '재생 시간(분)'
    FROM
    tracks;
    ```
### Sorting data
- ORDER BY : 조회 결과의 레코드를 정렬
    ```
    -- 02. Sorting data
    SELECT 
    FirstName
    FROM
    employees
    ORDER BY
    FirstName ASC;

    SELECT 
    FirstName
    FROM
    employees
    ORDER BY
    FirstName DESC;

    SELECT
    Country, City
    FROM
    customers
    ORDER BY
    Country DESC,
    City ASC;

    SELECT
    Name, Milliseconds / 60000 AS '재생 시간(분)'
    FROM
    tracks
    ORDER BY
    Milliseconds DESC;
    ```
  - NULL 값이 존재 할 경우, 오름차순 정렬 시 결과에 NULL이 먼저 출력

- SELECT Statements 실행 순서
  - FROM -> SELECT -> ORDER BY

### Filtering data
- DISTINCT statement : 조회 결과에서 중복된 레코드를 제거
  - SELECT 키워드 바로 뒤에 작성해야 함
  - SELCET DISTINCT 키워드 다음에 고유한 값을 선택하려는 하나 이상의 필드를 지정
    ```
    SELECT DISTINCT
    Country
    FROM
    customers
    ORDER BY
    Country;
    ```
- WHERE statement : 조회 시 특정 검색 조건을 지정
  - FROM clause 뒤에 위치
    ```
    SELECT
    LastName, FirstName, City
    FROM
    customers
    WHERE
    City = 'Prague';

    SELECT
    LastName, FirstName, City
    FROM
    customers
    WHERE
    City != 'Prague';

    SELECT
    LastName, FirstName, Company, Country
    FROM
    customers
    WHERE
    Company IS NULL 
    AND Country = 'USA';

    SELECT
    LastName, FirstName, Company, Country
    FROM
    customers
    WHERE
    Company IS NULL 
    OR Country = 'USA';

    SELECT
    Name, Bytes
    FROM
    tracks
    WHERE
    -- 100000 <= Bytes <= 500000;
    Bytes BETWEEN 100000 AND 500000;

    SELECT
    Name, Bytes
    FROM
    tracks
    WHERE
    Bytes BETWEEN 100000 AND 500000
    ORDER BY
    Bytes;

    SELECT
    LastName, FirstName, Country
    FROM 
    customers
    WHERE
    Country IN ('Canada', 'Germany', 'France');
    -- Country = 'Canada'
    -- OR Country = 'Germany'
    -- OR Country = 'France';

    SELECT
    LastName, FirstName, Country
    FROM 
    customers
    WHERE
    Country NOT IN ('Canada', 'Germany', 'France');

    SELECT
    LastName, FirstName
    FROM
    customers
    WHERE
    LastName LIKE '%son';

    SELECT
    LastName, FirstName
    FROM
    customers
    WHERE
    FirstName LIKE '___a';
    ```
- LIMIT clause: 조회하는 레코드 수를 제한
    ```
    SELECT 
      select_list
    FROM
      table_name
    LIMIT [offset,] row_count ;
    ```
  - 하나 또는 두개의 인자를 사용 (0 또는 양의 정수)
  - row_count는 조회하는 최대 레코드 수를 지정
  - offset으로 시작지점을, row_count로 끝 지점을 제한 가능함
    ![limit](https://github.com/yamuzin-oksusu/SSAFY_FW2023/blob/master/images/image-42.png)
    ```
    SELECT
    TrackId, Name, Bytes
    FROM
    tracks
    ORDER BY
    Bytes DESC
    LIMIT 7;

    SELECT
    TrackId, Name, Bytes
    FROM
    tracks
    ORDER BY
    Bytes DESC
    LIMIT 3, 4;
    -- LIMIT 4 OFFSET 3;
    ```
### Grouping data
- GROUP BY clause : 레코드를 그룹화하여 요약본 생성 ('집계 함수'와 함께 사용)
  - Aggregation Functions(집계 함수) : SUM, AVG, MAX, MIN, COUNT 
    ```
    SELECT
    Country, COUNT(*)
    FROM
    customers
    GROUP BY
    Country;

    SELECT
    Composer, AVG(Bytes)
    FROM
    tracks
    GROUP BY
    Composer
    ORDER BY
    AVG(Bytes) DESC;
    ```
  - HAVING clause 
    - 집계 항목에 대한 세부 조건을 지정
    - 주로  GROUP BY와 함께 사용되며 GROUP BY가 없다면 WHERE 처럼 동작
    ```
    SELECT
    Composer,
    AVG(Milliseconds / 60000) AS avgOfMinute
    FROM
    tracks
    GROUP BY
    Composer
    HAVING
    avgOfMinute < 10;

    ```
  
-  SELECT Statement 실행 순서
   -  FROM -> WHERE -> GROUP BY -> HAVING -> SELECT -> ORDER BY > LIMIT
