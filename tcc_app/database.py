import pyodbc as odbc

class DatabaseConnection:
  def __init__(self, dbname, user, password, host):
    self.dbname = dbname
    self.user = user
    self.password = password
    self.host = host
    self.conn = None

  def connect(self):
    driver = 'SQL SERVER'
    connection_string = f'Driver={driver};Server={self.host};Database={self.dbname};Uid={self.user};Pwd={self.password};Encrypt=yes;TrustServerCertificate=no;Connection Timeout=30;'
    print(connection_string)
    self.conn = odbc.connect(connection_string)
    
  def execute_query(self, query):
    self.connect()
    cur = self.conn.cursor()
    cur.execute(query)
    result = cur.fetchall()
    cur.close()
    return result