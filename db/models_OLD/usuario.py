from datetime import date
from pydantic import BaseModel


class Usuario(BaseModel):
    id: int
    documento: str
    nombres: str
    telefono: str
    correo: str
    ciudad: str
    fecha_registro: date




# #Python packages
# from datetime import datetime
# from typing import Optional
# from uuid import UUID
# #Pydantic packages
# from pydantic import BaseModel
# from pydantic import Field
# #Local packages
# from models.user import UserBase

# #Class for Trino Model
# classTrino(BaseModel):
#     id: UUID = Field(
#         ...,
#         title="Trino Id"
#         )
#     content: str = Field(
#         ...,
#         title="Trino content",
#         min_length=1,
#         max_length=256
#         )
#     created_at: datetime = Field(
#         default=datetime.now(),
#     )
#     updated_at: Optional[datetime] = Field(
#         default=datetime.now(),
#     )
#     by: UserBase = Field(
#         ...,
#         title="User who created the trino"
#         )