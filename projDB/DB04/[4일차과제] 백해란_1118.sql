-- 키가 180~185 사이인 회원만 검색

SELECT * FROM userTBL WHERE height >= 180 AND height <= 185;
SELECT * FROM userTBL WHERE height BETWEEN 180 AND 185;   -- Between 사용

-- 키가 166, 172, 182 회원만 검색

SELECT * FROM userTBL WHERE height = 166 OR height = 172 OR height = 182;
SELECT * FROM userTBL WHERE height IN(166,172,182);   -- IN사용

-- 전남, 경남, 서울 지역의 회원만 검색

SELECT * FROM userTBL WHERE addr = '전남' OR addr = '경남' OR addr = '서울';
SELECT * FROM userTBL WHERE addr IN('전남','경남','서울');

-- like 연산자 : 문자열 검색 / 회원 중 김씨성을 가진 회원만 검색

SELECT * FROM userTBL WHERE name LIKE '김%' ; -- LIKE 사용, % :상관없이.

-- 성을 제외한 이름에 '용'이 들어가는 회원을 검색

SELECT * FROM userTBL WHERE name LIke '_용%';      -- _ : 와일드 카드

-- 성을 제외한 이름이 '원'으로 끝나는 회원을 검색

SELECT * FROM userTBL WHERE name LIke '__원';
SELECT * FROM userTBL WHERE name LIke '%원';       -- 글자수상관없이 원으로 끝나는 사람 검색 가능


-- 같은 이름을 가진 회원 검색

SELECT * FROM userTBL WHERE name LIke '_종신';


-- 김경호 회원보다 키가 큰 회원 

SELECT userID, name, height FROM userTBL WHERE name = '김경호';   -- 김경호 키 검색1
SELECT * FROM userTBL WHERE height > 177;                         -- 김경호 키보다 큰 회원 검색 2


-- 서브쿼리를 하나의 쿼리로 생성

SELECT * FROM userTBL WHERE height >(SELECT height FROM userTBL WHERE name = '김경호');  -- 비교하는 네임이 같아야 함.

-- 은지원보다 키가 큰 사람

SELECT * FROM userTBL WHERE height >(SELECT height FROM userTBL WHERE name = '은지원');   

-- 전남에 사는 회원보다 키가 큰 회원을 검색

SELECT userID, name, addr ,height FROM userTBL WHERE addr = '전남';   -- 전남에 사는 사람 검색 - 177
SELECT * FROM userTBL WHERE height > 177;                             -- 177 이상 검색   


-- 서브쿼리로 하나의 쿼리  만들기

SELECT * FROM userTBL WHERE height > (SELECT height FROM userTBL WHERE addr = '전남'); 


-- 서울에 사는 회원보다 키가 큰 회원을 검색

SELECT userID, name, addr ,height FROM userTBL WHERE addr = '서울';   -- 서울에 사는 사람 검색 
SELECT * FROM userTBL WHERE height > ; -- ? ;                             -- 177 이상 검색  (오류) 


-- 서브쿼리로 하나의 쿼리  만들기 
-- ANY를 사용하면 서브쿼리의 제일 작은 값보다 큰  176

SELECT * FROM userTBL WHERE height > ANY (SELECT height FROM userTBL WHERE addr = '서울'); 

-- 서울 사람드르이 키 조건이 모두 만족했으면 좋겠다  
-- ALL : 서브쿼리에서 가장 큰 조건을 만족해야 함 186

SELECT * FROM userTBL WHERE height > ALL (SELECT height FROM userTBL WHERE addr = '서울');  

-- 서울 사람들의 키와 같은 회원 검색
                        
SELECT * FROM userTBL WHERE height = ANY (SELECT height FROM userTBL WHERE addr = '서울'); 
                        
SELECT * FROM userTBL WHERE height  IN(SELECT height FROM userTBL WHERE addr = '서울');  
-- ANY=IN 하지만IN이 더 명확.


SELECT * FROM userTBL WHERE height = ALL (SELECT height FROM userTBL WHERE addr = '서울');   
-- ALl은 '=' 사용 x 조건 만족 어려움.

-- 경남 사람보다 어린 사람들을 검색하기

SELECT userID, name, birthYear, addr FROM USERTBL WHERE addr = '경남';
SELECT * FROM userTBL WHERE birthYear > ; -- ???

-- 경남 사람보다 어린 사람 (조건이 하나 이상 포함된)

SELECT * FROM userTBL WHERE birthYear > ANY (SELECT birthYear FROM USERTBL WHERE addr = '경남');

-- 경남 사람 중에 가장 어린 사람 기준으로 비교

SELECT * FROM userTBL WHERE birthYear > ALL (SELECT birthYear FROM USERTBL WHERE addr = '경남');

-- 경남 사람들의 조건이 포함되게

SELECT * FROM userTBL WHERE birthYear = ANY (SELECT birthYear FROM USERTBL WHERE addr = '경남');
SELECT * FROM userTBL WHERE birthYear IN (SELECT birthYear FROM USERTBL WHERE addr = '경남');

