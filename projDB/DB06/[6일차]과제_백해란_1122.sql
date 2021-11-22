-- 판매자, 판매 계절, 판매 수량의 데이터를 관리하는 pivottest

-- 판매자 별 계절  판매 수량 맞춤 판매수량 집계

USE sqldb;
CREATE TABLE pivotTest
(uName CHAR(3),
season CHAR(2),
amount INT);

-- 테이블확인
DESC pivotTest;

-- 데이터 9건입력

INSERT INTO pivotTest VALUES
('김범수','겨울',10),('윤종신','여름',15),('김범수','가을',25),
('김범수','봄',  3),('김범수','봄',37),('윤종신','겨울',40),
('김범수','여름',14),('김범수','겨울',22),('윤종신','여름',64);

-- 데이터 확인
SELECT * FROM pivotTest;


-- 판매자 별 계절 판매 수량(컬럼으로) 맞춤판매 수량 집계
-- 1) 판매자 별로 그룹으로 해서 총 합계
SELECT uName, SUM(amount)
FROM pivotTest
GROUP BY uName;

-- 계절별 집계를 추가하기
SELECT uName,
SUM(If(season='봄',amount,0)) AS '봄',
SUM(If(season='여름',amount,0)) AS '여름',
SUM(If(season='가을',amount,0)) AS '가을',
SUM(If(season='겨울',amount,0)) AS '겨울',
SUM(amount) AS "합계"
FROM pivotTest
GROUP BY uName;


-- 계절별 사용자  판매 수량 및 합계를 집계
-- 1)계절별 수량 집계
SELECT season, SUM(amount)
FROM pivotTest
GROUP BY season;

-- 2) 사용자 판매 수량 및 합계
SELECT season,
SUM(If(uName='김범수',amount,0)) AS '김범수 ',
SUM(If(uName='윤종신',amount,0)) AS '윤종신 ',
SUM(amount) AS "계절별 합계"
FROM pivotTest
GROUP BY season;

-- JOIN

-- 구매 테이블에서 회원 정보를 추가해서 보고 싶다
-- 회원 정보를 알 수 있는 최소의 단위로 FK
-- userID, 회원명, 연락처, 주소, 구매한 상품, 구매수량
-- 회원테이블과 구매테이블 JOIN
-- 1) 기본 조인
SELECT * FROM buyTBL
INNER JOIN userTBL
ON buyTBL.userID = userTBL.userID; 
	-- 조인가능 확인. 여기서 멈추면 안됨. 유저아이디 중복, 정확한 리스트 아님
	
-- 2)userID, 회원명, 연락처, 주소, 구매한 상품, 구매수량 특정 컬럼만
-- 중복되는 컬럼명때문에 테이블명.컬럼명 or 테이블별칭. 컬럼명 해야 한다
SELECT userTBL.userID, name, CONCAT(mobile1, mobile2),addr, prodName, amount 
FROM buyTBL
INNER JOIN userTBL
ON buyTBL.userID = userTBL.userID
WHERE name = '조용필';  -- 조용필씨만 찾음

-- 3)주소가 서울 사람들의 구매 정보를 검색
SELECT userTBL.userID, name, CONCAT(mobile1, mobile2),addr, prodName, amount 
FROM buyTBL
INNER JOIN userTBL
ON buyTBL.userID = userTBL.userID
WHERE addr = '서울';

-- 4)테이블명에 별칭을 추가 (한글별칭은 보고서에는 사용하지만 주로  영어로 사용한다)
SELECT U.userID, U.name, CONCAT(U.mobile1, U.mobile2) AS "mobile", U.addr, B.prodName, B.amount  -- 별칭추가
FROM buyTBL B -- 별칭추가
INNER JOIN userTBL U  -- 별칭추가
ON B.userID = U.userID
WHERE U.addr = '서울';


-- 소속 확인
SELECT U.userID AS "U.userID", B.userID AS "B.userID", U.name, CONCAT(U.mobile1, U.mobile2) AS "mobile", U.addr, B.prodName, B.amount  -- 별칭추가
FROM buyTBL B 
INNER JOIN userTBL U 
ON B.userID = U.userID
WHERE U.addr = '서울';

