from error import DimensionError

class Foto():
    """
    Clase que representa una foto con dimensiones específicas y una ruta asociada.
 
    """
    MAX = 2500

    def __init__(self, ancho: int, alto: int, ruta: str) -> None:
        """
        Inicializa una instancia de la clase Foto.

        Parámetros:
            ancho: int, El ancho de la foto.
            alto: int, El alto de la foto.
            ruta: str, La ruta de la foto.
        """
        self.__ancho = None
        self.__alto = None
        self.ancho = ancho
        self.alto = alto
        ruta = ruta

    @property
    def ancho(self) -> int:
        """
        Obtiene el ancho de la foto.

        Retorna:
            int: El ancho de la foto.
        """
        return self.__ancho

    @ancho.setter
    def ancho(self, ancho) -> None:
        """
        Establece el ancho de la foto.

        Valida que el ancho esté dentro del rango permitido (1 a MAX). Si el valor es inválido, se lanza una excepción DimensionError.

        Parámetros:
            ancho: int, El nuevo ancho de la foto.

        Lanza:
            DimensionError: Si el ancho está fuera del rango permitido.
        """
        if ancho < 1 or ancho > Foto.MAX:
            raise DimensionError("Valor de ancho es invalido", dimension = ancho, maximo = Foto.MAX)
        self.__ancho = ancho

    @property
    def alto(self) -> int:
        """
        Obtiene el alto de la foto.

        Retorna:
            int: El alto de la foto.
        """
        return self.__alto

    @alto.setter
    def alto(self, alto) -> None:
        """
        Establece el alto de la foto.

        Valida que el alto esté dentro del rango permitido (1 a MAX). Si el valor es inválido, se lanza una excepción DimensionError.

        Parámetros:
            alto: int, El nuevo alto de la foto.

        Lanza:
            DimensionError: Si el alto está fuera del rango permitido.
        """
        if alto < 1 or alto > Foto.MAX:
            raise DimensionError("Valor de alto es invalido", dimension = alto, maximo = Foto.MAX)
        self.__alto = alto