import psycopg2

# 연결 파라미터 설정
conn_params = {
    'dbname': 'testdb',
    'user': 'postgres',
    'password': '2475',
    'host': 'localhost',  # 데이터베이스 서버가 로컬에 있을 경우
}

# 데이터베이스 연결 시도
try:
    conn = psycopg2.connect(**conn_params)
    print("데이터베이스에 성공적으로 연결되었습니다.")
except psycopg2.Error as e:
    print("데이터베이스 연결 중 오류가 발생했습니다.")
    print(e)

# 커서 객체 생성
cur = conn.cursor()

# SQL 쿼리 실행: 테이블 생성
create_table_query = """
CREATE TABLE IF NOT EXISTS users (
    id SERIAL PRIMARY KEY,
    name VARCHAR(50),
    age INT
);
"""
cur.execute(create_table_query)
conn.commit()  # 쿼리 결과를 데이터베이스에 반영

print("테이블이 성공적으로 생성되었습니다.")

# 데이터 삽입 쿼리
insert_query = """
INSERT INTO users (name, age) VALUES (%s, %s);
"""
# 데이터 삽입 실행
cur.execute(insert_query, ('Alice', 24))
conn.commit()

print("데이터가 성공적으로 삽입되었습니다.")

# 데이터 조회 쿼리
select_query = "SELECT * FROM users;"

# 쿼리 실행
cur.execute(select_query)

# 모든 결과 행 가져오기
rows = cur.fetchall()

for row in rows:
    print(row)

# 자원 정리
cur.close()
conn.close()