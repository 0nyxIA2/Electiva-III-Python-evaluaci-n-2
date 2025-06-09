import random



print("""
╔══════════════════════════╗
║   T U R N   M A G I T    ║
║    Turn-Based Combat     ║
╚══════════════════════════╝
""")

# Clase base
class Personaje:
    def __init__(self, nombre, vida, ataque, defensa):
        self.nombre = nombre
        self.vida = vida
        self.ataque = ataque
        self.defensa = defensa

    def atacar(self, oponente):
        daño = max(self.ataque - oponente.defensa, 0)
        oponente.vida -= daño
        return daño

    def defender(self, atacante):
        reduccion = int(self.defensa * 1.5)
        daño = max(atacante.ataque - reduccion, 0)
        self.vida -= daño
        return daño

# Subclases específicas
class Guerrero(Personaje):
    def __init__(self):
        super().__init__(nombre="Guerrero", vida=100, ataque=20, defensa=10)

class Mago(Personaje):
    def __init__(self):
        super().__init__(nombre="Mago", vida=80, ataque=25, defensa=5)

class Arquero(Personaje):
    def __init__(self):
        super().__init__(nombre="Arquero", vida=90, ataque=18, defensa=8)

class Marguinado(Personaje):
    def __init__(self):
        super().__init__(nombre="Marguinado", vida=50, ataque=45, defensa=1)

# Lista de instancias
personajes = [Guerrero(), Mago(), Arquero(), Marguinado()]
acciones = ["atacar", "defender"]

def seleccionar_personaje():
    print("\nElige tu personaje:")
    for i, p in enumerate(personajes, start=1):
        print(f"{i}. {p.nombre}")
    while True:
        entrada = input("Ingresa el número del personaje: ")
        try:
            idx = int(entrada) - 1
            if 0 <= idx < len(personajes):
                return personajes[idx]
            else:
                print(f"Debes ingresar un número entre 1 y {len(personajes)}.")
        except ValueError:
            print("Entrada inválida. Ingresa un número entero.")

def combatir(jugador, oponente):
    turno = 1
    while jugador.vida > 0 and oponente.vida > 0:
        print(f"\n--- Turno {turno} ---")
        print(f"Tu vida: {jugador.vida} | Vida oponente: {oponente.vida}")
        print("1. Atacar")
        print("2. Defender")

        elec = input("Elige 1 o 2: ")
        while elec not in ("1", "2"):
            print("\nEntrada inválida. Debes ingresar 1 (Atacar) o 2 (Defender).")
            elec = input("Elige 1 o 2: ")

        accion_jugador = "atacar" if elec == "1" else "defender"
        print(f"\nHaz elegido: {accion_jugador}")

        accion_oponente = random.choice(acciones)
        print(f"El oponente decide: {accion_oponente}")

        # Resolver interacciones
        if accion_jugador == "atacar" and accion_oponente == "atacar":
            daño_recibido = jugador.atacar(oponente)  # jugador ataca primero por simetría
            daño_infligido = oponente.atacar(jugador)
            print(f"\nLe quitas al oponente: {daño_recibido}")
            print(f"El oponente te quito: {daño_infligido}")

        elif accion_jugador == "atacar" and accion_oponente == "defender":
            daño = jugador.atacar(oponente)
            print("\nNo recibes daños")
            print(f"Le quitas al oponente: {daño}")

        elif accion_jugador == "defender" and accion_oponente == "atacar":
            daño = jugador.defender(oponente)
            print(f"\nEl oponente te quito: {daño}")

        else:  # ambos defienden
            print("\nAmbos se defendieron. No hubo daño.")

        turno += 1

    # Resultado final
    print("\n--- Fin del combate ---")
    if jugador.vida <= 0 and oponente.vida <= 0:
        print("¡Empate! Ambos cayeron al mismo tiempo.")
    elif jugador.vida <= 0:
        print("¡Has perdido!")
    else:
        print("¡Has ganado!")

def main():
    while True:
        print("\n===== MENÚ PRINCIPAL =====")
        print("1. Jugar")
        print("2. Salir")
        opcion = input("Selecciona una opción (1 o 2): ")
        while opcion not in ("1", "2"):
            print("Entrada inválida. Debes ingresar 1 para Jugar o 2 para Salir.")
            opcion = input("Selecciona una opción (1 o 2): ")

        if opcion == "1":
            jugador = seleccionar_personaje()
            # Elegir oponente distinto
            oponente = random.choice(personajes)
            while oponente is jugador:
                oponente = random.choice(personajes)

            print(f"\nHas elegido: {jugador.nombre}")
            print(f"Tu oponente es: {oponente.nombre}")
            combatir(jugador, oponente)
        else:
            print("¡Gracias por jugar! Hasta la próxima.")
            break

if __name__ == "__main__":
    main()