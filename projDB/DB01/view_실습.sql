-- 아르바이트 생에게는 회원정보 테이블에서. 히원아이디와 주소만 공개하고 싶다
-- 회원 테이블에서 회원아이디, 주소만 뷰로 생성해서 제공


-- 1) 회원테이블에서 아이디, 조소만 추출하는 쿼리 만들기
SELECT memberID, memberAddress FROM membertbl;

-- 2) view로 만들기
CREATE VIEW uv_memberTBL
AS
  SELECT memberID, memberAddress FROM membertbl;
  
  
-- 3)view죠회

SELECT * FROM uv_membertbl;   


-- 4) 아이디와 이름만 view로 만들기

SELECT memberID, memberName FROM membertbl;

-- 4-1) view 생성
CREATE VIEW uv2_memberTBL
AS
  SELECT memberID, memberName FROM membertbl;
  
-- view 생성

SELECT * FROM uv2_membertbl;
  


  