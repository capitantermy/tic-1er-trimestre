# -*- coding: cp1252 -*-
def operaciones():
    print'Este programa sirve para sumar, restar, multiplicar o dividir'
    print'Escribe los numeros con los que quieres calcular '
    a=input('Primer número: ')
    z=input('Segundo numero: ')
    print 'Ahora escribe:'
    print's para sumar'
    s=a+z
    print'r para restar'
    r=a-z
    print'm para multiplicar'
    m=a*z
    print'd para dividir'
    d=a/z
    repetir=True
    while(repetir==True):
        q=input ('operación a realizar: ')
        if (q==s or q==r or q==m or q==d):
            repetir=False
            if(q==s):
                print s
            if(q==r):
                print r
            if(q==m):
               print m
            if(q==d):
                print d  
        else:
            repetir=True
    

   
        
    

operaciones()
