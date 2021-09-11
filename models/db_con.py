import psycopg2

class DBConnection():
  conn = None
  curs = None
  
  def connect(self):
    try:
      print('Connecting to the database')
      self.conn = psycopg2.connect("dbname=cuetionario user=test password=12345")
      self.curs = self.conn.cursor()
    except (Exception, psycopg2.DatabaseError) as error:
      print(error)

  def query(self, query):
    commit = False
    db_version = None
    if ('INSERT' in query) or ('UPDATE' in query):
      commit = True
    try:
      self.curs.execute(query)
      if commit:
        self.conn.commit()
      else:
        db_version = self.curs.fetchall()
      self.curs.close()
      return db_version
    except (Exception, psycopg2.DatabaseError) as error:
      print(error)
      return 'error en la consulta'

  def close(self):
    if self.conn is not None:
        self.conn.close()
        print('Dabase connection closed.')