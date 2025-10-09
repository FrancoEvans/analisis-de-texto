import re

texto1 = "El correo de contacto es juan.perez123@gmail.com y también figura otro: info@empresa.org"

texto2 = "La reunión fue el 21/07/2025 en Buenos Aires. Otra fecha posible es 2025-08-15."

texto3 = "El número de teléfono principal es +54 9 11 2345-6789, el alternativo 011-4321-8765."

texto4 = "El código postal es 1425, y la dirección es Av. Corrientes 1234, CABA."

texto5 = "La tarjeta de crédito terminaba en 4567 y el DNI era 12.345.678."


# texto1: buscá todas las direcciones de email.
# texto2: encontrá todas las fechas
# texto3: buscá todos los números de teléfono.
# texto4: extraé el código postal y la dirección (separados).
# texto5: encontrá el número de tarjeta (4 dígitos) y el DNI completo.



# 1 (MAIL)

print(re.findall('[a-zA-Z0-9-_.]+@\w+\.\w+', texto1))

# [a-zA-Z0-9_.-] => conjunto personalizado con un + para que tome 1 o mas caracteres
# @ divide el dominio de la direccion
# \w+\.\w+ una palabra completa, un punto y otra palabra completa (gmail.com / edu.ar)


# 2 (FECHA)

print(re.findall('\d{2,4}[/-]\d{2}[/-]\d{2,4}', texto2))

# \d{2,4} digitos (entre 2 y 4)
# [/-] UNA barra o guion
# \d{2} digitos (2)


# 