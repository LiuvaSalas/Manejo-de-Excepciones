from error import DimesionError

class Foto():
    MAX = 2500

    def __init__(self, ancho: int, alto: int, ruta: str) -> None:
        self.__ancho = ancho
        self.__alto = alto
        self.__ancho = None
        self.__alto = None
        ruta = ruta

    @property
    def ancho(self) -> int:
        return self.__ancho

    @ancho.setter
    def ancho(self, ancho) -> None:
        if ancho < 1 or ancho > Foto.MAX:
            raise DimesionError("Valor de ancho no valido", dimension = ancho, maximo = Foto.MAX)
        self.__ancho = ancho

    @property
    def alto(self) -> int:
        return self.__alto

    @alto.setter
    def alto(self, alto) -> None:
        if alto < 1 or alto > Foto.MAX:
            raise DimesionError("Valor de alto no valido", dimension = alto, maximo = Foto.MAX)
        self.__alto = alto