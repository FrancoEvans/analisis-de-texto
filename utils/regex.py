import re
from .metricas import (
    info_basica_texto,
    palabra_mas_larga,
    frecuencia_palabras,
    calcular_densidad_lexica,
    distribucion_longitudes
)
from .text_utils import crear_lista_palabras




# una función para buscar palabra LISTO

# otra para buscar patrón regex genérico (recibe patrón y texto, devuelve matches).


RE_MAIL = re.compile(r'[a-zA-Z0-9-_.]+@\w+\.\w+')
RE_DATE = re.compile(r'\d{2,4}[/-]\d{2}[/-]\d{2,4}')
RE_TIME = re.compile(r'\b\d{1,2}[:]\d{2}\b')
RE_TILDES = re.compile(r'\b[A-Za-záéíóúÁÉÍÓÚñÑ]*[áéíóúÁÉÍÓÚ]+[A-Za-záéíóúÁÉÍÓÚñÑ]*\b')
RE_URL = re.compile(r'''
    (https?) :// #esquema
    ([A-Za-z0-9-]+(?:\.[A-Za-z0-9-]+)+) #dominio
    (:\d+)? #puerto (opcional)
    (/[^\s?#]*)? #ruta (opcional)
    (\?[^\s#]*)? #query args (opcional)
    (\#[^\s]*)? #seccion (opcional)
''', re.VERBOSE)


with open('data/texto_prueba4.txt', 'r', encoding='utf-8') as f:
    txt = f.read().strip()

print(re.findall('[a-zA-Z0-9-_.]+@\w+\.\w+', txt))


def buscar_palabra(palabra, txt):
    patron = re.compile(rf'\b{re.escape(palabra)}\b', re.IGNORECASE)
    
    resultados = re.findall(patron, txt)

    return resultados

