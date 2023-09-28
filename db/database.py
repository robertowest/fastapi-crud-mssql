import pyodbc
import sys

from contextlib import contextmanager

from core.config import settings


"""
Uso:
    ms_db = MSSQL()
    with ms_db.cursor() as cursor:
            cursor.execute("SELECT @@version;")
            print(cursor.fetchall())
"""
class MSSQL():
    """ 
    Colección de métodos para base de datos MS SQL Server
    """

    def __init__(self):
        self.username = settings.DB_USER
        self._password = settings.DB_PASS
        self.host = settings.DB_HOST
        self.port = settings.DB_PORT
        self.db = settings.DB_NAME
        self._connection = pyodbc.connect(settings.DATABASE_URL)
        # print('Connected to DB:', settings.DATABASE_URL)
        pyodbc.pooling = False

    def __repr__(self):
        return f"MS-SQLServer('{self.username}', <password hidden>, '{self.host}', '{self.port}', '{self.db}')"

    def __str__(self):
        return f"MS-SQLServer módulo para STP en {self.host}"

    def __del__(self):
        self._connection.close()

    @contextmanager
    def cursor(self, commit: bool = False):
        """
        El contextmanager de usará un cursor para operaciones de bases de datos.
        Esta función debe usarse para cualquier consulta u operación de la base de datos que sea necesario.

        :parámetro
        commit: booleano que define si se harán cambios en la base de datos
        """
        cursor = self._connection.cursor()
        try:
            yield cursor
        except pyodbc.DatabaseError as err:
            print("DatabaseError {} ".format(err))
            cursor.rollback()
            raise err
        else:
            if commit:
                cursor.commit()
        finally:
            cursor.close()

    def result_to_dict(cursor):
        """
        Función para devolver los resultados de SQL como un dict.
        Mapea los nombres y valores de la columna para el dict 
        Devuelve 'no se encontraron resultados' si no hay registros
        """
        try: 
            result = []
            columns = [column[0] for column in cursor.description]
            for row in cursor.fetchall():
                result.append(dict(zip(columns,row)))

            # comprueba si hay registros
            if len(result) > 0:
                ret = result
            else:
                ret = {"message": "No se encontraron registros"}

        except pyodbc.Error as e:
            print(e)
            ret = { "message": "Error interno al consultar la base de datos"}
        
        return ret


# if __name__ == '__main__':
#     from ..core.config import settings

#     ms_db = MSSQL()
#     with ms_db.cursor() as cursor:
#             cursor.execute("SELECT @@version;")
#             print(cursor.fetchall())
