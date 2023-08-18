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
