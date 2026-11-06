from idlelib import query

from database.DB_connect import DBConnect
from model.libro_DTO import Libro

"""
    LIBRO DAO
    Gestisce le operazioni di accesso al database relative ai libri (Effettua le Query).
"""

class LibroDAO:
    def __init__(self):
        pass

    #Todo
    def select_all_books(self,biblioteca=None,genre=None):

        cnx = DBConnect.get_connection()
        if cnx is not None:
            if biblioteca is None and genre is None:
                query = "SELECT * FROM libro "
                cursor=cnx.cursor()
                cursor.execute(query)
                result=[]
                for row in cursor.fetchall():
                    result.append(Libro(row[0],row[1],row[2],row[3],row[4],row[5]))


                print(result)
                cursor.close()
                return result
            elif biblioteca is None and genre is not None:
                query = """SELECT *
                                 FROM Libro
                                 WHERE genere = %s"""
                cursor = cnx.cursor()

                cursor.execute(query, (genre,))
                result = []
                for row in cursor.fetchall():
                    result.append(Libro(row[0], row[1], row[2], row[3], row[4], row[5]))

                cnx.close()

                return result
            elif biblioteca is not None and genre is None:
                query = f"""SELECT * 
                                     FROM libro 
                                     WHERE id_biblioteca ={biblioteca}


                          """
                cursor = cnx.cursor()
                cursor.execute(query)

                result = []
                for row in cursor.fetchall():
                    result.append(Libro(row[0], row[1], row[2], row[3], row[4], row[5]))

                cnx.close()
                return result

            elif biblioteca is not None and genre is not None:
                query = f"""SELECT * 
                                       FROM libro 
                                       WHERE id_biblioteca ={biblioteca} AND genere = %s
                                       """
                cursor = cnx.cursor()
                cursor.execute(query, (genre,))
                result = []
                for row in cursor.fetchall():
                    result.append(Libro(row[0], row[1], row[2], row[3], row[4], row[5]))
                cursor.close()

                return result


        else:
            print("Connection Error")

    def generi(self):
        cnx = DBConnect.get_connection()
        if cnx is not None:
            cursor=cnx.cursor()
            cursor.execute("SELECT * FROM libro")
            insie=[]
            for row in cursor.fetchall():
                if row [3] not in insie:
                    insie.append(row[3])
            print(insie)
            cursor.close()
            return insie