-- ORDER BY (컬럼명 ASC, DESC)로  정렬 하기 

SELECT * FROM buyTBL ORDER BY num ASC;   -- 오름차순  ASC 생략가능
SELECT * FROM buyTBL ORDER BY num DESC;  -- 내림차순


-- 회원이름으로 정렬 

SELECT * FROM userTBL ORDER BY name ASC;  -- 오름차순
SELECT * FROM userTBL ORDER BY name DESC; -- 내림차순

-- 지역으로 정렬

SELECT * FROM userTBL ORDER BY addr ASC;
SELECT * FROM userTBL ORDER BY addr DESC;

-- 지역별 정렬 후 지역 내에서 이름으로 정렬 (그리고 나서 출생년도로)

SELECT * FROM userTBL ORDER BY addr, name, birthYear ASC;    -- 정렬을 지정하고 싶은 컬럼순서대로 __,__,__

-- 지역을  오름차순으로 하고 이름은 내림 차순으로 보고 싶다.

SELECT * FROM userTBL 
WHERE addr IN ('서울','경남')    -- order by는 WHERE 절 다음에 
ORDER BY addr DESC, name ASC ;  -- 앞에 것을 기준으로 하고 싶으면 따로 디센딩 설정

-- 회원들의 지역을 검색(중복제거)

SELECT DISTINCT addr FROM userTBL ;  -- DISTINCT 사용, 반드시 셀렉트 뒤에 와야 함

SELECT DISTINCT addr, name FROM userTBL ;  -- name은 중복이 없으므로 모두 출력

SELECT DISTINCT birthYear FROM userTBL ;  

-- employees 데이터베이스에서 employees의 성별을 중복 제거 하고 싶다

SELECT DISTINCT gender FROM employees.employees;  -- 카테고리, 타이틀만 출력하기에 좋음

-- employees 데이터베이스에서 title 테이블의 직급 구성을 보기

SELECT DISTINCT title FROM employees. titles;

--  employees 데이터베이스에서 입사일이 가장 오래된 직원 5명 검색

SELECT emp_no, first_name, hire_date FROM employees.employees
ORDER BY hire_date ASC
-- 전체 오름차순 정렬로 다섯명 고를 순 있지만 전부 다 출력됨
LIMIT 5; -- lIMIT을 사용하여 1위~5위만 출력 가능



-- buytbl과 같은 구조, 데이트 가진 테이블 생성 (백업) 

CREATE TABLE buyTBL3 (SELECT * FROM buyTBL);    -- 단, 제약조건(PK와 FK)까지는 복사하지 않음.

-- buyTBL의 userID, prodName, price로만 된 테이블을 생성할 건데 amount 수가 2개 이상인 상품

CREATE TABLE buyTBL2 
(
SELECT userID, prodName, price  FROM buyTBL  
WHERE amount>=2
);

SELECT * FROM buyTBL2;  -- 확인


-- buytbl의 구조만 복사해서 buytbl4  생성하기

CREATE TABLE buyTBL4 (SELECT * FROM buyTBL WHERE 1 = 0);  -- 왜 오류가 아니고...?


-- GROUG BY  -> 그룹을 지을 수 있는 컬럼을 이해하는 것
-- 회원 중에 구매한 물건의 수를 집계

SELECT userID AS '사용자 아이디', SUM(amount) AS '총 구매 개수' FROM buyTBL
GROUP BY userID;


-- 회원의 총 구매액을 집계

SELECT userID AS '사용자 아이디', SUM(amount*price) AS '총 구매액 ' FROM buyTBL
GROUP BY userID
ORDER BY 2 DESC;    -- 사용자 아이디 = 1, 총구매액 = 2


-- 전체 회원의 구매액->매출집계

SELECT SUM(amount*price) AS '총 구매액' FROM buyTBL;
SELECT SUM(amount) AS '총 구매개수' FROM buyTBL;

-- 전체회원의 평균 구매액
SELECT AVG(amount*price) AS '평균 구매액' FROM buyTBL;
SELECT AVG(amount) AS '평균  구매개수' FROM buyTBL;


-- 회원별 평균 구매액

SELECT userID, AVG(amount*price) AS '평균 구매액' FROM buyTBL
GROUP BY userID;

SELECT userID, AVG(amount) AS '평균  구매개수' FROM buyTBL
GROUP BY userID;

-- 가장 키큰 사람이랑 가장 키 작은 사람이랑 평균키

SELECT name, 
MAX(height) AS '가장 키가 큰 사람', 
MIN(height) AS '가장 키가 작은 사람',
AVG(height) AS '평균신장' 
FROM userTBL
GROUP BY name;
-- 이렇게 쓰면 오류

-- 키가 가장 큰 사람은 누구?
-- 1) 가장 큰 키를 찾는다
SELECT MAX(height) AS '가장 키가 큰 사람' FROM userTBL;

-- 1-2) 서브쿼리 조건으로 연결

SELECT * FROM userTBL
WHERE height= (SELECT MAX(height)FROM userTBL);

