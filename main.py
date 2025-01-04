import logging
import json
import requests
import re
from bs4 import BeautifulSoup
from shared.helpers.loggingHelper import LogginHelper
from sections.buscadorProtectoras.model.Protectora import Protectora

class main:
    def __init__(self):
        self.porComunidad = None

        LogginHelper()
        self.cargarDatos()
        logging.debug("main initialized")


    def cargarDatos(self):
        logging.debug("cargarDatos() called")
        with open(r"resources\porComunidad.json", encoding="utf-8") as file:
            self.porComunidad = json.load(file)



    def abrirPorComunidad(self):
        logging.debug("abrirPorComunidad() called")
        map_protectoras = {}
        rutaBase = self.porComunidad["link"]
        for comunidad in self.porComunidad["links"]:
            list_comunidades = []
            ruta =rutaBase + self.porComunidad["links"][comunidad]
            llamada = requests.get(ruta, timeout=5)
            soup = BeautifulSoup(llamada.text, 'html.parser')
            nodos = soup.select("section.backgroundcolor-white:first-child div.uk-section-small ul.uk-list li")
            for li in nodos:
                protectora = Protectora()
                protectora.name = li.select("b")[0].text
                self.ordenar_links(li.select("a"), protectora) # ordenar los links
                protectora.comunidad_autonoma = comunidad
                list_comunidades.append(protectora)
            # Convertir objeto a diccionario
            dict_list = [model.dict() for model in list_comunidades]
            map_protectoras[comunidad] = dict_list

        return map_protectoras
    
    def ordenar_links(self, links, protectora: Protectora):
        for link in links:
            if re.match(r".+@.+\..+", link.text):
                protectora.mailto = link.text.split("/")[0].strip()
            elif re.match(r"[\d ]+", link.text):
                protectora.phone = link.text
            elif re.match   (r"www\..+\..+", link.text):
                protectora.web = link.text
    
    def escribirFichero(self, map_protectoras):
        logging.debug("escribirFichero() called")
        with open(r"resources\protectoras.json", "w", encoding="utf-8") as file:
            json.dump(map_protectoras, file, ensure_ascii=False, indent=4)

if __name__ == "__main__":
    main = main()
    protectoras = main.abrirPorComunidad()
    main.escribirFichero(protectoras)

