# postgresql sample db 에서 contry table 을 이용하여 CRUD 만들기
# 1. contry table의 모든 데이터 조회
# 2. contry table의 모든 데이터 추가
# 3. contry table의 모든 데이터 수정
# 4. contry table의 모든 데이터 삭제
# class로 만들기
import psycopg2
from dotenv import load_dotenv
import os
load_dotenv()
DB_NAME = os.getenv('DBNAME')
USER_NAME = os.getenv('USERNAME')
PASS_WORD = os.getenv('PASSWORD')
HOST_NAME = os.getenv('HOST')
PORT_NUMBER = os.getenv('PORT')
class CountryCRUD:
    def __init__(self):
        self.conn_params = {
            'dbname' : DB_NAME,
            'user' : USER_NAME,
            'password' : PASS_WORD,
            'host' : HOST_NAME,
            'port' : PORT_NUMBER
            
        }
        self.com = None
        self.connect()

    def connect(self):
        """데이터베이스에 연결합니다."""
        try:
            self.conn = psycopg2.connect(**self.conn_params)
            print("데이터베이스에 성공적으로 연결되었습니다.")
        except psycopg2.Error as e:
            print(f"데이터베이스 연결 중 오류가 발생했습니다: {e}")

    def create_country(self, country):
        """country 테이블에 새로운 나라를 추가합니다."""
        print(country)
        with self.conn.cursor() as cur:
            cur.execute("""
                INSERT INTO country (country)
                VALUES (%s) RETURNING country_id;
            """, (country,))
            country_id = cur.fetchone()[0]
            self.conn.commit()
            print(f"국가 '{country}'이(가) country {country_id}로 추가되었습니다.")
            return country_id

    def read_country(self, country_id):
        """country_id 기반으로 국가 정보를 조회합니다."""
        with self.conn.cursor() as cur:
            cur.execute("SELECT * FROM country WHERE country_id = %s;", (country_id,))
            country = cur.fetchone()
            if country:
                print(country)
                return country
            else:
                print("국가를 찾을 수 없습니다.")
                return None

    def update_country(self, country_id, country=None):
        """country 정보를 업데이트합니다."""
        with self.conn.cursor() as cur:
            cur.execute("""
                UPDATE country
                SET country = %s
                WHERE country_id = %s;
            """, (country, country_id))
            self.conn.commit()
            print(f"국가 {country_id}의 정보가 업데이트되었습니다.")

    def delete_country(self, country_id):
        """영화 정보를 삭제합니다."""
        with self.conn.cursor() as cur:
            cur.execute("DELETE FROM country WHERE country_id = %s;", (country_id,))
            self.conn.commit()
            print(f"country {country_id}의 정보가 삭제되었습니다.")
    def create_actor(self, actor_id,)

    def close(self):
        """데이터베이스 연결을 종료합니다."""
        if self.conn:
            self.conn.close()
            print("데이터베이스 연결이 종료되었습니다.")

country_crud = CountryCRUD()
country_id = country_crud.create_country()
country_crud.read_country()
country_crud.update_country()
country_crud.delete_country()
country_crud.close()