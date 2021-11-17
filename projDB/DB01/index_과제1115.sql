CREATE TABLE idxTBL (first_name varchar(14), 
							last_name varchar(16), 
							hire_date date);

INSERT INTO idxTBL	
			SELECT first_name, last_name, hire_date
			FROM employees.employees
			LIMIT 1500;
			
SELECT * FROM idxTBL;			
			


SELECT * FROM idxTBL WHERE first_name = 'Mary';


EXPLAIN SELECT * FROM idxtbl WHERE first_name = 'Mary';

-- 실제 데이터에서 검색 

EXPLAIN SELECT * FROM employees.employees WHERE first_name = 'Mary';


-- index를 생성 

CREATE INDEX first_name ON idxtbl(first_name);

-- 다시 겸색 해보기


EXPLAIN SELECT * FROM idxtbl WHERE first_name = 'Mary';										
							