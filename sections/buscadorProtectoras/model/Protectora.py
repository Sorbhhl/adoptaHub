from pydantic import BaseModel

class Protectora(BaseModel):
    name: str = ""
    phone: str = ""
    web: str = ""
    mailto: str = ""
    comunidad_autonoma: str = ""

