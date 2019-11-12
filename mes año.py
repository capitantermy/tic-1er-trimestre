# -*- coding: cp1252 -*-
def mes_del_ao():
    print 'Escribe un número del 1 al 2' 
    print 'para saber a que mes del año corresponde'
    repetir=True
    while (repetir==True):
        mes=input('Pon el número de mes:')
        repetir = (mes<1) or (mes>12)
        if (repetir==True):
            print 'Repetir número'
    if(mes==1):
        print'enero'
    if(mes==2):
        print'febrero'
    if(mes==3):
        print'marzo'
    if(mes==4):
        print'abril'
    if(mes==5):
        print'mayo'
    if(mes==6):
        print'junio'
    if(mes==7):
        print'julio'
    if(mes==8):
        print'agosto'
    if(mes==9):
        print'septiembre'
    if(mes==10):
        print'octubre'
    if(mes==11):
        print'noviembre'
    if(mes==12):
        print'diciembre'   
mes_del_ao()
