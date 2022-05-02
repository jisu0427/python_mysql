# pypi.org -> 파이썬 공식 라이브러리 관리하는 사이트

# MySQL 과 Python을 연결하는 코드
# try 라고 나오면, 들여쓰기 되어있는 문장들을 실행하라는 뜻.

import mysql.connector
from mysql.connector.errors import Error

try:
    connection = mysql.connector.connect(
        host = 'AWS 엔드포인트 주소',
        database = 'streamlit_db',
        user = 'python_user',
        password='2105'
    )
    if connection.is_connected():
        df_info = connection.get_server_info()
        print('MySQL indo', df_info)
# 위 코드를 실행하다 에러가 발생하면 except 실행
except Error as e:
    print('Error while connecting to MySQL',e)

finally:
    if connection.is_connected():
        if connection.is_connected():
            cursor.close()
            connection.close()
            print('MySQL connection is closed')
        else :
            print('connection does not exist')
