# 데이타베이스 관리 파일
import mysql.connector


# 데이타베이스 접속 함수
def get_connection():
    conn = mysql.connector.connect(
        host='127.0.0.1',
        user='test',
        password='0000',
        db='inside_trip',
        charset='utf8')
    return conn
