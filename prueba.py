from error import DimensionError
from foto import Foto

def main():
    """
    Esta es la funcion principal que ejecuta las clases y metodos anidados entre si.
    """
    consultar = True
    while consultar:
        try:
            ancho = int(input("Ingresa el ancho de la foto:\n>"))
            alto = int(input("Ingresa el alto de la foto:\n>"))
            ruta = input("Ingresa la ruta:\n>")
            prueba_foto = Foto(ancho, alto, ruta)
            consultar = False
        except DimensionError as e:
            print(f"ERROR: {e}")

    print("Valores de la foto valida!")

if __name__ == "__main__":
    main()