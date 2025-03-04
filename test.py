import pandas as pd
import psycopg2
import datetime


# 🔹 Configuración de PostgreSQL
DB_CONFIG = {
    "dbname": "FAST_API",
    "user": "postgres",
    "password": "232629oria",
    "host": "localhost",
    "port": "5432",
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