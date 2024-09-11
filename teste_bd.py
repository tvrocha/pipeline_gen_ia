import psycopg2
import os
from dotenv import load_dotenv

# Carregar variáveis de ambiente do arquivo .env
load_dotenv()

# Configuração do banco de dados PostgreSQL
DB_HOST = os.getenv("DB_HOST")
DB_NAME = os.getenv("DB_NAME")
DB_USER = os.getenv("DB_USER")
DB_PASS = os.getenv("DB_PASS")

try:
    print(f'Conectando a {DB_HOST}, {DB_NAME}, {DB_USER}, {DB_PASS}')
    conn = psycopg2.connect(
        host=DB_HOST,
        database=DB_NAME,
        user=DB_USER,
        password=DB_PASS,
    )
    print("Conexão com o banco de dados estabelecida.")
    conn.close()
except Exception as e:
    print(f"Erro ao conectar no banco de dados: {e}")
