def celsius_a_fahrenheit(Celsius):
    return (Celsius*9/5) +32
def fahrenheit_a_celsius(fahrenheit):
    return (fahrenheit-32) *5/9
def celsius_a_kevin(Celsius):
    return Celsius+273.15
def kevin_a_celsius(Kevin):
    return Kevin-273.15
def metros_a_km(metros):
    return metros/1000
def km_a_metros(km):
    return km*1000
def metros_a_millas(metros):
    return metros * 0.000621371
def millas_a_metros(millas):
    return millas /0.000621371
def kg_a_libras(kg):
    return kg * 2.20462
def libras_a_kg(libras):
    return libras/2.20462
def gramos_a_onzas(gramos):
    return gramos * 0.035274
def onzas_a_gramos(onzas):
    return onzas/0.035274

respuesta_usuario = 0

while  respuesta_usuario != 14:
    print("       ---CONVERSOR---")
    print("TEMPERATURA")
    print("1. Grados Celsius a Grados Fahrenheit")
    print("2. Grados Fahrenheit a Grados Celsius")
    print("3. Grados Celsius a Grados Kevin")
    print("4. Grados Kevin a Grados Celsius")
    print("DISTANCIA")
    print("5. Metros a Kilometros")
    print("6. Kilometros a Metros")
    print("7. Metros a Millas")
    print("8. Millas a Metros")
    print("PESO")
    print("9. Kilogramos a Libras")
    print("10. Libras a Kilogramos")
    print("11. Gramos a Onzas")
    print("12. Onzas a Gramos")
    print("EXTRAS")
    print("13. SALIR")
    
    respuesta_usuario = int(input("Selecciona una opción: "))
    if respuesta_usuario == 1:
        Celsius = float(input("Grados celsius: "))
        fahrenheit = celsius_a_fahrenheit(Celsius)
        print(f"{Celsius} Cº son {fahrenheit} Fº")
        input("presiona enter para volver al menú")
    elif respuesta_usuario == 2:
        fahrenheit = float(input("Grados fahrenheit: "))
        Celsius = fahrenheit_a_celsius(fahrenheit)
        print(f"{fahrenheit} Fº son {Celsius} Cº")
        input("presiona enter para volver al menú")
    elif respuesta_usuario == 3:
        Celsius = float(input("Grados celsius: "))
        Kevin = celsius_a_kevin(Celsius)
        print(f"{Celsius} Cº son {Kevin} Kº")
        input("presiona enter para volver al menú")
    elif respuesta_usuario == 4:
        Kevin = float(input("Grados Kevin: "))
        Celsius = kevin_a_celsius(Kevin)
        print(f"{Celsius} Cº son {Kevin} Kº")
        input("presiona enter para volver al menú")
    elif respuesta_usuario == 5:
        metros = float(input("Metros: "))
        km = metros_a_km(metros)
        print(f"{metros} Metros son {km} KIlometros")
        input("presiona enter para volver al menú")
    elif respuesta_usuario == 6:
        km = float(input("Kilometros: "))
        metros = km_a_metros(km)
        print(f"{km} Kilometros son {metros} Metros")
        input("presiona enter para volver al menú")
    elif respuesta_usuario == 7:
        metros = float(input("Metros: "))
        millas = metros_a_millas(metros)
        print(f"{metros} Metros son {millas} Millas")
        input("presiona enter para volver al menú")
    elif respuesta_usuario == 8:
        millas = float(input("Millas: "))
        metros = millas_a_metros(millas)
        print(f"{millas} Millas son {metros} Metros")
        input("presiona enter para volver al menú")
    elif respuesta_usuario == 9:
        kg = float(input("Kilogramos: "))
        libras = kg_a_libras(kg)
        print(f"{kg} Kilogramos son {libras} Libras")
        input("presiona entter para volver al menú")
    elif respuesta_usuario == 10:
        libras = float(input("Libras: "))
        kg = libras_a_kg(libras)
        print(f"{libras} Libras son {kg} Kilogramos")
        input("presiona enter para volver al menú")
    elif respuesta_usuario == 11:
        gramos = float(input("Gramos: "))
        onzas = gramos_a_onzas(gramos)
        print(f"{gramos} Gramos son {onzas} Onzas")
        input("presiona enter para volver al menú")
    elif respuesta_usuario == 12:
        onzas = float(input("Onzas: "))
        gramos = onzas_a_gramos(onzas)
        print(f"{onzas} Onzas son {gramos} Gramos")
        input("presiona enter para volver al menú")
    elif respuesta_usuario == 13:
        print("HASTA LA PRÓXIMA")
        exit()
    else:
        print("OPCIÓN NO VÁLIDA. INTENTA DE NUEVO")
    print("\n")