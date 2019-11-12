# -*- coding: cp1252 -*-
def fecha():
    print 'Escribe un día del mes '
    rep=True
    while (rep==True):
        dia=input('Escribe el día: ')
        rep = (dia<1) or (dia>31)
        if (rep==True):
            print'Día no válido'
    print 'Escribe un mes del año'
    repe=True
    while (repe==True):
        mes=input('Escribe el mes: ')
        repe = (mes<1)or(mes>12)
        if(repe==True):
            print'Mes no válido'
    ao =input('Escribe el año')
    if(mes==1):
        print dia,' de enero de ',ao
    if(mes==2):
        print dia,' de febrero de ',ao
    if(mes==3):
        print dia,' de marzo de ',ao
    if(mes==4):
        print dia,' de abril de ',ao
    if(mes==5):
        print dia,' de mayo de ',ao
    if(mes==6):
        print dia,' de junio de ',ao
    if(mes==7):
        print dia,' de julio de ',ao
    if(mes==8):
        print dia,' de agosto de ',ao
    if(mes==9):
        print dia,' de septiembre de ',ao
    if(mes==10):
        print dia,' de octubre de ',ao
    if(mes==11):
        print dia,' de noviembre de ',ao
    if(mes==12):
        print dia,' de diciembre de ',ao  

fecha()