-- 조인하게 되면 buytbl에서 검색할 수 없었던 회원정보도 구매 정보를 검색가능하다.
-- 회원명, 주소, 연락처, 가입일 등 컬럼으로 구매정보 검색 가능
-- 오름차순 userID 정렬 
-- 1) 은지원 구매 정보 검색 userID, 회원명, 연락처, 주소, 구매한 상품, 구매수량
SELECT u.userID, u.name, CONCAT(u.mobile1, u.mobile2) AS "mobile" ,u.addr, b.prodName, b.amount 
FROM buyTBL b
INNER JOIN userTBL u
ON b.userID = u.userID
WHERE u.name = '은지원'
ORDER BY prodName;

-- 2) 주소 중에서 서울과 경기지역의 구매 정보 검색
SELECT u.userID, u.name, CONCAT(u.mobile1, u.mobile2) AS "mobile" ,u.addr, b.prodName, b.amount 
FROM buyTBL b
INNER JOIN userTBL u
ON b.userID = u.userID
WHERE addr IN('서울' ,'경기')
ORDER BY userID;

-- 3) 연락처가 없는 사람의 구매정보 검색
SELECT u.userID, u.name, CONCAT(u.mobile1, u.mobile2) AS "mobile" ,u.addr, b.prodName, b.amount 
FROM buyTBL b
INNER JOIN userTBL u
ON b.userID = u.userID
WHERE u.mobile1 IS NULL     -- CONCAT(mobile1, mobile2)
ORDER BY userID;


-- 4) 회원 중에 키가 180 이상인 회원의 구매 정보만 검색
SELECT u.userID, u.name, CONCAT(u.mobile1, u.mobile2) AS "mobile", u.addr, b.prodName, b.amount , u.height 
FROM buyTBL b
INNER JOIN userTBL u
ON b.userID = u.userID
WHERE u.height >= 180
ORDER BY userID;

-- 5) 회원 중에 모든 회원의 평균 키보다 작은 회원의 구매정보만 검색

-- 5-1) 평균키를 구함
SELECT AVG(height) FROM userTBL;

-- 5-2)평균키보다 작은 회원 구매 정보 검색
SELECT u.userID, u.name, CONCAT(u.mobile1, u.mobile2) AS "mobile", u.addr, b.prodName, b.amount, u.height
FROM buyTBL b
INNER JOIN userTBL u
ON b.userID = u.userID
WHERE height <= (SELECT AVG(height) FROM userTBL)
ORDER BY userID; 

-- 6) 구매한 적이 있었던 회원 중복제거  DISTINCT
SELECT DISTINCT u.userID, u.name, u.addr
FROM buyTBL b
INNER JOIN userTBL u
ON b.userID = u.userID;


-- join 없이 where절로 조인 만들기
SELECT u.userID, u.name, u.addr
FROM BUYTBL b, usertbl u 
WHERE b.userID = u.userID;  


-- join 없이) 평균키보다 작은 회원들 출력
SELECT u.userID, u.name, u.addr, u.height
FROM BUYTBL b, usertbl u 
WHERE b.userID = u.userID AND u.height <= (SELECT AVG(height) FROM userTBL)
ORDER BY userID;  


-- 학생 - 학생_동아리 - 동아리 : many to many 는 학생과 동아리가 바로 관계불가능 - 바로 조인할 수 없다.
-- 학생테이블(이름, 지역)
-- 동아리 테이블( 동아리명, 동아리방 호수)
-- 학생_동아리 (넘버, 학생이름, 동아리명)

-- 각 학생의 이름, 지역, 가입한 동아리, 동아리방 정보 검색 
-- 학생 테이블 -> 학생_동아리 -> 동아리 테이블 


-- 세 개의 테이블 샘플

-- 1)stutbl
CREATE TABLE stuTBL
(stuName VARCHAR(10) NOT NULL PRIMARY KEY,
addr CHAR(4) NOT NULL);

-- 2)clubtbl  
CREATE TABLE clubTBL
(clubName VARCHAR(10) NOT NULL PRIMARY KEY,
roomNo CHAR(4) NOT NULL);

