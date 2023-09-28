import pyodbc

from db.database import MSSQL
from db.models.especialidad import EspecialidadModel

# select distinct ActivityGroupLid id, ActivityGroupName nombre from [dbo].[TuoTempo_Activities] where AppEnable=1

class EspecialidadService:
    """
    Modelo CRUD para actualización de tabla

    Métodos:
    List   - Lista todos los registros
    Create - crea un registro
    """
    
    table = "dbo.TuoTempo_Activities"       # nombre de la tabla
    view = "dbo.TuoTempo_Activities"        # en caso de que use una vista
    fields = ", ".join(EspecialidadModel.get_field_names())

    def list(self):
        """
        Lista registros paginando en grupo de 20
        """
        sql =  "SELECT distinct ActivityGroupLid id, ActivityGroupName nombre " \
              f"FROM {self.view} " \
               "WHERE AppEnable=1" \
               "ORDER BY ActivityGroupName"        
        try:
            with MSSQL().cursor() as cursor:
                cursor.execute(sql)
                ret = MSSQL.result_to_dict(cursor)
        except pyodbc.Error as e:
            ret = {"message": "error del sistema, falló SQL Query"}
            print(f"SQL Query Failed: {e}")        
        return ret

    def _read(self, sql: str, id: str):
        if not id: 
            return {"message": "Falta definir el id"}
        try:
            with MSSQL().cursor() as cursor:
                cursor.execute(sql, id)
                ret = MSSQL.result_to_dict(cursor)
        except pyodbc.Error as e:
            ret = {"message": "error del sistema, falló SQL Query"}
            print(f"SQL Query Failed: {e}")        
        return ret

    def read(self, id: str=None):
        sql = f"SELECT ActivityGroupLid id, ActivityGroupName nombre FROM {self.view} WHERE ActivityGroupLid=?"
        return self._read(sql, id)
