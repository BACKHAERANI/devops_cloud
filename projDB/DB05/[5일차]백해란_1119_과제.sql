-- TestTBL 생성하기

CREATE TABLE TestTBL1(id int, userName char(3), age int);

DESC TestTBL1;

-- insert (1, 홍길동, 25세)
 
INSERT INTO TestTBL1 VALUES(1, 홍길동,25);
 
-- insert 2, 설현
-- 1) 없는 데이터를 NULL을 붙여준다
INSERT INTO TestTBL1 VALUES(2, 설현, NULL);
-- 2) 암묵적으로 NULL만들기
INSERT INTO TestTBL1 (id,userName) VALUES(2, 설현);
 
SELECT * FROM TestTBL1;
 
-- insert 초아,26세,3
INSERT INTO TestTBL1 (userName,age,id) VALUES('초아',26,3);  -- 순서가 다른 데이터를 순서대로 넣는 식
  
  
-- auto_INCREMENT를 적용한 테이블 생성
  
CREATE TABLE TestTBL2
(id int AUTO_INCREMENT PRIMARY KEY,
userName char(3),
age int
);
  
  
-- insert 지민 25세, 유나 22세 유경 21세

INSERT INTO TestTBL2 VALUES (NULL,'지민',25);
INSERT INTO TestTBL2 VALUES (NULL,'유나',22); 
INSERT INTO TestTBL2 VALUES (NULL,'유경',21); 

SELECT * FROM testTBL2;

-- id를 자동으로 100번부터 다시 발급
ALTER TABLE TestTBL2 AUTO_INCREMENT = 100;
INSERT INTO TestTBL2 VALUES (NULL, '찬미', 23);

-- auto increment의 초기값은 1000으로 하고 3 증가해서 id 발급
CREATE TABLE TestTBL3
(id int AUTO_INCREMENT PRIMARY KEY,
userName char(3),
age int);

ALTER TABLE testtbl3 AUTO_INCREMENT = 1000;
-- 증가값을 지정하는 서버변수(기본 1로 설정되어 있음)
SET @@auto_increment_increment = 3;
INSERT INTO TestTBL3 VALUES (NULL,'나연',20);
INSERT INTO TestTBL3 VALUES (NULL,'정연',18); 
INSERT INTO TestTBL3 VALUES (NULL,'모모',19); 

-- 데이터 확인
SELECT * FROM testTBL3;


SELECT LAST_INSERT_ID();  -- 마지막 id번호가 뭐냐?


--  테이블을 생성하고 그후에 insert into select 통해 대량의 데이터 삽입

CREATE TABLE TestTBL4
(id int AUTO_INCREMENT PRIMARY KEY,
FName varchar(50),
LName varchar(50));

ALTER TABLE testtbl4 AUTO_INCREMENT = 1000;

-- insert into select통해 다량의 데이터를 삽입

INSERT INTO testtbl4
   SELECT NULL, first_name, last_name FROM employees.employees;

-- 데이터 확인 
SELECT * FROM testtbl4;


-- 정보수정 UPDATE - kyoichi 전화번호를 없음으로 변경

-- 1)kyoichi정보검색

SELECT * FROM testtbl4 WHERE Fname = 'kyoichi';

-- 2) 정보수정

UPDATE testTBL4 
SET Lname = '없음'
WHERE Fname = 'kyoichi';   -- 특정정보 지정

-- buytbl 상품가격을 인상 1.5배(전체)
-- 1) 변경된 데이터 확인-> 12개 건이 업데이트 확인 필수
SELECT price, price * 1.5 FROM buytbl;

-- 정보 수정
UPDATE buytbl
SET price = price * 1.5 ;

SELECT * FROM buytbl;


-- 데이터 삭제 delete

-- 1) testtbl4 테이블에서 Fname이 Aamer 인 사람 삭제

-- 1-2)Aamer 찾기 -> 228건 삭제

SELECT * FROM testTBL4 WHERE Fname  = 'Aamer';

-- 1-3) 데이터 삭제
DELETE FROM testTBL4 WHERE Fname  = 'Aamer';


-- 대용량 테이블 삭제

-- 1) 테이블 생성
USE sqldb;
CREATE table bigtbl1 (select*from employees.employees);
CREATE table bigtbl2 (select*from employees.employees);
CREATE table bigtbl3 (select*from employees.employees);

-- 2)테이블 삭제

DELETE FROM bigtbl1;
DROP table bigtbl2;
TRUNCATE table bigtbl3;


-- 회원별로 총 구매액을 집계하고 가장 높은 구매액 순으로 정렬

SELECT userID, SUM(price*amount)
FROM buytbl
GROUP BY userID
ORDER BY 2 DESC;

-- CTE형태로 변경