-- 2) 키가 가장 작은 사람
SELECT * FROM userTBL
WHERE height= (SELECT MIN(height) FROM userTBL);

-- 3) 키가 평균이상인 사람
SELECT * FROM userTBL
WHERE height>= (SELECT AVG(height) FROM userTBL);

-- 4) 키가 가장 큰 사람과 작은 사람
SELECT * FROM userTBL
WHERE height= (SELECT MAX(height)FROM userTBL)
OR height= (SELECT MIN(height) FROM userTBL);

-- 제일 많이 사용하는 집계 함수 COUNT()
SELECT COUNT(*) FROM userTBL;
SELECT COUNT(*) FROM buyTBL;

SELECT userID, COUNT(userID) FROM buyTBL    
GROUP BY userID;                               -- 아이디 기준 그룹핑

-- COUNT()할때, NULL은 제외하고 수를 셈
SELECT COUNT(*)-COUNT(mobile1) FROM userTBL;
-- = 
SELECT COUNt(*) FROM userTBL
WHERE mobile1 IS NULL;


SELECT COUNT(mobile1) FROM userTBL;
-- = 
SELECT COUNt(*) FROM userTBL
WHERE mobile1 IS  NOT NULL;


-- 검색 조건에 집계함수를 하고 싶다
-- 총 구매액이 1000 이상인 사용자에게 사은품을 증정하고 싶다
-- 총 구매액이 1000 이상은 사람을 검색
SELECT * FROM buyTBL
WHERE SUM(amount*price) >1000;
-- 이렇게하면 오류

-- WHERE절에 집계함수를 쓰려면 서브쿼리로만. 자체로는 불가능
-- GROUP BY HAVING으로 사용 가능

SELECT userID, SUM(amount*price)
FROM buyTBL
GROUP BY userID
HAVING SUM(amount*price) > 1000;

-- 1)사용자 그룹 정의
SELECT userID, AVG(amount*price), COUNT(*), SUM(amount*price), MAX(amount*price), MIN(amount*price)
FROM buyTBL
WHERE userID != 'BBK' -- 그룹핑 전에 조건 설정해야함
GROUP BY userID   -- 조건검색 (비교연산자) 가능하지만, 집계함수는 사용 불가
HAVING AVG(amount*price)>400;  -- 집계함수는 그룹핑 후에 사용 가능하니까 해빙 뒤에

-- 회원 중에 구매액이 평균 이상인 사람

SELECT userID, AVG(amount*price), COUNT(*), SUM(amount*price), MAX(amount*price), MIN(amount*price)
FROM buyTBL
GROUP BY userID   -- 조건검색 (비교연산자) 가능하지만, 집계함수는 사용 불가
HAVING AVG(amount*price)> (SELECT AVG(amount*Price) FROM9 buyTBL); 

-- 회원 중에 구매수가  평균 이하인 사람만 검색

SELECT userID, AVG(amount), COUNT(*), SUM(amount)
FROM buyTBL
GROUP BY userID  
HAVING SUM(amount) =< (SELECT AVG(amount) FROM buyTBL); 


SELECT userID, SUM(amount), AVG(amount), COUNT(*) 
FROM buyTBL
-- where
GROUP BY userID  
HAVING SUM(amount) >= (SELECT AVG(amount) FROM buyTBL)   -- 이상 구매한 사람
ORDER BY 1 DESC;

-- ROLLUP  총합 또는 중간합계

SELECT * FROM buytbl;

--groupName별로 합계 및 총합을 집계

SELECT groupName, SUM(amount)   -- prodName 을 여기 넣으면  /  여기에 적힐 수 있음 /집계함수는 숫자만 돼
FROM buytbl
GROUP BY groupName             -- prodName 도 그룹핑이 필요함 /반대로 그룹핑을 해야/ 
WITH ROLLUP;


SELECT num, userID, SUM(amount) 
FROM buytbl  
GROUP BY userID, num  
WITH ROLLUP;


-- 과제))

-- 1)사용자 기준으로 구매액을 중간합계를 포함해서 총합계를 집계

SELECT num, userID AS '사용자', SUM(amount*price) AS '총 구매액'
FROM buyTBL
GROUP BY userID , num
WITH ROLLUP;

-- 2) 분류 기준으로 구매액을 중간합계를 포함해서 총합계를 집계groupName

SELECT num, groupName AS '분류', SUM(amount*price) AS '총 구매액'
FROM buyTBL
GROUP BY groupName, num
WITH ROLLUP;

-- 3) 상품명 기준으로 , 구매액을 중간합계를 포함해서 총합계를 집계

SELECT num, prodName AS '상품명', SUM(amount*price) AS '총 구매액'
FROM buyTBL
GROUP BY prodName, num
WITH ROLLUP;


-- 4) 분류 기준으로 구매액을 중간합계를 포함해서 총합계를 NULL을 제외하고 집계  

SELECT num, groupName AS '분류', SUM(amount*price) AS '총 구매액'
FROM buyTBL
WHERE groupName IS NOT NULL
GROUP BY groupName, num
WITH ROLLUP;         