import os
from dotenv import load_dotenv
from pandas import read_sql
from sqlalchemy import create_engine, inspect

# Load environment variables from .env file
load_dotenv()

# Define database connection settings
db_settings = {
    "host": os.getenv("52.186.170.255"),
    "database": os.getenv("stephie"),
    "username": os.getenv("sogbebor"),
    "password": os.getenv("Stephio03$$$"),
    "port": int(os.getenv("DB_PORT", 3306)),
    "charset": os.getenv("DB_CHARSET", "utf8mb4"),
}

# Connection string
conn_string = f"mysql+pymysql://{db_settings['username']}:{db_settings['password']}@{db_settings['host']}:{db_settings['port']}/{db_settings['database']}?charset={db_settings['charset']}"

# Create a database engine
db_engine = create_engine(conn_string, echo=False)

def get_table_names(engine):
    """Get a list of table names in the database."""
    inspector = inspect(engine)
    return inspector.get_table_names()

def execute_query_to_dataframe(sql_query, engine):
    """Execute SQL query and return result as a DataFrame."""
    return read_sql(sql_query, engine)

if __name__ == "__main":
    tables = get_table_names(db_engine)
    print("Tables in the database:", tables)

    sql_query = "SELECT * FROM patients"  # Modify as per your table
    df = execute_query_to_dataframe(sql_query, db_engine)
    print(df)
