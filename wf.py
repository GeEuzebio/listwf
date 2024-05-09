import psycopg2
import csv

# Conecta ao banco de dados
conn = psycopg2.connect(
    dbname="wflibrary",
    user="postgres",
    password="An@5ophia",
    host="3.14.132.96",
    port=5432
)
cur = conn.cursor()

# Caminho para o arquivo CSV
csv_file_path = "alunos.csv"

# Abre o arquivo CSV e insere os dados na tabela
with open(csv_file_path, 'r', encoding='latin-1') as file:
    reader = csv.reader(file)
    next(reader)  # Pula o cabeçalho do CSV
    for row in reader:
        cur.execute(
            "INSERT INTO \"User\" (\"Name\", \"Class\", \"SIGE\", \"Email\", \"PhoneNumber\", \"HasBorrow\", \"HasReservation\") VALUES (%s, %s, %s, %s, %s, %s, %s)",
            (row[4], row[2], row[0], " ", " ", False, False)
        )

# Faz commit da transação
conn.commit()

# Fecha o cursor e a conexão
cur.close()
conn.close()
