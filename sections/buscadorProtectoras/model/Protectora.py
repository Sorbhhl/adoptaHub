from pydantic import BaseModel

class Protectora(BaseModel):
    number: int = 0
    name: str = ""
    phone: str = ""
    web: str = ""
    mailto: str = ""
    facebook: str = ""
    comunidad_autonoma: str = ""
    paginas: str = ""
    da_datos: int = 0


