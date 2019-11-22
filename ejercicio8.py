def ejercicio8():
    a=input("escriba el precio")
    print'la tasa puede ser general, reducida y superreducida'
    b=raw_input("escriba la tasa ")
    if b=="general":
        print a*1.16
    if b=="reducida":
        print a*1.07
    if b=="superreducida":
        print a*1.04
ejercicio8()
