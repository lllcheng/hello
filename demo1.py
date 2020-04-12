import pymysql
db = pymysql.connect(host="192.144.148.91",user="ljtest",password="123456",db="ljtestdb")
cursor = db.cursor()
cursor.execute("show tables;")
res = cursor.fetchall()
print(res)
