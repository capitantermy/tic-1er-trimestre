def piramide():
    filas= input('Dime la altura de la piramide: ')
    espacios=' '
    asteriscos='*'
    for i in range(filas):
        for nespacios in range(1,filas-i):
            espacios=espacios+' '
        for nasteriscos in range(-1,2*i-1):
            asteriscos=asteriscos+'*'
        #Escribe de golpe toda la fila
        print espacios + asteriscos
        espacios=' '
        asteriscos='*'
piramide()
