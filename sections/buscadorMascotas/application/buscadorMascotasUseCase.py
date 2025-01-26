import logging
import json

class BuscadorMascotasUseCase:
    def __init__(self):
        logging.debug("BuscadorMascotasUseCase initialized")

    def execute(self):
        logging.debug("BuscadorMascotasUseCase executed")
        protectorasComunidadJSON = self.cargarDatos()
        self.leerProtectoras(protectorasComunidadJSON)


    def cargarDatos(self) -> dict:
        logging.debug("cargarDatos() called")
        with open(r"resources\protectoras.json", encoding="utf-8") as file:
            return json.load(file)
        
    def leerProtectoras(self, protectorasComunidadJSON):
        logging.debug("leerProtectoras() called")
        
        for comunidad in protectorasComunidadJSON:
            for protectora in protectorasComunidadJSON[comunidad]:
                
                if not(protectora.get("web") is None or protectora.get("web") == ""):
                    ruta = str(protectora.get("number")) + protectora.get("web")
                    logging.debug(ruta)

                elif not(protectora.get("mailto") is None or protectora.get("mailto") == ""):
                    ruta = str(protectora.get("number")) + protectora.get("mailto")
                    logging.debug(ruta)
                break
            break

               