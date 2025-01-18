import logging
from sections.buscadorMascotas.application.buscadorMascotasUseCase import BuscadorMascotasUseCase
from sections.buscadorProtectoras.application.buscarorProtectorasUseCase import BuscadorProtectorasUseCase
from shared.helpers.loggingHelper import LogginHelper

BUSCARPROTECTORAS = True
BUSCARMASCOTAS = False


class main:
    def __init__(self):
        LogginHelper()
        logging.debug("main initialized")
        self.bp = BuscadorProtectorasUseCase()
        self.bm = BuscadorMascotasUseCase()



if __name__ == "__main__":
    main = main()
    if BUSCARPROTECTORAS:
        main.bp.execute()
    if BUSCARMASCOTAS:
        main.bm.execute()

