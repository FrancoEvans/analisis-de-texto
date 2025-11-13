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
            print(f'La ruta "{ruta}" fue eliminada')
    else: 
        print('La ruta para eliminar no se encontro')
        return
    
def mostrar_opciones_rutas(rutas):
    print('\nRUTAS:')
    print('0) Agregar nueva')
    print('1) Eliminar ruta')
    for i, ruta in enumerate(rutas, start=2):
        print(f'{i}) {ruta}')

def elegir_ruta():
    rutas = lista_de_rutas()
    mostrar_opciones_rutas(rutas)

    while True:
        try:
            ruta_elegida = int(input('ingrese el numero de una ruta: '))

            if ruta_elegida == 0: 
                agregar_ruta(input('ingrese una ruta para agregar: '))
                rutas = lista_de_rutas()
                mostrar_opciones_rutas(rutas)
                continue

            if ruta_elegida == 1:
                eliminar_ruta(input('ingrese una ruta para eliminar: '))
                rutas = lista_de_rutas()
                mostrar_opciones_rutas(rutas)
                continue

            if 2 <= ruta_elegida <= len(rutas) + 1:
                return rutas[ruta_elegida - 2]

            print("numero fuera de rango. ingrese de nuevo")

        except ValueError:
            print("caracter invalido, ingrese de nuevo")

def elegir_varias_rutas():
    rutas = []

    while True:
        ruta = elegir_ruta()
        if ruta:
            rutas.append(ruta)
            print(f"ruta agregada: {ruta}")
        else:
            print("no se seleccionó ninguna ruta")

        seguir = input("\nseleccionar mas rutas? (s/n): ").strip().lower()
        if seguir != "s":
            break

    print("\nrutas seleccionadas:")
    for i, r in enumerate(rutas, start=1):
        print(f"{i}) {r}")

    return rutas


