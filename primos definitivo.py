def primos():
    n=input('¿Desde que número?: ')
    nmax = input('¿hasta que numero?: ')
    primo=True
    for x in range(n, nmax):
        print x
        for i in range(2, x):
            if x%i == 0:
                primo=False
        if(primo==True):
            print "primo"
        else:
            print "no es primo"
        primo=True

primos()