-- 3)stdclubtbl pk ->fk
CREATE TABLE stdclubTBL
(num int AUTO_INCREMENT NOT NULL PRIMARY KEY,
stuName VARCHAR(10) NOT NULL,
clubName VARCHAR(10) NOT NULL,
FOREIGN KEY (stuName) REFERENCES stuTBL(stuName),
FOREIGN KEY (clubName) REFERENCES clubTBL(clubName));

-- 테이블 확인하기

DESC stutbl;
DESC clubtbl;
DESC stdclubtbl;

-- 4)내용 넣기 insert
INSERT INTO stuTBL VALUES (N'김범수', N'경남'),(N'성시경', N'서울'),
								  (N'조용필', N'경기'),(N'은지원', N'경북'),(N'바비킴', N'서울');
								  
/** 위와 같음
INSERT INTO stuTBL VALUES
SELECT DISTINCT u.name, u.addr
FROM buytbl b
INNER JOIN userTBL u
ON b.userID=u.userID order by u.name;
**/								  
								  
INSERT INTO clubTBL VALUES (N'수영', N'101호'),(N'바둑', N'102호'),
								  (N'축구', N'103호'),(N'봉사', N'104호');

INSERT INTO stdclubTBL VALUES (NULL, N'김범수', N'바둑'),(NULL, N'김범수', N'축구'),
								  (NULL, N'조용필', N'축구'),(NULL, N'은지원', N'축구'),(NULL, N'은지원', N'봉사'),
								  (NULL, N'바비킴', N'봉사');								  



-- 테이블 내용 확인하기

SELECT * FROM stutbl;
SELECT * FROM clubtbl;
SELECT * FROM stdclubtbl;

-- 다: 다 관계에서의 데이터 삭제 순서 : 학생_동아리 테이블 삭제 -> 학생 테이블 삭제, 동아리 테이블

-- 학생기준으로 학생 이름/지역/가입한 동아리/ 동아리방 출력

SELECT s.stuName, s.addr, c.clubName, c.roomNo
FROM stuTBL s
	INNER JOIN stdclubTBL sc
	ON s.stuName = sc.stuName
	INNER JOIN clubTBL c
	ON sc.clubName = c.clubName
ORDER BY s.stuName;


 -- 동아리 기준으로 동아리 명, 동아리 방, 학생 이름, 지역 출력
  
SELECT c.clubName, c.roomNo, s.stuName, s.addr
FROM clubTBL c
	INNER JOIN stdclubTBL sc
	ON c.clubName = sc.clubName
	INNER JOIN stuTBL s
	ON sc.stuName = s.stuName
ORDER BY c.clubName;


-- OUTER JOIN  비주류 데이터를 찾을 때 -> 소속되지 않은 학생, 아무도 가입하지 않은 동아리 

-- 회원 구매 목록을 조인 ->5명
-- 회원을 기준으로 구매 목록을 검색(구매하지 않은 회원도 포함)
SELECT u.userID, u.name, CONCAT(u.mobile1,u.mobile2) AS '연락처', u.addr, b.prodName, b.amount
FROM userTBL u
LEFT OUTER JOIN buyTBL b
ON u.userID = b.userID
ORDER BY b.amount, name;

-- 회원을 기준으로 구매 목록을 검색(구매하지 않은  회원들만)
SELECT u.userID, u.name, CONCAT(u.mobile1,u.mobile2) AS '연락처', u.addr, b.prodName, b.amount
FROM userTBL u
LEFT OUTER JOIN buyTBL b
ON u.userID = b.userID
WHERE b.prodName IS NULL
ORDER BY b.amount, name;


--  모든 구매 목록이 나오도록 검색 
-- 1) buytbl을 left outer join 기준으로(통상적)
SELECT u.userID, u.name, CONCAT(u.mobile1,u.mobile2) AS '연락처', u.addr, b.prodName, b.amount
FROM buyTBL b
 LEFT OUTER JOIN userTBL u
ON b.userID = u.userID
ORDER BY b.amount, name;

