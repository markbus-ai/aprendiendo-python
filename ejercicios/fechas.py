"""
/*
 * EJERCICIO:
 * Crea dos variables utilizando los objetos fecha (date, o semejante) de tu lenguaje:
 * - Una primera que represente la fecha (día, mes, año, hora, minuto, segundo) actual.
 * - Una segunda que represente tu fecha de nacimiento (te puedes inventar la hora).
 * Calcula cuántos años han transcurrido entre ambas fechas.
 *
 * DIFICULTAD EXTRA (opcional):
 * Utilizando la fecha de tu cumpleaños, formatéala y muestra su resultado de
 * 10 maneras diferentes. Por ejemplo:
 * - Día, mes y año.
 * - Hora, minuto y segundo.
 * - Día de año.
 * - Día de la semana.
 * - Nombre del mes.
 * (lo que se te ocurra...)
 */
"""
from datetime import datetime, timedelta

fecha_actual = datetime.now()

fecha_nacimiento = datetime(2005, 12, 19, 21)

tiempo_trans = fecha_actual - fecha_nacimiento

dias_pasados = tiempo_trans.days
años_pasados = dias_pasados / 365
aux_dias = dias_pasados % 365

print(f"ha pasado {años_pasados:.0f} años y {aux_dias:.0f} dias desde mi nacimiento\n")



"""
extra
"""

fecha_formateada1 = fecha_actual.strftime("%m/%y/%d")
fecha_formateada2 = fecha_actual.strftime("%m/%d/%y")
fecha_formateada3 = fecha_actual.strftime("%d/%y/%m")
fecha_formateada4 = fecha_actual.strftime("%d/%m/%Y")
fecha_formateada5 = fecha_actual.strftime("%y/%d/%m")
fecha_formateada6 = fecha_actual.strftime("%y/%m/%d")
fecha_formateada7 = fecha_actual.strftime("%y/%d")
fecha_formateada8 = fecha_actual.strftime("%m/%y")
fecha_formateada9 = fecha_actual.strftime("%d/%m")
fecha_formateada10 = fecha_actual.strftime("%d/%y")

print(f"{fecha_formateada1}\n")
print(f"{fecha_formateada2}\n")
print(f"{fecha_formateada3}\n")
print(f"{fecha_formateada4}\n")
print(f"{fecha_formateada5}\n")
print(f"{fecha_formateada6}\n")
print(f"{fecha_formateada7}\n")
print(f"{fecha_formateada8}\n")
print(f"{fecha_formateada9}\n")
print(f"{fecha_formateada10}\n")