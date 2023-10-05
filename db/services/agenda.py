import pyodbc

from db.database import MSSQL
from db.models.agenda import AgendaModel


class AgendaService:
    """
    Modelo CRUD para actualización de tabla

    Métodos:
    List   - Lista todos los registros
    Create - crea un registro
    Read   - Lee un registro
    Update - Actualiza un registro
    Delete - Elimina un registro
    """
    
    table = "dbo.agenda"       # nombre de la tabla
    view = "dbo.agenda_view"   # en caso de que use una vista
    fields = ", ".join(AgendaModel.get_field_names())

    def list(self, paciente: str):
        """
        Lista agenda de un paciente a partir de hoy
        """
        sql = f"SELECT {self.fields} " \
              f"FROM {self.view} " \
              f"WHERE id_paciente = '{paciente}' " \
               "ORDER BY dia, hora, minuto"

        try:
            with MSSQL().cursor() as cursor:
                cursor.execute(sql)
                ret = MSSQL.result_to_dict(cursor)

        except pyodbc.Error as e:
            ret = {"message": "error del sistema, falló SQL Query"}
            print(f"SQL Query Failed: {e}")
        
        return ret

    def create(self, data):
        sql = f"INSERT INTO {self.table} (dia, hora, minuto, consulta, paciente, mod_visita, nuevo_pac, pendiente_llegar) " \
               "OUTPUT INSERTED.id VALUES (?,?,?,?,?,?,?,?);"
        try:
            with MSSQL().cursor(commit=True) as cursor:
                row = cursor.execute(sql, 
                                     data.dia, data.hora, data.minuto, data.consulta, data.paciente, 
                                     data.mod_visita, data.nuevo_pac, data.pendiente_llegar).fetchone()
                ret = {"message": "nuevo registro creado", "id": row[0]}

        except pyodbc.Error as e:
            ret = {"message": "No se pudo crear un registro", "error": e}
            print(f"SQL Query Failed: {e}")
       
        return ret
    
    def read(self, id = None):
        if not id: 
            return {"message": "Falta definir el id"}

        sql = f'SELECT {self.fields} FROM {self.view} WHERE id=?'
        
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

        sql = f"UPDATE {self.table} SET dia=?, hora=?, minuto=?, consulta=?, paciente=?, " \
               "mod_visita=?, nuevo_pac=?, pendiente_llegar=? WHERE id=?"

        try:
            with MSSQL().cursor(commit=True) as cursor:
                cursor.execute(sql, 
                               data.dia, data.hora, data.minuto, data.consulta, data.paciente, 
                               data.mod_visita, data.nuevo_pac, data.pendiente_llegar, id)
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
