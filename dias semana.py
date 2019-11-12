def dias_de_la_semana():
    print 'Escribe un número del 1 al 7' 
    print 'para saber a que dia de la semana corresponde'
    repetir=True
    while (repetir==True):
        dia=input('Pon el número de día:')
        repetir = (dia<0) or (dia>7)
        if (repetir==True):
            print 'Repetir número'
    if(dia==1):
        print'lunes'
    if(dia==2):
        print'martes'
    if(dia==3):
        print'miércoles'
    if(dia==4):
        print'jueves'
    if(dia==5):
        print'viernes'
    if(dia==6):
        print'sábado'
    if(dia==7):
        print'domingo'
dias_de_la_semana()
   