-- 2) right 기준으로 변경
SELECT u.userID, u.name, CONCAT(u.mobile1,u.mobile2) AS '연락처', u.addr, b.prodName, b.amount
FROM userTBL u
RIGHT OUTER JOIN buyTBL b
ON u.userID = b.userID
ORDER BY b.amount, name;

-- 3) 회원과 구매 목록 모두 포함되는 데이터 full 기능은 마리아디비에는 없다!
SELECT u.userID, u.name, CONCAT(u.mobile1,u.mobile2) AS '연락처', u.addr, b.prodName, b.amount
FROM userTBL u
FULL OUTER JOIN buyTBL b
ON u.userID = b.userID
ORDER BY b.amount, name;

-- 이건 오류남

-- union 사용 (중복을 제거한 전체)
-- 가입하지 않은 학생 ,동아리에 가입한 학생  , 한 명도 가입하지 않은 동아리 
SELECT s.stuName, s.addr, c.clubName, c.roomNo
FROM stuTBL s
LEFT OUTER JOIN stdclubTBL sc
ON s.stuName = sc.stuName     
LEFT OUTER JOIN clubTBL c
ON sc.clubName = c.clubName
UNION
SELECT s.stuName, s.addr, c.clubName, c.roomNo
FROM stuTBL s
LEFT OUTER JOIN stdclubTBL sc
ON sc.stuName = s.stuName
RIGHT OUTER JOIN clubTBL c
ON sc.clubName = c.clubName;


-- 중복제거한 후 합침

SELECT stuName, addr FROM stuTBL
UNION
SELECT clubName, roomNo FROM clubTBL;

-- 중복제거 없이 합침 -> 속도가 빠름 
SELECT stuName, addr FROM stuTBL
UNION ALL
SELECT clubName, roomNo FROM clubTBL;


-- 세 개의 테이블로 outer join

-- 학생기준으로 동아리 가입하지 않은 학생 포함해서 목록 출력
SELECT s.stuName, s.addr, c.clubName, c.roomNo
FROM stuTBL s
LEFT OUTER JOIN stdclubTBL sc
	ON s.stuName = sc.stuName
LEFT OUTER JOIN clubTBL c
	ON sc.clubName = c.clubName
ORDER BY c.clubName;

-- 동아리에 가입하지 않은 학생만 출력

SELECT s.stuName, s.addr, c.clubName, c.roomNo
FROM stuTBL s
LEFT OUTER JOIN stdclubTBL sc
	ON s.stuName = sc.stuName
LEFT OUTER JOIN clubTBL c
	ON sc.clubName = c.clubName
WHERE c.clubName IS NULL
ORDER BY c.clubName;

-- 아무도 가입하지 않은 동아리 검색

SELECT  c.clubName, c.roomNo, s.stuName, s.addr
FROM clubTBL c
LEFT OUTER JOIN stdclubTBL sc
	ON sc.clubName  = c.clubName
LEFT OUTER JOIN stuTBL s
	ON sc.stuName = s.stuName
WHERE s.stuName IS NULL	
ORDER BY c.clubName;

-- or right로 변경

SELECT s.stuName, s.addr, c.clubName, c.roomNo
FROM stuTBL s
LEFT OUTER JOIN stdclubTBL sc
	ON s.stuName = sc.stuName
RIGHT OUTER JOIN clubTBL c
	ON sc.clubName = c.clubName
-- WHERE s.stuName IS NULL
ORDER BY c.clubName;


-- cross join  테이블*테이블의 수가 검색  (조인조건없음, 의미없는 데이터, 더미데이터 만들기)
-- 조인 할 때 조인 조건 확인 필수 on 또는 where 절에 조인 조건 확인      
SELECT * FROM buyTBL 
CROSS JOIN userTBL;

SELECT * FROM buyTBL, userTBL ;


-- SELF JOIN 
-- 1) emptbl 생성

CREATE TABLE empTBL (
emp CHAR (3),
manager CHAR(3),
empTel VARCHAR(8));

