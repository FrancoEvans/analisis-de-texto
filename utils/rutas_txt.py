from pathlib import Path

rutas_file = Path('data/textos/rutas.txt')


def lista_de_rutas():
    with open(rutas_file, "r", encoding="utf-8") as f:
        return f.read().splitlines()

def agregar_ruta(ruta):
    rutas = lista_de_rutas()
    ruta_archivo = Path(ruta)

    if ruta_archivo.exists():
        with open(rutas_file, "w", encoding="utf-8") as f:
            rutas.append(ruta)
            f.write("\n".join(rutas))
    else:
        print(f"no existe el archivo de la ruta {ruta}")

def eliminar_ruta(ruta):
    rutas = lista_de_rutas()
    if ruta in rutas:
        rutas.remove(ruta)
        with open(rutas_file, "w", encoding="utf-8") as f:
            f.write("\n".join(rutas))
    else: 
        print('la ruta para eliminar no se encontro')
        return

def elegir_ruta():
    rutas = lista_de_rutas()
    print("\nRUTAS:")
    print("0) Agregar nueva ruta")

    for i, ruta in enumerate(rutas, start=1):
        print(f'{i}) {ruta}')

    while True:
        try:
            ruta_elegida = int(input('ingrese el numero de una ruta: '))

            if ruta_elegida == 0: 
                agregar_ruta(input('ingrese una ruta para agregar: '))
                rutas = lista_de_rutas()
                continue

            if 1 <= ruta_elegida <= len(rutas):
                return rutas[ruta_elegida - 1]

            print("numero fuera de rango. ingrese de nuevo")

        except ValueError:
            print("caracter invalido, ingrese de nuevo")


# listo

