sql = "SELECT userID, name, birthYear, addr," \
      "IFNULL(CONCAT(mobile1,'-',mobile2),'-') AS mobile," \
      "IFNULL(height,0) AS height," \
      "IFNULL(mDate, '-') AS mDate " \
      "FROM userTBL"


cur.execute(sql)

print("회원ID   회원명    출생연도    주소    연락처     키    가입날짜")
print("--------------------------------------------------------")

while(True):
    row = cur.fetchone()
    if row == None :
        break
    userID = row[0]
    name = row[1]
    birthYear = row[2]
    addr = row[3]
    mobile = row[4]
    height = row[5]
    mDate = row[6]

    print("%3s %7s %8d %6s %10s %d %5s" % (userID, name, birthYear, addr, mobile, height, mDate))

conn.close()
