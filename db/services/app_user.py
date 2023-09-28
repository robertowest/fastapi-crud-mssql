import pyodbc

from db.database import MSSQL
from db.models.app_user import AppUser, AppUserToken

class AppUserSrv:
    """
    Modelo CRUD para actualización de tabla

    Métodos:
    Create - crea un registro
    Read - Lee un registro
    Update - Actualiza un registro
    Delete - Elimina un registro

    List - Lista todos los registros
    """
    
    table = "dbo.appusers"      # nombre de la tabla
    view = "dbo.appusers_view"  # en caso de que use una vista
    fields = ", ".join(AppUser.get_field_names())

    # def create(self, data):        
    #     sql = f'INSERT INTO {self.table} ([documento], [nombres], [telefono], [correo]) OUTPUT INSERTED.id VALUES (?,?,?,?);'
        
    #     try:
    #         with MSSQL().cursor(commit=True) as cursor:
    #             row = cursor.execute(sql, data.documento, data.nombres, data.telefono, data.correo).fetchone()
    #             ret = {"message": "nuevo registro creado", "id": row[0]}

    #     except pyodbc.Error as e:
    #         ret = {"message": "No se pudo crear un registro", "error": e}
    #         print(f'SQL Query Failed: {e}')
       
    #     return ret
    
    def read(self, dni: str = None):
        if not dni: 
            return {"message": "Falta definir el DNI"}

        sql = f'SELECT {self.fields} FROM {self.view} WHERE dni=?'
        
        try:
            with MSSQL().cursor() as cursor:
                cursor.execute(sql, dni)
                ret = MSSQL.result_to_dict(cursor)

        except pyodbc.Error as e:
            ret = {"message": "error del sistema, falló SQL Query"}
            print(f'SQL Query Failed: {e}')
        
        return ret
    
    # def update(self, data, id = None):
    #     if not id: 
    #         return {"message": "Falta definir el id"}

    #     sql = f"UPDATE {self.table} SET documento=?, nombres=?, telefono=?, correo=? WHERE id=?"

    #     try:
    #         with MSSQL().cursor(commit=True) as cursor:
    #             cursor.execute(sql, data.documento, data.nombres, data.telefono, data.correo, id)
    #             ret = {"message": "registro actualizado correctamente"}

    #     except pyodbc.Error as e:
    #         ret = {"message": "error del sistema, falló SQL Query"}
    #         print(f'SQL Query Failed: {e}')
        
    #     return ret

    # def delete(self, id = None):
    #     if not id: 
    #         return {"message": "Falta definir el id"}

    #     sql = f'DELETE FROM {self.table} WHERE id=?'
        
    #     try:
    #         with MSSQL().cursor(commit=True) as cursor:
    #             cursor.execute(sql, id)
    #             ret = {"message": "registro eliminado correctamente"}

    #     except pyodbc.Error as e:
    #         ret = {"message": "error del sistema, falló SQL Query"}
    #         print(f'SQL Query Failed: {e}')
        
    #     return ret

    def list(self, page=1, per_page=20):
        """
        Lista de usuarios paginando en grupo de 20
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
            print(f'SQL Query Failed: {e}')
        
        return ret


    def generate_token(dni, password):
        # # forma de uso de la generación de token
        # >>> from datetime import datetime, timedelta
        # >>> from typing import Optional
        # >>> from fastapi import Depends, HTTPException, status
        # >>> from fastapi.security import OAuth2PasswordBearer
        # >>> from jose import JWTError, jwt
        # >>> from passlib.context import CryptContext
        # >>> from core.config import Settings
        # >>> settings = Settings()
        # >>> pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
        # >>> data = {'dni': '12345678A', 'pwd': '123456'}
        # >>> to_encode = data.copy()
        # >>> expire = datetime.utcnow() + timedelta(minutes=15)
        # >>> to_encode.update({"exp": expire})
        # >>> jwt.encode(to_encode, settings.SECRET_KEY, algorithm=settings.ALGORITHM)

        # autentica usuario
        user = AppUserSrv.read(dni, password)
        # if not user:
        #     raise HTTPException(
        #         status_code=status.HTTP_401_UNAUTHORIZED,
        #         detail="Datos incorrectos",
        #         headers={"WWW-Authenticate": "Bearer"},
        #     )
        # access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
        # return create_access_token(
        #     data={"sub": user.dni}, expires_delta=access_token_expires
        # )
