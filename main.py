import logging
from sections.buscadorMascotas.application.buscadorMascotasUseCase import BuscadorMascotasUseCase
from sections.buscadorProtectoras.application.buscarorProtectorasUseCase import BuscadorProtectorasUseCase
from shared.helpers.loggingHelper import LogginHelper

BUSCARPROTECTORAS = 0
BUSCARMASCOTAS = 1


class main:
    def __init__(self):
        LogginHelper()
        logging.debug("main initialized")
        self.bp = BuscadorProtectorasUseCase()
        self.bm = BuscadorMascotasUseCase()



if __name__ == "__main__":
    main = main()
    if BUSCARPROTECTORAS == 1:
        main.bp.execute()
    if BUSCARMASCOTAS == 1:
        main.bm.execute()

