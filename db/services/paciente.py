import pyodbc

from db.database import MSSQL
from db.models.paciente import Paciente


class PacienteSrv:
    """
    Modelo CRUD para actualización de tabla

    Métodos:
    List   - Lista todos los registros
    Create - crea un registro
    """
    
    table = "dbo.pacientes"       # nombre de la tabla
    view = "dbo.pacientes"        # en caso de que use una vista
    fields = ", ".join(Paciente.get_field_names())

    def list(self, page=1, per_page=20):
        """
        Lista registros paginando en grupo de 20
        """
        from_page = ((page - 1) * per_page) + 1
        sql = f"SELECT {self.fields} " \
              f"FROM {self.view} " \
               "ORDER BY apellido1, apellido2, nombre  " \
              f"OFFSET {from_page} ROWS FETCH NEXT {per_page} ROWS ONLY"
        
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
        sql = f"SELECT {self.fields} FROM {self.view} WHERE id_pac=?"
        return self._read(sql, id)

    def read_by_dni(self, id: str=None):
        sql = f"SELECT {self.fields} FROM {self.view} WHERE dni=?"
        return self._read(sql, id)

    def read_tutor(self, id: str=None):
        "obtiene el paciente y sus adherentes"
        sql = "EXEC sp_buscar_pacientes_por_pac @id_pac=?"
        return self._read(sql, id)

    def read_tutor_by_dni(self, id: str=None):
        "obtiene el paciente y sus adherentes buscando por DNI"
        sql = "EXEC sp_buscar_pacientes_por_dni @dni=?"
        return self._read(sql, id)
