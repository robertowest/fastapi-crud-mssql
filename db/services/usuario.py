import pyodbc

from db.database import MSSQL

class UsuarioSrv:
    """
    Modelo CRUD para actualización de tabla

    Métodos:
    Create - crea un registro
    Read - Lee un registro
    Update - Actualiza un registro
    Delete - Elimina un registro

    List - Lista todos los registros
    """
    
    table = "dbo.usuario"       # nombre de la tabla
    view = "dbo.usuario"        # en caso de que use una vista

    def create(self, data):        
        sql = f'INSERT INTO {self.table} ([documento], [nombres], [telefono], [correo]) OUTPUT INSERTED.id VALUES (?,?,?,?);'
        
        try:
            with MSSQL().cursor(commit=True) as cursor:
                row = cursor.execute(sql, data.documento, data.nombres, data.telefono, data.correo).fetchone()
                ret = {"message": "nuevo registro creado", "id": row[0]}

        except pyodbc.Error as e:
            ret = {"message": "No se pudo crear un registro", "error": e}
            print(f'SQL Query Failed: {e}')
       
        return ret
    
    def read(self, id = None):
        if not id: 
            return {"message": "Falta definir el id"}

        sql = f'SELECT * FROM {self.view} WHERE id=?'
        
        try:
            with MSSQL().cursor() as cursor:
                cursor.execute(sql, id)
                ret = MSSQL.result_to_dict(cursor)

        except pyodbc.Error as e:
            ret = {"message": "error del sistema, falló SQL Query"}
            print(f'SQL Query Failed: {e}')
        
        return ret
    
    def update(self, data, id = None):
        if not id: 
            return {"message": "Falta definir el id"}

        sql = f"UPDATE {self.table} SET documento=?, nombres=?, telefono=?, correo=? WHERE id=?"

        try:
            with MSSQL().cursor(commit=True) as cursor:
                cursor.execute(sql, data.documento, data.nombres, data.telefono, data.correo, id)
                ret = {"message": "registro actualizado correctamente"}

        except pyodbc.Error as e:
            ret = {"message": "error del sistema, falló SQL Query"}
            print(f'SQL Query Failed: {e}')
        
        return ret

    def delete(self, id = None):
        if not id: 
            return {"message": "Falta definir el id"}

        sql = f'DELETE FROM {self.table} WHERE id=?'
        
        try:
            with MSSQL().cursor(commit=True) as cursor:
                cursor.execute(sql, id)
                ret = {"message": "registro eliminado correctamente"}

        except pyodbc.Error as e:
            ret = {"message": "error del sistema, falló SQL Query"}
            print(f'SQL Query Failed: {e}')
        
        return ret

    def list(self):
        """
        Listado de usuarios
        """
        sql = f'SELECT * FROM {self.view}'

        try:
            with MSSQL().cursor() as cursor:
                cursor.execute(sql)
                ret = MSSQL.result_to_dict(cursor)

        except pyodbc.Error as e:
            ret = {"message": "error del sistema, falló SQL Query"}
            print(f'SQL Query Failed: {e}')
        
        return ret