INSERT INTO empTBL VALUES (N'나사장',NULL,'0000');
INSERT INTO empTBL VALUES (N'김재무',N'나사장','2222');
INSERT INTO empTBL VALUES (N'김부장',N'김재무','2222-1');
INSERT INTO empTBL VALUES (N'이부장',N'김재무','2222-2');
INSERT INTO empTBL VALUES (N'우대리',N'이부장','2222-2-1');
INSERT INTO empTBL VALUES (N'지사원',N'이부장','2222-2-2');
INSERT INTO empTBL VALUES (N'이영업',N'나사장','1111');
INSERT INTO empTBL VALUES (N'한과장',N'이영업','1111-1');
INSERT INTO empTBL VALUES (N'최정보',N'나사장','3333');
INSERT INTO empTBL VALUES (N'윤차장',N'최정보','3333-1');
INSERT INTO empTBL VALUES (N'이주임',N'윤차장','3333-2');

-- 2) 데이터확인

SELECT * FROM empTBL
ORDER BY empTel;


-- 김부장님의 직속 상관의 연락처

SELECT emp, empTel FROM empTBL
WHERE emp = (SELECT manager FROM empTBL WHERE emp = '김부장');

- 부하직원명, 직속상관명, 직속상관 연락처

SELECT e.emp AS '부하직원', m.emp AS '직속상관', m.empTel AS '직속상관연락처'
FROM empTBL e
INNER JOIN  empTBL m
ON e.manager = m.emp    -- 사장님을 제외한 직속상관이 있는 사람 모두 
-- WHERE e.emp = '김부장'; -- 김부장의 상관만 나옴

-- 사장님도 포함하고 싶어요
SELECT e.emp AS '부하직원', m.emp AS '직속상관', m.empTel AS '직속상관연락처'
FROM empTBL e
LEFT OUTER JOIN  empTBL m
ON e.manager = m.emp;

-- 사장님만 뽑고 싶어요. (직속상관이 없는 직원만)
SELECT e.emp AS '부하직원', m.emp AS '직속상관', m.empTel AS '직속상관연락처'
FROM empTBL e
LEFT OUTER JOIN  empTBL m
ON e.manager = m.emp
WHERE e. manager IS NULL;


-- RIGHT로 바꾸기

SELECT m.emp AS '부하직원', e.emp AS '직속상관', e.empTel AS '직속상관연락처'
FROM empTBL m
RIGHT OUTER JOIN  empTBL e
ON m.emp = e.manager;



-- 프로시저

-- IF ELSE END IF 사용해서 프로시저 등록, 호출 

-- employees db의 employees 테이블에 입사일이 얼마나 됐는지 출력하는 프로시서 생성

-- 1) 입사일 계산하는 쿼리부터 생성
-- 오늘 날짜 - 입사일 차이 계산

SELECT emp_no, DATEDIFF(CURRENT_DATE(), hire_date) AS "근무일수"FROM employees.employees;
SELECT emp_no, TRUNCATE(DATEDIFF(CURRENT_DATE(), hire_date)/ 365,0) AS "근무년수"FROM employees.employees;

-- 2) 입사일이 35년 이상 넘은 사람만 출력하도록 조건문으로 실행



DELIMITER $$  -- ; 대체 기호
CREATE PROCEDURE checkHIREDATEProc(IN empno int)
BEGIN
		DECLARE hireDATE DATE;   -- 입사일
		DECLARE curDATE DATE;    -- 오늘
		DECLARE days INT;        -- 근무한 일수
		
		SELECT hire_date INTO hireDate -- 변수이름 지정
			FROM employees.employees
			WHERE emp_no = empno;
	
		
		SET curDATE = CURRENT_DATE();
		SET days = DATEDIFF(CURRENT_DATE(), hireDate);
		
		IF (days/365) >= 35 THEN 
						SELECT CONCAT('입사한지', days, '일이 지났습니다. 축하합니다!') AS result;
		ELSE 				
						SELECT CONCAT('입사한지', days, '일밖에 안되었네여. 열심히 일하세요.') AS result;
		END IF;
		
END $$
DELIMITER ;		

-- DROP PROCEDURE checkHIREDATEProc;  // DROP PROCEBURE IF EXISTS checkHIREDATEProc;  -- 프로시저 삭제

CALL checkHIREDATEProc(10001);											