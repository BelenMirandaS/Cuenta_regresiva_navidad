from datetime import datetime

def tiempo_para_navidad():
    ahora = datetime.now()
    año_actual = ahora.year

# Navidad es el 25 de diciembre a las 00:00
    navidad = datetime(año_actual, 12, 25)

# Si ya pasó navidad, se calcula con respecto al otro año
    if ahora > navidad:
        navidad = datetime (año_actual + 1, 12, 25)
    diferencia = navidad - ahora

# Total de dias completos
    dias = diferencia.days

# El resto (que no sean días) en segundos
    segundos_restantes = diferencia.seconds
    horas = segundos_restantes // 3600
    minutos = (segundos_restantes % 3600) // 60
    segundos = segundos_restantes % 60

    return dias, horas, minutos, segundos

# Dibujo de árbol
def mostrar_arbol():
    ramas = r"""
             *
            ***
          *******
        ***********
      ***************
    *******************
    """.rstrip()
    tronco = r"""
           |||||
           |||||
    """.lstrip("\n")
    # Ramas verdes
    print("\033[32m" + ramas + "\033[0m")
    # Tronco café
    print("\033[38;5;94m" + tronco + "\033[0m")

def main():
    print("¡Cuenta regresiva para Navidad! 🎄🎁✨")
    mostrar_arbol()
    input("Presiona Enter para saber cuánto tiempo falta...")

    dias, horas, minutos, segundos = tiempo_para_navidad()
    print(f"Faltan {dias} días, {horas} horas, {minutos} minutos y {segundos} segundos para Navidad.")
    print("¡Queda menos! 🎄🎁✨")

if __name__ == "__main__":
    main()