WITH CTE_BUYTBL(userID, total)
AS 
(
SELECT userID, SUM(price*amount)
FROM buytbl
GROUP BY userID
ORDER BY 2 DESC
)
SELECT*FROM CTE_BUYTBL
ORDER BY TOTAL DESC ;


-- buytbl 총합
WITH CTE_BUYTBL(userID, total)
AS 
(
SELECT userID, SUM(price*amount)
FROM buytbl
GROUP BY userID
)
SELECT AVG(total) FROM CTE_BUYTBL
ORDER BY TOTAL DESC ;

-- 회원테이블에서 각 지역별로 가장 큰 키를 한명씩 뽑은 후
-- 그 사람들의 평균키를 집계하라

-- 1)지역별로 가장 키 큰 사람 집계
SELECT addr, MAX(height), MIN(height)
FROM usertbl
GROUP BY addr;

-- 2) CTE로 만들어서 결과를 받은 후에 키 큰사람 기준 평균, 키 작은 사람 평균을 낸다
WITH cte_usertbl(addr, MAXheight, MINheight)
AS
(SELECT addr, MAX(height), MIN(height)
FROM usertbl
GROUP BY addr)
SELECT AVG(MAXheight) AS '키 큰 사람 기준 평균', AVG(MINheight) AS '키 작은 사람 기준 평균'
FROM cte_usertbl;


-- 변수를 선언해서 쿼리를 실행

-- 5개 이하 검색
SET @myval5 = 5 ;
SELECT * FROM buytbl WHERE amount <= @myval5;

-- 2개 이하 검색

SET @myval2 = 2 ;
SELECT * FROM buytbl WHERE amount =< @myval2;

-- 분류에서 서적만 검색
SET @myval = '서적';
SELECT * FROM buytbl 
WHERE groupName = @myval;

-- 평균 구매 개수를 정수로 표현

SELECT AVG(amount) FROM buytbl;

-- 정수형 CAST, CONVERT형 변환 방법
SELECT CAST(AVG(amount) AS SIGNED INTEGER) FROM buytbl;
SELECT CONVERT(AVG(amount), SIGNED INTEGER) FROM buytbl;

-- 문자형->날짜형으로 변환

SELECT CAST('2022$12$12' AS DATE);
SELECT CAST('2022$12$12' AS DATE);
SELECT CAST('2022$13$12' AS DATE);   -- 변환할 수 없는 데이터는 Null 리턴

-- 암묵적 형변화
SELECT '100'+'200'; 
-- ->
SELECT CONCAT('100','200');

-- IF (수식(연산,비교), TREU 출력, FALSE 출력)
SELECT IF(100>200, '참', '거짓');
SELECT IF(100>200, 100/200, 100*200);
 
-- IFNULL(컬럼, 널이면 수식1, 널이 아니면 2)
-- 널이면 시행
SELECT IFNULL (NULL,'널이네요');
SELECT userID, prodName, IFNULL (groupName, '아직미정') AS '분류' FROM buytbl;

-- NULLIF(수식 1,2)비교 한다음에 같으면 널하고 다르면 수식1을 반환

SELECT IFNULL (NULLIF(100,100), '너리'), NULLIF(200,100);


-- 다중분리  CASE WHEN ELSE END 

SELECT CASE amount
		 WHEN 1 THEN '노력하세요'
		 WHEN 5 THEN '오오...'
		 WHEN 10 THEN '감사합니다'
		 ELSE '모름'
	END	 
FROM buytbl;

-- 문자열 내장함수

-- 1) LENGTH(문자열) 문자열의 길이를 반환
SELECT LENGTH('가나다'), LENGTH('ABC'), CHAR_LENGTH('abc');   -- 한글은 3바이트/ 영어는 1바이트

-- 2) concat() 문자열 연결시켜주는 함수
SELECT CONCAT('가나다','마바사');
SELECT CONCAT(userID,'님, 반갑습니다.')
FROM usertbl;

	
SELECT CONCAT_WS(',',userID,name)
FROM usertbl;	

-- format	
SELECT FORMAT (price*amount,3) FROM buytbl;

-- 3) insert(문자열,위치, 길이, 바꿀문자(수))문자열에 문자를 삽입해주는 함수-> 데이터 마킹
-- 은지원 -> 은*원
SELECT userID, name, INSERT(name, 2, 1, '*')
FROM usertbl;

-- 회원의 핸드폰 번호(한번에 출력)  가운데 ****처리

Select * from usertbl;

SELECT userID, INSERT(CONCAT(mobile1, mobile2), 4, 4, '****') AS '연락처'
FROM usertbl;

SELECT userID, name, CONCAT(mobile1, INSERT(mobile2,1,4,'****'))  AS '연락처'
FROM usertbl;

-- 4) insert(문자열,찾을 문자) 특정 문자의 위치를 찾는 함수
SELECT INSTR('042)9000-0000',')');

