def dias_de_la_semana():
    print 'Escribe un n�mero del 1 al 7' 
    print 'para saber a que dia de la semana corresponde'
    repetir=True
    while (repetir==True):
        dia=input('Pon el n�mero de d�a:')
        repetir = (dia<0) or (dia>7)
        if (repetir==True):
            print 'Repetir n�mero'
    if(dia==1):
        print'lunes'
    if(dia==2):
        print'martes'
    if(dia==3):
        print'mi�rcoles'
    if(dia==4):
        print'jueves'
    if(dia==5):
        print'viernes'
    if(dia==6):
        print's�bado'
    if(dia==7):
        print'domingo'
dias_de_la_semana()
   
