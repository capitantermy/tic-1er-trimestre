#en este programa le pedimos al usuario
#que introduzca los coeficientes de un polinomio
#y hallamos el valor de las raices
import math
def ecuacion():
    print 'introduzca los coeficientes del polinomio'
    print 'A*x^2+B*x+C=0'
    a=input('A=')
    b=input('B=')
    c=input('C=')
    radicando=(b*b)+(-4*a*c)
    print radicando
    if (radicando>0):
        raiz1=(-b+math.sqrt(radicando))/(2*a)
        raiz2=(-b-math.sqrt(radicando))/(2*a)
        print 'primera solucion '
        print raiz1
        print 'segunda solucion '
        print raiz2
    else:
        print 'no tiene solución real'
ecuacion()
