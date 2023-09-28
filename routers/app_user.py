from fastapi import APIRouter
from fastapi import Depends
from fastapi.security import OAuth2PasswordRequestForm

from db.models.app_user import AppUserToken
from db.services.app_user import AppUserSrv as UsuarioSrv


app_route = APIRouter(prefix="/usuario")



# List - Lista todos los registros

@app_route.get("/list", name="Listado de usuarios", tags=["Usuarios"])
async def get_users_list(page: int=1, per_page: int=20):
    """Obtiene todos los usuarios de la base de datos"""
    return UsuarioSrv().list(page, per_page)


# Create - crea un registro

# Read - Lee un registro

@app_route.get("/{dni}", name="Obtener usuario", tags=["Usuarios"])
def get_user(dni: str):
    """
    Obtiene un usuario de la base de datos

    Parámetros:
     - dni: Documento identificativo

    Retorno:
     - Objeto JSON con estructura correspondiente al modelo `AppUser`
    """
    return UsuarioSrv().read(dni)


# Update - Actualiza un registro

# Delete - Elimina un registro

# Actions - Otras acciones

@app_route.post("/login", name="Iniciar sesión utilizando Token", tags=["Usuarios"])    # , response_model=Token
# async def login_whith_token(form_data: OAuth2PasswordRequestForm = Depends()):
async def login_whith_token(form_data: AppUserToken = Depends()):    
    """
    ## Iniciar sesión con Token

    ### Parámetros:
    La aplicación puede recibir campos de texto mediante datos de formulario
    - username: Nombre de usuario o correo electrónico
    - password: Su contraseña

    ### Retorno:
    - token de acceso y tipo de token
    """
    access_token = UsuarioSrv.generate_token(form_data.username, form_data.password)
    #return Token(access_token=access_token, token_type="bearer")
    return None
