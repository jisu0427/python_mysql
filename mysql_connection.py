import mysql.connector

def get_connection():
   connection = mysql.connector.connect(
        host = 'AWS 엔드포인트 주소',
        database = 'streamlit_db',
        user = 'python_user',
        password='2105'
    )
