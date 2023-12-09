import psycopg2

# Conectar ao banco de dados
conn = psycopg2.connect(
    host="localhost",
    port=5433,
    database="",
    user="",
    password=""
)

# Criar um cursor
cur = conn.cursor()

# Definir a consulta SQL para inserir dados
import csv;

count = 0;
aux = []
with open('corr_mensal_delay_negativo_2.csv', newline='') as arquivo_csv:
    leitor_csv = csv.reader(arquivo_csv)

    for linha in leitor_csv:
        if count > 1 and linha[2] != '':
            code1 = linha[0]
            code2 = linha[1]
            correlacao = f"{float(linha[2]):.3f}"
            delay = int(linha[3])
            count = count+1
            sql = """INSERT INTO "tcc-aplicacao".tb_correlacao (CODE1, CODE2, CORRELATION, DELAY ) VALUES (%s, %s, %s, %s)"""
            dados = (code1, code2, correlacao, delay)
            cur.execute(sql, dados)
            conn.commit()
        else:
            count = count + 1


# Fechar o cursor e a conexão
cur.close()
conn.close()