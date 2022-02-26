import numpy as np 
import math as mt
#Cálculo de la presión atmosférica con la altura sobre el nivel del mar#
#La fórmula usada es: Patm=Po*e^(a*h)
# Donde: 
# Po: Presión atmosférica al nivel del mar (Pa) 
# h: Altura a la que se quiere calcular la presión atmosférica (m)
# d: densidad del aire en condiciones normales (Kg/m^3)
# g: valor de la gravedad (m/s^2)
print('Vamos a calcular la presión atmosférica a una altura sobre el nivel del mar que tu desees.')
d=1.24
g=9.81
Po=101325
a=((d*g)/Po)*-1
h=float(input('Introduce la altura sobre el nivel del mar de tu interés(en metros):'))
e=2.718281828
Patm=Po*(e**(a*h))
print('La presión atmosférica a',h,'metros sobre el nivel del mar es:')
print(Patm,'Pa.')
