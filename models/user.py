from models.db_con import DBConnection

class User():
  def createUser(self, nombre, username, password):
    db_connection = DBConnection()
    db_connection.connect()
    query = 'INSERT INTO cuetionario.public.user (nombre, username, password) VALUES ( \'' + nombre + '\', \'' + username + '\', \'' + password + '\');'
    response = db_connection.query(query)
    db_connection.close()
    return response

  def deleteUser(self, username):
    db_connection = DBConnection()
    db_connection.connect()
    query = 'DELETE FROM cuetionario.public.user WHERE username=\''+ username +'\';'
    print(query)
    response = db_connection.query(query)
    db_connection.close()
    return response

  def updateInfoUser(self, nombre):
    self.nombre = nombre

  def showInfoUser(self, username):
    print(self.nombre)
    print(self.username)

  def changePassword(self, username, password):
    db_connection = DBConnection()
    db_connection.connect()
    query = 'UPDATE cuetionario.public.user SET password=\''+password+'\' WHERE username=\''+ username +'\';'
    print(query)
    response = db_connection.query(query)
    db_connection.close()
    return response

  def showAllUsers(self):
    db_connection = DBConnection()
    db_connection.connect()
    response = db_connection.query('SELECT * FROM cuetionario.public.user;')
    db_connection.close()
    return response

  def showOneUserByUsername(self, username):
    db_connection = DBConnection()
    db_connection.connect()
    response = db_connection.query('SELECT id, nombre, username FROM cuetionario.public.user WHERE username = \'' + username + '\';')
    db_connection.close()
    return response

  def showOneUserById(self, id):
    db_connection = DBConnection()
    db_connection.connect()
    response = db_connection.query('SELECT id, nombre, username FROM cuetionario.public.user WHERE id = ' + str(id) + ';')
    db_connection.close()
    return response

  def validUserData(self, username, password):
    db_connection = DBConnection()
    db_connection.connect()
    response = db_connection.query('SELECT id, nombre FROM cuetionario.public.user WHERE username = \'' + username + '\' AND password = \'' + password + '\';')
    db_connection.close()
    return response

# user = User()
# user.createUser('Rosa Meltrozo', 'rosameltrozo', '123456')
# print(user.showAllUsers())
# user.changePassword('rosameltrozo', '12345')
# user.deleteUser('rosameltrozo')
# print(user.showOneUserByUsername('rosameltrozo'))
# print(user.showOneUserById(2))
# print(user.validUserData('rosameltrozo', '12345'))