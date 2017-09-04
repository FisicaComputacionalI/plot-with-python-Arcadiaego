import numpy as np
import pylab as pl
# crea un vector (arreglo) con los valores del eje X
x = [ 1990, 1991, 1992, 1993, 1994, 1995, 1996, 1997, 1997, 1999, 2000, 2001, 2002, 2003, 2004, 2005, 2006, 2007, 2008, 2009, 2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017]
# crea un vector (arreglo) con los valores del eje Y para cada valor en el eje x
y = [ 0, 1, 1, 1, 1, 1, 1, 2, 2, 3, 4, 6, 3, 7, 4, 3, 2, 1, 4, 4, 4, 4, 4, 3, 2, 2, 4, 4]
# Dar nombre a los ejes
pl.ylabel('novias y mascotas')
pl.xlabel('anios de vida')
# Colocamos los rangos
pl.axis([0,30, 0,10])
# Grafica el vector x contra el vector y
pl.plot(x, y, 'cH')
#Guardar la grafica en formato png
pl.savefig('temp1.png')
#mostrar 
pl.show()
