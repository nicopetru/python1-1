calculo = input('Mencione un mes del año:')
meses_verano = ['Enero', 'Febrero', 'Marzo']
meses_invierno = ['Junio', 'Julio', 'Agosto']
meses_otoño = ['Abril', 'Mayo', 'Junio']
meses_primavera = ['Septiembre', 'Octurbre', 'Noviembre']
estacion = ' '
if calculo in meses_verano:
 estacion ="Verano"
elif calculo in meses_primavera:
 estacion ="Primavera"
elif calculo in meses_otoño:
 estacion="otoño"
elif calculo in meses_invierno:
 estacion="invierno"
else:
 estacion=' No es un mes del año, por favor elige un mes del año'
print(f'Estamos en la estacion de: {estacion}')

