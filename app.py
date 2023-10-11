from flask import Flask, render_template
from sqlalchemy import create_engine, Column, Integer, String, Date, ForeignKey
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy.ext.declarative import declarative_base
from dotenv import load_dotenv
import os  # Import the 'os' module

app = Flask(__name__)

# Load environment variables from .env file
load_dotenv()

# Define a function to create a database connection engine
def create_db_engine():
    db_settings = {
        "DB_HOST": os.getenv("52.186.170.255"),
        "DB_DATABASE": os.getenv("stephie"),
        "DB_USERNAME": os.getenv("sogbebor"),
        "DB_PASSWORD": os.getenv("Stephio03$$$"),
        "DB_PORT": int(os.getenv("DB_PORT", 3306)),
        "DB_CHARSET": os.getenv("DB_CHARSET", "utf8mb4")
    }
    conn_string = (
        f"mysql+pymysql://{db_settings['DB_USERNAME']}:{db_settings['DB_PASSWORD']}@"
        f"{db_settings['DB_HOST']}:{db_settings['DB_PORT']}/{db_settings['DB_DATABASE']}?"
        f"charset={db_settings['DB_CHARSET']}"
    )
    return create_engine(conn_string, echo=False)

# Create a database engine and session
db_engine = create_db_engine()
Session = sessionmaker(bind=db_engine)
session = Session()

# Define your data model using SQLAlchemy
Base = declarative_base()

class Patient(Base):
    __tablename__ = 'patients'
    patient_id = Column(Integer, primary_key=True)
    patient_name = Column(String(255))
    doctor_id = Column(Integer, ForeignKey('doctors.doctor_id'))
    doctor = relationship("Doctor", back_populates="patients")

class Doctor(Base):
    __tablename__ = 'doctors'
    doctor_id = Column(Integer, primary_key=True)
    doctor_name = Column(String(255))
    specialty = Column(String(255))
    patients = relationship("Patient", back_populates="doctor")

class Appointment(Base):
    __tablename__ = 'appointments'
    appointment_id = Column(Integer, primary_key=True)
    patient_id = Column(Integer, ForeignKey('patients.patient_id'))
    appointment_date = Column(Date)
    patient = relationship("Patient", back_populates="appointment")

@app.route('/')
def base():
    return render_template('base.html')

@app.route('/patients')
def show_patients():
    patients = session.query(Patient).join(Doctor).all()
    return render_template('patients.html', data=patients)

@app.route('/doctors')
def show_doctors():
    doctors = session.query(Doctor).outerjoin(Patient).all()
    return render_template('doctors.html', data=doctors)

@app.route('/appointments')
def show_appointments():
    appointments = session.query(Appointment).join(Patient).join(Doctor).all()
    return render_template('appointments.html', data=appointments)

if __name__ == '__main__':
    app.run(debug=True)