-- 5) upper() 대문자로 변경lower() 소문자로 변경
-- 아이디 중복 확인 할 때 사용
-- userN 가입하려고 하는데  usern 이 있을 때 가입 불가 usern -> upper('usern') = upper('userN')
SELECT upper('usern') , upper('userN');
SELECT lower('usern') , lower('userN'); 

-- 6)TRIM(컬럼명) 앞뒤 공백제거
SELECT TRIM('           안 녕.. ..    ');

-- 7) REPLACE(문자열, 검색할 단어, 변경할 단어)
SELECT REPLACE('이것이 MariaDB이다','이것이','THIS IS');

-- 경기지역만 경기도로 변경해서 출력
SELECT REPLACE (addr, '경기', '경기도')
FROM usertbl;

-- 8) SUBSTRING(문자열, 시작위치, 길이) 문자열을 잘라주는 함수
-- 대한민국만세에서 민국만 추출하기
SELECT SUBSTRING('대한민국만세', 3,2);

SELECT SUBSTRING('042)000-0000',1,INSTR('042)000-0000',')')-1);


-- 수학함수

-- 올림: ceiling(숫자), 내림: floor(숫자), 반올림: round(숫자) -> 정수 
-- ROUND는 반올림의  소수점 기준을 줄 수 있다
SELECT CEILING(4.7), FLOOR(4.7), ROUND(4.7);
SELECT ROUND(4.75,2), ROUND(4.7), ROUND(4.75,1);

-- 지정된 소수점 이하 버림
SELECT TRUNCATE(4.759,2);

--  MOD(숫자1, 숫자2) 숫자1과 숫자2를 나눈 나머지값을 리턴
-- 나머지가 0과 1을 비교해서 홀, 짝
SELECT MOD(10,3);

-- 날짜함수
-- 1) ADDDATE(날짜, 차이), SUBDATE(날짜, 차이)
-- 날짜기준으로 차이를 빼거나 더하기
SELECT ADDDATE('2021-11-19',INTERVAL 1 MONTH),
		 SUBDATE('2021-11-19',INTERVAL 1 MONTH);

-- 현재 날짜와 시간을 제공해주는 함수
-- CURDATE(): 현재날짜, CURTIME(): 현재 시간, NOW(): 현재날짜 + 시간, SYSDATE(): 현재 날짜 + 시간
SELECT CURDATE(), CURTIME(), NOW(), SYSDATE();
SELECT DATE(SYSDATE()), TIME(SYSDATE());

-- 지금으로부터 12-31일까지 얼마나 남았는지 궁금해요
SELECT DATEDIFF(NOW(),'2021-12-31');
-- 교육종료일
SELECT DATEDIFF(NOW(),'2022-4-30');

-- LAST_DAY() 마지막 날을 반환해주는 함수
SELECT LAST_DAY('2027-02-01')

-- 회원테이블에서 회원 중에 키가 큰 순으로 순위를 정하고 싶다
-- 1) 키큰 순으로 정렬
SELECT height, name, addr FROM usertbl
ORDER BY height DESC;

-- 2)ROW_NUMBER()으로 순위 부여
SELECT ROW_NUMBER() OVER(ORDER BY height DESC, name ASC) "키 큰 순위", 
		 name, addr, height 
FROM usertbl;


-- 3)순위를 동률일 때  같은 순위를 부여하는 방식! (이거 파이썬 할때 하고 싶었는데 못한 거..!!!)

SELECT DENSE_RANK() OVER(ORDER BY height DESC) "키 큰 순위", 
		 name, addr, height 
FROM usertbl;

-- 4) 순위를 동률일 때 같은 순위를 주고 (올림픽 기준) 순위를 부여하는 방식
SELECT RANK() OVER(ORDER BY height DESC) "키 큰 순위", 
		 name, addr, height 
FROM usertbl;

-- 5) 전체순위 말고 지역별로 순위를 주고 싶을 경우 -- partition by 기준
SELECT DENSE_RANK() OVER(PARTITION BY addr ORDER BY height DESC, name ASC) "키 큰 순위", 
		 name, addr, height 
FROM usertbl;


-- 6) 가장 키 큰 사람의 키와 비교해서 차이를 확인하기 

SELECT addr, name, height,
		 height- (FIRST_VALUE(height) OVER(ORDER BY height DESC))"키 차이"
FROM usertbl;		 

-- 7) 지역별로 가장 키  큰 사람
SELECT addr, name, height,
		 height- (FIRST_VALUE(height) OVER(PARTITION BY addr ORDER BY height DESC))"키 차이"
FROM usertbl;	

--  공통의 데이터 포맷으로 json 형태로 쿼리 결과를 변경
SELECT JSON_OBJECT('addr', addr, 'name', name, 'height', height,
'distance', (height- (FIRST_VALUE(height) OVER(ORDER BY height DESC)))) "JSON VALUE" 
FROM usertbl;

