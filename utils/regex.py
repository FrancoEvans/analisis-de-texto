import re
from .metricas import (
    info_basica_texto,
    palabra_mas_larga,
    frecuencia_palabras,
    calcular_densidad_lexica,
    distribucion_longitudes
)
from .text_utils import crear_lista_palabras




import re

# patrones predefinidos
RE_MAIL = r'[a-zA-Z0-9-_.]+@\w+\.\w+'
RE_DATE = r'\d{2,4}[/-]\d{2}[/-]\d{2,4}'
RE_TIME = r'\b\d{1,2}[:]\d{2}\b'
RE_TILDES = r'\b[A-Za-záéíóúÁÉÍÓÚñÑ]*[áéíóúÁÉÍÓÚ]+[A-Za-záéíóúÁÉÍÓÚñÑ]*\b'
RE_URL = r'(https?://[^\s]+)'


def buscar_regex(txt):
    print('''
Menu de busqueda
1) Buscar palabra
2) Buscar patron (mails, fechas, horas, tildes o urls)
0) Volver
''')

    while True:
        try:
            opcion = int(input('Elija una opcion: '))
            break
        except ValueError:
            print('Ingrese un numero valido')

    if opcion == 0:
        return

    if opcion == 1:
        palabra = input('Ingrese palabra: ').strip()
        patron = re.compile(rf'\b{re.escape(palabra)}\b', re.IGNORECASE)
        resultados = re.findall(patron, txt)
        print(f"La palabra '{palabra}' aparece {len(resultados)} veces")
        if resultados:
            print('Coincidencias:', resultados)
        return

   
    if opcion == 2:
        print('''
Elija el tipo de patron
1) Mails
2) Fechas
3) Horas
4) Tildes
5) Urls
0) volver
''')

        try:
            tipo = int(input('Elija una opcion: '))
        except ValueError:
            print('Ingrese un numero valido')
            return

        if tipo == 0:
            return

        if tipo == 1:
            patron = RE_MAIL
        elif tipo == 2:
            patron = RE_DATE
        elif tipo == 3:
            patron = RE_TIME
        elif tipo == 4:
            patron = RE_TILDES
        elif tipo == 5:
            patron = RE_URL
        else:
            print('Opcion invalida')
            return

        resultados = re.findall(patron, txt)
        print(f"se encontraron {len(resultados)} coincidencias")
        if resultados:
            for r in resultados:
                print('-', r)
