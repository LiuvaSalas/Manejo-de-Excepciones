class DimesionError(Exception):
    def __init__(self, mensaje: str, dimension: int, maximo: int):
        self.mensaje = mensaje
        self.dimension = dimension
        self.maximo = maximo
        super().__init__(mensaje)

    def __str__(self):
        if self.dimension == None or self.maximo == None:
            return super().__str__()
        else:
            return f"Mensaje: {self.mensaje} - Dimesion: {self.dimension} - Maximo: {self.maximo}"