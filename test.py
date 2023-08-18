from db.database import MSSQL
from db.services.usuario import UsuarioSrv
from db.models import UsuarioModel


srv = UsuarioSrv()

print( srv.read(1) )

print( "-----------------------" )

print( srv.list() )

# model = UsuarioModel()

# with db.cursor() as cursor:
#     cursor.execute("SELECT * FROM usuario WHERE id=1;")
#     print(cursor.fetchall())
