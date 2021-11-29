import pymysql

conn= pymysql.connect(host='127.0.0.1', user='root', password='1234',db='sqlDB', charset='utf8')  #데이터베이스 접속
cur = conn.cursor()   #커서

sql = ""

# usertbl의 회원 데이터 insert
# userID, name, birthYear, addr = "", "", "", ""

userID = ""
name = ""
birthYear = ""
addr = ""
mobile1 = ""
mobile2 = ""
height = ""

while(True):
    userID = input("사용자ID ==>")
    if userID =="":
        break
    name = input("사용자 이름==>")
    birthYear = input("사용자 출생연도==>")
    addr = input("사용자 주소==>")
    mobile1 = input("사용자 전화번호 앞 세자리==>")
    mobile2 = input("사용자 전화번호 앞 세자리 제외한 전체==>")
    height = input("사용자 키==>")

    sql = "INSERT INTO userTBL(userID, name, birthYear, addr, mobile1, mobile2, height, mDate) VALUES" \
          "('"+userID+"','"+name+"',"+birthYear+",'"+addr+"','"+mobile1+"','"+mobile2+"',"+height+", curdate())"    # curdate = 나머지는 null
    print(sql)
    cur.execute(sql)

conn.commit()
conn.close()