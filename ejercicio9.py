def ejercicio9():
    print 'dinero que te pagan por trabajar'
    a=input("numero de horas trabajadas en la semana=")
    if a<=40:
        print a*30,"euros"
    if a>40:
        print ((a-40)*45),"euros,por las horas extra"
        print ((a-1)*30),"euros por las horas no extra"
ejercicio9()
