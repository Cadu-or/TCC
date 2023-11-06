import psycopg2

class DatabaseConnection:
  def __init__(self, dbname, user, password, host, port):
    self.dbname = dbname
    self.user = user
    self.password = password
    self.host = host
    self.port = port
    self.conn = None

  def connect(self):
    if self.conn is None or self.conn.closed != 0:
      self.conn = psycopg2.connect(
          dbname=self.dbname,
          user=self.user,
          password=self.password,
          host=self.host,
          port=self.port
        )

  def execute_query(self, query):
    self.connect()
    cur = self.conn.cursor()
    cur.execute(query)
    result = cur.fetchall()
    cur.close()
    return result

  def close(self):
    if self.conn is not None and self.conn.closed == 0:
      self.conn.close()