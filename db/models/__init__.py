from pydantic import BaseModel

class AdaptedModel(BaseModel):
    @classmethod
    def get_field_names(cls,alias=False):
        """Obtener los nombres de campos de una clase pydantic"""
        return list(cls.model_json_schema(alias).get("properties").keys())
