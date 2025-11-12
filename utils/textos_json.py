import json 

def seleccionar_textos(cantidad, minimo=2):
    if cantidad < minimo:
        print(f"Se necesitan al menos {minimo} textos, pero solo hay {cantidad}.")
        return []

    while True:
        try:
            entrada = input(f"Ingrese números de texto separados por coma (ej: 1,3,4) o 0 para todos: ")
            entrada = "".join(entrada.split())

            if entrada == "0":
                return list(range(cantidad))

            partes = entrada.split(",")
            indices = []

            for p in partes:
                n = int(p)
                if n < 1 or n > cantidad:
                    raise ValueError
                idx = n - 1
                if idx not in indices:
                    indices.append(idx)

            if len(indices) < minimo:
                print(f"Debe elegir al menos {minimo} textos.")
                continue

            return indices

        except ValueError:
            print("Entrada inválida. Intente de nuevo.")


def cargar_mas_textos(textos):
    print("\n==============================")
    print("      CARGAR MÁS TEXTOS")
    print("==============================")

    cantidad_inicial = len(textos)

    while True:
        try:
            txt = input("Ingrese un nuevo texto (o presione Enter para finalizar): ")
            if len(txt) > 10000:
                raise ValueError
            if txt.strip() == "":
                break
            textos.append(txt)
        except ValueError:
            print("El texto ingresado es demasiado largo. Intente con un texto más corto.")

    nuevos = len(textos) - cantidad_inicial

    if nuevos == 0:
        print("No se cargó ningún texto nuevo.")
    elif nuevos == 1:
        print("Se cargó 1 texto nuevo.")
    else:
        print(f"Se cargaron {nuevos} textos nuevos.")

    return textos

def guardar_resultados_json(resultados_todos):
    try:
        arch = open("resultados.json", "wt")
        json.dump(resultados_todos, arch)
        print("\nResultados guardados correctamente en 'resultados.json'.")
    except (FileNotFoundError, OSError) as error:
        print("ERROR DE GRABACION:", error)
    finally:
        try:
            arch.close()
        except NameError:
            pass
        
def guardar_textos_json(textos):
    try:
        arch = open("textos.json", "wt", encoding="utf-8")
        json.dump(textos, arch)
        print("\nTextos guardados correctamente en 'textos.json'.")
    except (FileNotFoundError, OSError) as error:
        print("ERROR DE GRABACION:", error)
    finally:
        try:
            arch.close()
        except NameError:
            pass

def cargar_textos_json():
    try:
        arch = open("textos.json", "rt", encoding="utf-8")
        textos = json.load(arch)
        print(f"\nSe cargaron {len(textos)} textos desde 'textos.json'.")
        return textos
    except (FileNotFoundError, OSError) as error:
        print("ERROR DE LECTURA:", error)
        return []
    finally:
        try:
            arch.close()
        except NameError:
            pass