"""
Se ingresa el día y mes del presente año, determinar:
    1. El día de la semana de la fecha
    2. La cantidad de días para finalizar el año
"""

"""
Recursos:
http://exponentis.es/programa-en-python-para-calcular-el-numero-de-dias-entre-dos-fechas
"""

# FUNCIONES
# Determinamos si es año bisiesto
def esBisiesto(year):
    return year % 4 == 0 and year % 100 != 0 or year % 400 == 0

# Determinamos cantidad de dias entre dos fechas
def diasHastaFecha(day1, month1, year1, day2, month2, year2):
    # Si estamos en el mismo año
    if (year1 == year2):
        if esBisiesto(year1) == False:
            diasMes = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        else:
            diasMes = [0, 31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

        llevaYear = 0
        total = 0
        i = month1

        if i < month2:
            while i < month2:
                llevaYear = llevaYear + diasMes[i]
                i = i + 1
            total = day2 + llevaYear - 1
            return total
        else:
            total = day2 - day1
            return total
    else:
        return False

# LISTA CON DIAS DE LA SEMANA
lista_semana = ['Lunes', 'Martes', 'Miercoles', 'Jueves', 'Viernes', 'Sabado', 'Domingo']

# OBTENEMOS DIA Y MES EN FORMATO DD Y MM
print("\n---- Ingrese dia (dd) y mes (mm) del presente año ----\n")
dia  = int(input('Dia: '))
mes  = int(input('Mes: '))
anio = 2022;

# OBTENEMOS FECHA
import datetime
fecha = datetime.date(anio, mes, dia)
print("\n- La fecha es: " + str(fecha))

# OBTENEMOS DIA DE LA SEMANA DE LA FECHA
dia_semana = fecha.isoweekday()
print("- El dia de la semana es: " + str(lista_semana[dia_semana-1]))

# OBTENEMOS CANTIDAD DE DIAS PARA FINALIZAR EL AÑO
dias_anio = diasHastaFecha(1, 1, 2022, 31, 12, 2022)
dias_fecha = diasHastaFecha(1, 1, 2022, dia, mes, anio)
dias_finalizar = dias_anio - dias_fecha
print("- La cantidad de dias para finalizar el año es es: " + str(dias_finalizar))
