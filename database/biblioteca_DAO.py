from database.DB_connect import DBConnect
from model.biblioteca_DTO import Biblioteca

"""
    Biblioteca DAO
    Gestisce le operazioni di accesso al database relative alle biblioteche (Effettua le Query).
"""

class BibliotecaDAO:
    def __init__(self):
        pass

    # TODO+
    def select_all(self):

        cnx= DBConnect.get_connection()
        if cnx is not None:
            print("Connection Successful with the Database ")
            cursor=cnx.cursor()
            cursor.execute("SELECT * FROM biblioteca")
            result=[]
            for row in cursor.fetchall():
                result.append(Biblioteca(row[0],row[1],row[2]))
            cursor.close()
            return result
        else:
            print("Connection Error")







c=BibliotecaDAO()
c.select_all()