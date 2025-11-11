import re
from .metricas import (
    info_basica_texto,
    palabra_mas_larga,
    frecuencia_palabras,
    calcular_densidad_lexica,
    distribucion_longitudes
)
from .text_utils import crear_lista_palabras


with open('data/texto_prueba4.txt', 'r', encoding='utf-8') as f:
    txt = f.read().strip()

print(re.findall('[a-zA-Z0-9-_.]+@\w+\.\w+', txt))


def buscar_palabra(palabra, txt):
    patron = re.compile(rf'\b{re.escape(palabra)}\b', re.IGNORECASE)
    
    resultados = re.findall(patron, txt)

    return resultados
