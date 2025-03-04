import pandas as pd
import psycopg2
import datetime
from dotenv import load_dotenv
import os

# 🔹 Configuración de PostgreSQL
DB_CONFIG = {
    "dbname": os.getenv("DB_NAME"),
    "user": os.getenv("DB_USER"),
    "password": os.getenv("DB_PASSWORD"),
    "host": os.getenv("DB_HOST"),
    "port": os.getenv("DB_PORT"),
}

QUERY = "SELECT * FROM alert_levels;"

# 🔹 Conexión y extracción de datos
conn = psycopg2.connect(**DB_CONFIG)
df = pd.read_sql(QUERY, conn)
conn.close()

# 🔹 Generar nombre de archivo con fecha
timestamp = datetime.datetime.now().strftime("%Y-%m-%d")
filename = f"data_export_{timestamp}.xlsx"
df.to_excel(filename, index=False, engine="openpyxl")