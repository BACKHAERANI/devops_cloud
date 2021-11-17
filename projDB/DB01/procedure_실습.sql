-- 쿼리 2개를 한 번에 실행하는 myproc() 라는 프로시저 만들기

-- 쿼리 2개 생성

SELECT * FROM memberTBL WHERE memberName = '당탕이';
SELECT * FROM productTBL WHERE productName = ' 냉장고';

-- 2) 프로시저 생성

DELIMITER //
CREATE PROCEDURE myProc()
BEGIN	
	SELECT * FROM memberTBL WHERE memberName = '당탕이' ;
	SELECT * FROM productTBL WHERE productName = uv2_membertbl'냉장고' ;
END //
DELIMITER ;


-- 실행하기

CALL myProc(); 