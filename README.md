# CRUD con FastAPI

Ejemplo simple con **FastAPI** de un CRUD contra una base de datos SQLServer


### Tabla
```sql
CREATE TABLE [dbo].[usuario](
    [id] [int] IDENTITY(1,1) NOT NULL,
    [documento] [varchar](60) NULL,
    [nombres] [varchar](60) NULL,
    [telefono] [varchar](60) NULL,
    [correo] [varchar](60) NULL,
    [ciudad] [varchar](60) NULL,
    [fecha_registro] [datetime] NULL,
PRIMARY KEY CLUSTERED ( [id] ASC ) ON [PRIMARY]
) ON [PRIMARY]
GO

ALTER TABLE [dbo].[usuario] ADD DEFAULT (getdate()) FOR [fecha_registro]
GO
```


### TODO: modificaciones

el campo `documento` debría ser único en la tabla, por lo que habría que poner una restricción a nivel de clave única o en su defecto controlar que no exista el documento en la tabla antes de realizar la creación

```py
if item_save.documento == item.documento:
    raise HTTPException(
        status_code=status.HTTP_400_BAD_REQUEST, detail = "el documento ya existe"
    )
```


# ¿como convertir un row en pydantic.BaseModel?

falta determinar como convertir facilmente un pyodbc.row en un modelo pydantic.BaseModel

```py
import pyodbc
from db.models.paciente import Paciente
from typing import List
from pydantic import TypeAdapter

conn = pyodbc.connect("Driver={SQL Server};Server=OFICINAROBERTOP\SQLEXPRESS;Database=sinfonia_test;Trusted_Connection=yes;")
cursor = conn.cursor()
cursor.execute("SELECT top 1 dni, nombre, apellido1, apellido2, fecha_nacimiento, id_pac, movil, email, sexo FROM dbo.pacientes")
rows = cursor.fetchall()
result = []
for row in rows:
    for field in Paciente.model_fields:
        print(field, row[field])
        result.append(dict(zip(field,row)))
```