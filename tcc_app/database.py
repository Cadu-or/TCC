import psycopg2

class DatabaseConnection:
  def __init__(self, dbname, user, password, host):
    self.dbname = dbname
    self.user = user
    self.password = password
    self.host = host
    self.conn = None

  def connect(self):
    connection_string = f"host={self.host} dbname={self.dbname} user={self.user} password={self.password}"
    self.conn = psycopg2.connect(connection_string)
      
  def execute_query(self, query):
    self.connect()
    cur = self.conn.cursor()
    cur.execute(query)
    result = cur.fetchall()
    cur.close()
    return result
