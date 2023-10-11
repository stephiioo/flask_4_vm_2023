import os
from dotenv import load_dotenv
from sqlalchemy import create_engine, text
from faker import Faker
from random import choice

# Load environment variables
load_dotenv()

# Database connection settings from environment variables
DB_HOST = os.getenv("52.186.170.255")
DB_DATABASE = os.getenv("stephie")
DB_USERNAME = os.getenv("sogbebor")
DB_PASSWORD = os.getenv("Stephio03$$$")
DB_PORT = int(os.getenv("DB_PORT", 3306))
DB_CHARSET = os.getenv("DB_CHARSET", "utf8mb4")

# Connection string
conn_string = (
    f"mysql+pymysql://{DB_USERNAME}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_DATABASE}"
    f"?charset={DB_CHARSET}"
)

# Create a database engine
db_engine = create_engine(conn_string, echo=False)
fake = Faker()

def insert_fake_data(engine, num_patients=100, num_doctors=20, num_appointments=150):
    # Start a connection
    with engine.connect() as connection:
        # Insert fake data into doctors
        for _ in range(num_doctors):
            doctor_name = fake.name()
            specialty = fake.job()
            query = text("INSERT INTO doctors (doctor_name, specialty) VALUES (:doctor_name, :specialty)")
            connection.execute(query, {"doctor_name": doctor_name, "specialty": specialty})

        # Insert fake data into patients
        for _ in range(num_patients):
            patient_name = fake.name()
            doctor_id = choice(range(1, num_doctors + 1))
            query = text("INSERT INTO patients (patient_name, doctor_id) VALUES (:patient_name, :doctor_id)")
            connection.execute(query, {"patient_name": patient_name, "doctor_id": doctor_id})

        # Insert fake data into appointments
        for _ in range(num_appointments):
            patient_id = choice(range(1, num_patients + 1))
            appointment_date = fake.date_between(start_date="-5y", end_date="today")
            query = text("INSERT INTO appointments (patient_id, appointment_date) VALUES (:patient_id, :appointment_date)")
            connection.execute(query, {"patient_id": patient_id, "appointment_date": appointment_date})

        connection.commit()

if __name__ == "__main__":
    insert_fake_data(db_engine)
    print("Fake data insertion complete!")
