-- 점수를 주면 학점을 계산해주는 프로시저 등록

DROP PROCEDURE IF EXISTS caseProc;
DELIMITER $$
CREATE PROCEDURE caseProc(IN point int)
BEGIN
	DECLARE credit CHAR(1);  -- 학점을 담을 변수 

CASE	
   WHEN point >= 90 THEN
   	SET credit = 'A';
   WHEN point >= 80 THEN
   	SET credit = 'B';
   WHEN point >= 70 THEN
  	   SET credit = 'C';
   WHEN point >= 60 THEN
   	SET credit = 'D';
   ELSE
   	SET credit = 'F';

END CASE;
SELECT CONCAT('취득점수==>',point) AS '점수', CONCAT('학점==>',credit) AS '학점'; -- 결과출력
END $$

DELIMITER ;

CALL caseProc(83);   -- 실행


-- 구매 테이블에 구매액(price*amount)이 1500원 이상인 고액은 최우수고객 
-- 1000원 이상인 고객은 우수고객
-- 1원 이상 고객은 일반고객
-- 전혀 실적이 없는 고객은 유령고객

-- 1) 구매액을 회원별로 계산 -> 구매액 순으로 내림차순

SELECT userID, SUM(price*amount) AS '총구매액'
FROM buyTBL
GROUP BY userID
ORDER BY 2 DESC;

-- 2) userID, 회원명, 총 구매액 보여주기 

SELECT b.userID, u.name, SUM(b.price*b.amount) AS '총구매액'
FROM buyTBL b
INNER JOIN userTBL u
ON b.userID = u.userID
GROUP BY userID, u.name
ORDER BY 3 DESC;

-- 3) 유령고객 찾기 (NUll 찾기) INNER join -> outer join

SELECT b.userID, u.name, SUM(b.price*b.amount) AS '총구매액'
FROM buyTBL b
RIGHT OUTER JOIN userTBL u    -- 구매안한 회원은 회원테이블에 있음 
ON b.userID = u.userID
GROUP BY userID, u.name
ORDER BY 3 DESC;

-- 최우수 고객 우수고객 일반고객 유령고객 

SELECT b.userID, u.name, SUM(b.price*b.amount) AS '총구매액',
-- 구매액에 따른 고객 분류  CASE
CASE
	WHEN (SUM(b.price*b.amount) >= 1500) THEN '최우수고객'
	WHEN (SUM(b.price*b.amount) >= 1000) THEN '우수고객'
	WHEN (SUM(b.price*b.amount) >= 1) THEN '일반고객'
	ELSE '유령고객'
END AS '고객등급' -- 컬럼별칭
FROM buyTBL b
RIGHT OUTER JOIN userTBL u     
ON b.userID = u.userID
GROUP BY userID, u.name
ORDER BY 3 DESC;


-- 스토어드 함수
-- 상품 금액과 수량을 주면 구매액을 계산해주는 함수 
DROP FUNCTION IF EXISTS purchaseFunc;
DELIMITER $$
CREATE FUNCTION purchaseFunc(price int, amount int)
RETURNS INT
BEGIN
RETURN Price*amount;
END $$
DELIMITER ;

SELECT userID, price, amount, (price*amount), purchaseFunc(price,amount) AS '총구매액'
FROM BUYTBL;

SELECT purchaseFunc(6,4929);   -- 함수값 실행


-- 출생연도를 입력하면 나이가 출력되는 함수

DROP FUNCTION IF EXISTS GETAGEFUNC;
DELIMITER $$
CREATE FUNCTION GETAGEFUNC(Byear INT)
	RETURNS INT
BEGIN
 DECLARE age INT ;
 SET age = YEAR(CURDATE()) - Byear ;
 RETURN age ;
 END $$
DELIMITER ;

SELECT YEAR(birth_date), GETAGEFUNC(YEAR(birth_date)) FROM employees.employees
ORDER BY 2 ASC;

SELECT userID, name, birthyear, GETAGEFUNC(birthyear) FROM usertbl
ORDER BY 4 ASC;

SHOW CREATE FUNCTION GETAGEFUNC;


-- 