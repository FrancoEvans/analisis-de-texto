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
menu de busqueda
1) buscar palabra
2) buscar patron (mails, fechas, horas, tildes o urls)
0) volver
''')

    while True:
        try:
            opcion = int(input('elige una opcion: '))
            break
        except ValueError:
            print('ingresa un numero valido')

    if opcion == 0:
        return

    if opcion == 1:
        palabra = input('ingresa palabra: ').strip()
        patron = re.compile(rf'\b{re.escape(palabra)}\b', re.IGNORECASE)
        resultados = re.findall(patron, txt)
        print(f"la palabra '{palabra}' aparece {len(resultados)} veces")
        if resultados:
            print('coincidencias:', resultados)
        return

   
    if opcion == 2:
        print('''
elige el tipo de patron
1) mails
2) fechas
3) horas
4) tildes
5) urls
0) volver
''')

        try:
            tipo = int(input('elige una opcion: '))
        except ValueError:
            print('ingresa un numero valido')
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
            print('opcion invalida')
            return

        resultados = re.findall(patron, txt)
        print(f"se encontraron {len(resultados)} coincidencias")
        if resultados:
            for r in resultados:
                print('-', r)
