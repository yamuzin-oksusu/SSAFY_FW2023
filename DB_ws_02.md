# SQL2

2023.10.10 (Tue)
-----

## Managing Tables
> SQL Statements 유형 중 DDL에 해당함
### Create a table
CREATE TABLE statement : 테이블 생성
- CREATE TABLE syntax
    ```
    CREATE TABLE examples (
    ExamId INTEGER PRIMARY KEY AUTOINCREMENT,
    
    LastName VARCHAR(50) NOT NULL,
    FirstName VARCHAR(50) NOT NULL
    );
    ```
    - 각 필드에 적용할 데이터 타입 작성
        - NULL : 아무런 값도 포함하지 않음
        - INTEGER : 정수
        - REAL : 부동 소수점
        - TEXT : 문자열
        - BLOB : 이미지, 동영상, 문서 등의 바이너리 데이터

    - 테이블 및 필드에 대한 제약조건(constraints) 작성 -> 데이터 무결성 유지, 데이터 베이스의 일관성을 보장
      - PRIMARY KEY : 해당 필드를 기본 키로 지정, **INTEGER 타입에만 적용되며 INT, BIGINT등과 같은 정수 유형은 적용되지 않음**
      - NOT NULL : 해당 필드에 NULL 값을 허용하지 않도록 지정
      - FOREIGN KEY : 다른 테이블과의 외래 키 관계를 정의

    - AUTOINCREMENT keyword
      - 자동으로 고유한 정수 값을 생성하고 할당하는 필드 속성
      - 필드의 자동 증가를 나타내는 특수한 키워드
      - 주로 PRIMARY KEY 필드에 적용
      - INTEGER PRIMARY KEY AUTOINCREMENT가 작성된 필드는 항상 새로운 레코드에 대해 이전 최대 값보다 큰 값을 할당
      - 삭제된 값은 무시되며 재사용 불가

- 테이블 스키마(구조) 확인
    ```
    PRAGMA table_info('examples');
    ```
### Modifying table fields 
- ALTER TABLE statement :테이블 및 필드 조작
    | 명령어 | 역할 |
    |---|:---:|
    |ALTER TABLE ADD COLUMN| 필드 추가 |
    |ALTER TABLE RENAME COLUMN| 필드 이름 변경 |
    |ALTER TABLE DROP COLUMN| 필드 삭제 |
    |ALTER TABLE RENAME TO | 테이블 이름 변경 |

    ```
    -- 2.1 ADD COLUMN
    ALTER TABLE 
    examples
    ADD COLUMN
    Country VARCHAR(100) NOT NULL;
    
    -- sqlite는 단일 문을 사용하여 한번에 여러 열을 추가하는 것을 지원하지 않음
    ALTER TABLE examples
    ADD COLUMN Age INTEGER NOT NULL;

    ALTER TABLE examples
    ADD COLUMN Address VARCHAR(100) NOT NULL;

    -- 2.2 RENAME COLUMN
    ALTER TABLE examples
    RENAME COLUMN Address TO PostCode;

    -- 2.3 DROP COLUMN
    ALTER TABLE examples
    DROP COLUMN PostCode;

    -- 2.4 RENAME TO
    ALTER TABLE examples
    RENAME TO new_examples;
    ```

### Delete a table
- DROP TABLE statement :테이블 삭제

    ```
    -- 3. Delete a table
    DROP TABLE new_examples;
    DROP TABLE examples;

    -- sqlite는 컬럼 수정 불가
    -- 대신 테이블의 이름을 바꾸고, 새 테이블을 만들고 데이터를 새 테이블에 복사하는 방식을 사용
    ```
### 참고
- 타입 선호도(Type Affinity) : 컬럼에 데이터 타입이 명시적으로 지정되지 않았거나 지원하지 않을 때 SQLite가 자동으로 데이터 타입을 추론하는 것 
  - 유연한 데이터 타입 지원
    - 데이터 타입을 명시적으로 지정하지 않고도 데이터를 저장하고 조회할 수 있음
    - 컬럼에 저장되는 값의 특성을 기반으로 데이터 타입을 유추
  - 간편한 데이터 처리
    - INTEGER Type Affinity를 가진 열에 문자열 데이터를 저장해도 SQLite는 자동으로 숫자로 변환하여 처리
  - SQL 호환성
    - 다른 데이터베이스 시스템과 호환성을 유지
## Modifying Data
> SQL Statements 유형 중 DML에 해당함
### Insert data
- INSERT statement :테이블 레코드 삽입
  - INSERT INTO 절 다음에 테이블 이름과 괄호 안에 필드 목록 작성
  - VALUES 키워드 다음 괄호 안에 해당 필드에 삽입할 값 목록 작성
    ```
    INSERT INTO 
    articles (title, content, createdAt)
    VALUES 
    ('hello', 'world', '1700-01-01');

    INSERT INTO 
    articles (title, content, createdAt)
    VALUES 
    ('title1', 'content1', '1800-01-01'),
    ('title2', 'content2', '1900-01-01'),
    ('title3', 'content3', '2000-01-01');

    INSERT INTO 
    articles (title, content, createdAt)
    VALUES 
    ('mytitle', 'mycontent', DATE());
    ```
### Update data
- UPDATE statement :테이블 레코드 수정
    - SET 절 다음에 수정할 필드와 새 값을 지정
    - WHERE 절에서 수정할 레코드를 지정하는 조건 작성
    - WHERE 절을 작성하지 않으면 모든 레코드를 수정
    ```
    UPDATE 
    articles
    SET
    title = 'update Title'
    WHERE
    id = 1;

    UPDATE 
    articles
    SET
    title = 'update Title',
    content = 'update Content'
    WHERE
    id = 2;
    ```

### Delete data
- DELETE statement :테이블 레코드 삭제
  - DELETE FROM 절 다음에 테이블 이름 작성
  - WHERE 절에서 삭제할 레코드를 지정하는 조건 작성
  - WHERE 절을 작성하지 않으면 모든 레코드를 삭제
    ```
    DELETE FROM 
    articles
    WHERE 
    id = 1;
    ```


## Multi table queries
### Join
- 관계 : 여러 테이블 간의 (논리적) 연결
- JOIN이 필요한 순간
  - 테이블을 분리하면 데이터 관리는 용이해질 수 있으나 출력시에는 문제가 있음
  - 테이블 한 개 만을 출력할 수 밖에 없어 다른 테이블과 결합하여 출력하는 것이 필요해짐
### Joining tables
- INNER JOIN clause : 두 테이블에서 값이 일치하는 레코드에 대해서만 결과를 반환
- LEFT JOIN clause :오른쪽 테이블의 일치하는 레코드와 함께 왼쪽 테이블의 모든 레코드 반환
  - 왼쪽 테이블 : 모든 레코드 표기
  - 오른쪽 테이블 : 매칭되는 레코드가 없으면 NULL을 표시
    ```
    -- INNER JOIN
    SELECT * FROM articles
    INNER JOIN users 
    ON users.id = articles.userId;

    SELECT articles.title, users.name 
    FROM articles
    INNER JOIN users 
    ON users.id = articles.userId
    WHERE users.id = 1;


    -- LEFT JOIN
    SELECT * FROM articles
    LEFT JOIN users 
    ON users.id = articles.userId;

    SELECT * FROM users
    LEFT JOIN articles 
    ON articles.userId = users.id
    WHERE articles.userId IS NULL;
    ```