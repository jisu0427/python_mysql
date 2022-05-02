from logging import currentframe
import mysql.connector
from mysql.connector import errors
from datetime import datetime
# from mysql.connector.errors import Error

try :
    # 1. DB 연결
    connection = mysql.connector.connect(
        host = 'AWS 엔드포인트 주소',
        database = 'streamlit_db',
        user = 'python_user',
        password = '2105'
    )

    # 2. 쿼리문 만들기
    current_time = datetime.now()

    query ='''insert into test(name, date) values(%s, %s);'''
    record= [('qqq',current_time), ('yyy',current_time), ('ppp',current_time)]
    # 3. 커넥션으로부터 커서를 가져온다.
    cursor = connection.cursor()
    # 4. 쿼리문을 커서에 넣어서 실행한다.
    cursor.executemany(query, record)
    # 5. 커넥션을 커밋한다 DB에 영구적으로 반영한다.
    connection.commit()

except errors as e :
    print('Error', e)
finally :
    if connection.is_connected() :
        cursor.close()
        connection.close()
        print('MySQL connectionis closed')
