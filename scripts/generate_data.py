
import sqlite3
from faker import Faker
from tqdm import tqdm

DB_PATH = "database/citizen.db"
NUM_RECORDS = 10_000_000  # Bạn có thể giảm xuống để test nhanh hơn

def init_db():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS citizen (
        perID TEXT PRIMARY KEY,
        name TEXT,
        dob TEXT,
        sex TEXT CHECK(sex IN ('M', 'F'))
    )
    """)
    cursor.execute("CREATE INDEX IF NOT EXISTS idx_name ON citizen(name)")
    cursor.execute("CREATE INDEX IF NOT EXISTS idx_dob ON citizen(dob)")
    conn.commit()
    conn.close()

def generate_fake_data():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    faker = Faker()

    for _ in tqdm(range(NUM_RECORDS), desc="Generating citizens"):
        name = faker.name()
        dob = faker.date_of_birth(minimum_age=0, maximum_age=100).isoformat()
        sex = faker.random_element(elements=('M', 'F'))
        perID = faker.uuid4()
        cursor.execute("INSERT OR IGNORE INTO citizen VALUES (?, ?, ?, ?)", (perID, name, dob, sex))

        if _ % 10000 == 0:
            conn.commit()  # Commit từng đợt nhỏ để tránh overload

    conn.commit()
    conn.close()

if __name__ == "__main__":
    init_db()
    generate_fake_data()
