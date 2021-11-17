-- USE employees.title(데이터배이스)했을 경우 데이터베이스명 생략 가능 

SELECT * FROM employees.titles;
SELECT * FROM titles;          
 

-- 특정 컬럼만 내용 순서에 맞게 가져와서 SELECT하기

-- SELECT emp_no, title FROM titles;   -- 순서 바뀌기 가능

SELECT to_Date, title, emp_no FROM titles;

-- 정보 확인할 때 사용

SHOW DATABASES;

USE employees;

SHOW TABLES;

SELECT * FROM departments;

SHOW TABLE STATUS;


-- TABLE의 열 이름 확인->데이터 구조를 알고 싶을 때

DESC departments;

DESC employees;


-- 별칭을 줘서 여 리읆과 다르게 결과 내보내기

SELECT first_name AS 이름, gender AS 성별, hire_Date AS '회사 입사일' FROM employees;     

-- ','와 AS는 같음. 중간에 공백(띄어쓰기)있다면 ',' 사용



-- Todo : 실습용 데이터베이스 생성해서 관리

-- 1) sqldb 데이터베이스 생성

DROP DATABASE IF EXISTS sqldb;  -- 기존에 있으면 삭제

CREATE DATABASE sqldb;  


-- use sqldb

USE sqldb;


-- 회원테이블생성

CREATE TABLE usertbl
(userID char(8) NOT NULL PRIMARY KEY,
 name varchar(10) NOT NULL,
 birthYear INT NOT NULL,
 addr char(2) NOT NULL,
 mobile1 char(3),
 mobile2 char(8),
 height SMALLINT,
 mDate DATE
 );
 

-- 4) 회원 구매 테이블 생성 :buytbl

CREATE TABLE buyTBL
(num INT AUTO_INCREMENT NOT NULL PRIMARY KEY,
 userID char(8) NOT NULL,
 prodName char(6) NOT NULL,
 groupName char(4),
 price INT NOT NULL,
 amount SMALLINT NOT NULL,
 FOREIGN KEY(userID) REFERENCES userTBL(userID)
 );
 
 -- 5) 회원테이블에 데이터 insert
 
INSERT INTO userTBL VALUES('LSG', '이승기', 1987, '서울','011','11111111', 182, '2008-8-8');
INSERT INTO userTBL VALUES('KBS', '김범수', 1979, '경남','011','22222222', 173, '2012-4-4');
INSERT INTO userTBL VALUES('KKH', '김경호', 1971, '전남','019','33333333', 177, '2007-7-7');
INSERT INTO userTBL VALUES('JYP', '조용필', 1950, '경기','011','44444444', 166, '2009-4-4');
INSERT INTO userTBL VALUES('SSK', '성시경', 1979, '서울', NULL, NULL,      186, '2013-12-12');
INSERT INTO userTBL VALUES('LJB', '임재범', 1963, '서울','016','66666666', 182, '2009-9-9');
INSERT INTO userTBL VALUES('YJS', '윤종신', 1969, '경남', NULL, NULL,      170, '2005-5-5');
INSERT INTO userTBL VALUES('EJW', '은지원', 1972, '경북','011','88888888', 174, '2014-3-3');
INSERT INTO userTBL VALUES('JKW', '조관우', 1965, '경기','018','99999999', 172, '2010-10-10');
INSERT INTO userTBL VALUES('BBK', '바비킴', 1973, '서울','010','00000000', 176, '2013-5-5');

-- 6) 구매테이블에 데이터 insert

INSERT INTO buyTBL VALUES(NULL, 'KBS', '운동화',   NULL,   30, 2);
INSERT INTO buyTBL VALUES(NULL, 'KBS', '노트북', '전자', 1000, 1);
INSERT INTO buyTBL VALUES(NULL, 'JYP', '모니터', '전자',  200, 1); 
INSERT INTO buyTBL VALUES(NULL, 'BBK', '모니터', '전자',  200, 5);
INSERT INTO buyTBL VALUES(NULL, 'KBS', '청바지', '의류',   50, 3);
INSERT INTO buyTBL VALUES(NULL, 'BBK', '메모리', '전자',  80, 10);
INSERT INTO buyTBL VALUES(NULL, 'SSK', '책'    , '서적',   15, 5);    
INSERT INTO buyTBL VALUES(NULL, 'EJW', '책'    , '서적',   15, 2);  
INSERT INTO buyTBL VALUES(NULL, 'EJW', '청바지', '의류',   50, 1);
INSERT INTO buyTBL VALUES(NULL, 'BBK', '운동화',   NULL,   30, 2);
INSERT INTO buyTBL VALUES(NULL, 'EJW', '책'    , '서적',   15, 1);
INSERT INTO buyTBL VALUES(NULL, 'BBK', '운동화',   NULL,   30, 2);

-- 데이터확인

SELECT * FROM buytbl;
SELECT * FROM usertbl;


-- 8) 특정 조건이 보고 싶을 때 검색  WHERE

SELECT * FROM userTBL WHERE name = '김경호';

-- 9) 조건을 2개 이상 같이 사용하고 싶을 때

-- 1970년 이후 출생하고 신장이 182 이상인 사람의 아이디와 이름

SELECT userID, Name FROM userTBL WHERE birthYear >= 1970 AND height >= 182;

-- 9-2)1970년 이후에 출생했거나  신장이 182 이상인 사람의 아이디

SELECT * FROM userTBL WHERE birthYear >= 1970 OR height >= 182;

-- 9-3)신장이 175이상이면서 지역이 서울인 사람

SELECT * FROM userTBL WHERE height >= 175 AND addr= '서울';


-- 9-4) 핸드폰 앞자리가 010으로 시작하는 사람

SELECT * FROM userTBL WHERE mobile1 = '010';


-- 9-5)서울에 살지 않는 사람 모두 찾아주세요

SELECT * FROM userTBL WHERE addr != '서울';


-- 9-6)010이 아닌 사람

SELECT * FROM userTBL WHERE mobile1 != '010';

-- 9-7)핸드폰 앞자리가 011이  아니면서 키가 175 이하인사람

SELECT * FROM userTBL WHERE mobile1 != '011' AND height <= 175;

-- 9-8) 구매 테이블에서 컴퓨터를 1개이상 구매한 고객 찾기

SELECT * FROM buyTBL WHERE prodName = '노트북' AND amount >= 1;

-- 9-9) 구매 테이블에서 책을 두 개 이상 구매한 고객 찾기
SELECT * FROM buyTBL WHERE prodName = '책' AND amount >= 2;

-- 9-10) 구매테이블에서 가격이 50 이상이면서, 구매 개수가 2개 이상인 물건

SELECT prodName, price, amount FROM buyTBL WHERE price >= 50 AND amount >= 2;

-- 9-11) 구매 테이블에서 모니터를 구매한 고객을 제외한 구매 리스트

SELECT * FROM buyTBL WHERE prodName != '모니터';

-- 9-12) 구매 테이블에서 구매품목이 정해지지 않은(NULL) 구매 리스트

SELECT * FROM buyTBL WHERE groupName IS NUll;  -- 널은 정해진 값이 없어서 비교연산자가 불가능하다

-- 9-13) NULL을 제외
SELECT * FROM buyTBL WHERE groupName IS NOT NUll;

-- 180~183의 키를 가진 사람

SELECT Name, height FROM userTBL WHERE height >= 180 AND height <=183;



