import pyodbc

from db.database import MSSQL
from db.models.sede import SedeModel

class SedeService:
    table = "dbo.sede"       # nombre de la tabla
    view = "dbo.sede"        # en caso de que use una vista
    fields = ", ".join(SedeModel.get_field_names())

    # def create(self, data):
    
    
    def read(self, id = None):
        if not id: 
            return {"message": "Falta definir el id"}

        sql = f'SELECT {self.fields} FROM {self.view} WHERE idSede=?'
        
        try:
            with MSSQL().cursor() as cursor:
                cursor.execute(sql, id)
                ret = MSSQL.result_to_dict(cursor)

        except pyodbc.Error as e:
            ret = {"message": "error del sistema, falló SQL Query"}
            print(f'SQL Query Failed: {e}')
        
        return ret
    
    
    # def update(self, data, id = None):


    # def delete(self, id = None):


    def list(self, page=1, per_page=20):
        """
        Listado de sedes
        """
        from_page = ((page - 1) * per_page) + 1        
        sql = f"SELECT {self.fields} " \
              f"FROM {self.view} " \
               "ORDER BY nombre " \
              f"OFFSET {from_page} ROWS FETCH NEXT {per_page} ROWS ONLY"
        try:
            with MSSQL().cursor() as cursor:
                cursor.execute(sql)
                ret = MSSQL.result_to_dict(cursor)

        except pyodbc.Error as e:
            ret = {"message": "error del sistema, falló SQL Query"}
            print(f'SQL Query Failed: {e}')
        
        return ret
