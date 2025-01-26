class Conductor:
    def __init__(self, nombre, id_conductor):
        self.nombre = nombre
        self.id_conductor = id_conductor
        self.horarios = []  

    def asignar_horario(self, horario):
        if horario in self.horarios:
            return False
        self.horarios.append(horario)
        return True


class Bus:
    def __init__(self, id_bus):
        self.id_bus = id_bus
        self.ruta = None
        self.horarios = []  
        self.conductores_asignados = {}  

    def asignar_ruta(self, ruta):
        self.ruta = ruta

    def registrar_horario(self, horario):
        if horario not in self.horarios:
            self.horarios.append(horario)

    def asignar_conductor(self, horario, conductor):
        if horario not in self.horarios:
            return f"El horario {horario} no está registrado para este bus."
        if horario in self.conductores_asignados:
            return f"El horario {horario} ya tiene un conductor asignado."
        if not conductor.asignar_horario(horario):
            return f"El conductor {conductor.nombre} ya está asignado en el horario {horario}."
        self.conductores_asignados[horario] = conductor
        return f"Conductor {conductor.nombre} asignado al bus {self.id_bus} en el horario {horario}."


class Admin:
    def __init__(self):
        self.buses = []
        self.conductores = []

    def agregar_bus(self, id_bus):
        if any(bus.id_bus == id_bus for bus in self.buses):
            return f"El bus con ID {id_bus} ya existe."
        self.buses.append(Bus(id_bus))
        return f"Bus con ID {id_bus} agregado exitosamente."

    def agregar_conductor(self, nombre, id_conductor):
        if any(conductor.id_conductor == id_conductor for conductor in self.conductores):
            return f"El conductor con ID {id_conductor} ya existe."
        self.conductores.append(Conductor(nombre, id_conductor))
        return f"Conductor {nombre} con ID {id_conductor} agregado exitosamente."

    def obtener_bus(self, id_bus):
        for bus in self.buses:
            if bus.id_bus == id_bus:
                return bus
        return None

    def obtener_conductor(self, id_conductor):
        for conductor in self.conductores:
            if conductor.id_conductor == id_conductor:
                return conductor
        return None

    def mostrar_menu(self):
        while True:
            print("\nGestión de Tickets de Buses")
            print("1. Agregar Bus")
            print("2. Agregar Ruta a Bus")
            print("3. Registrar Horario a Bus")
            print("4. Agregar Conductor")
            print("5. Asignar Horario a Conductor y Bus")
            print("6. Salir")

            opcion = input("Seleccione una opción: ")

            if opcion == "1":
                id_bus = input("Ingrese el ID del bus: ")
                print(self.agregar_bus(id_bus))

            elif opcion == "2":
                id_bus = input("Ingrese el ID del bus: ")
                ruta = input("Ingrese la ruta: ")
                bus = self.obtener_bus(id_bus)
                if bus:
                    bus.asignar_ruta(ruta)
                    print(f"Ruta '{ruta}' asignada al bus {id_bus}.")
                else:
                    print(f"El bus con ID {id_bus} no existe.")

            elif opcion == "3":
                id_bus = input("Ingrese el ID del bus: ")
                horario = input("Ingrese el horario (ej. 08:00): ")
                bus = self.obtener_bus(id_bus)
                if bus:
                    bus.registrar_horario(horario)
                    print(f"Horario '{horario}' registrado para el bus {id_bus}.")
                else:
                    print(f"El bus con ID {id_bus} no existe.")

            elif opcion == "4":
                nombre = input("Ingrese el nombre del conductor: ")
                id_conductor = input("Ingrese el ID del conductor: ")
                print(self.agregar_conductor(nombre, id_conductor))

            elif opcion == "5":
                id_bus = input("Ingrese el ID del bus: ")
                id_conductor = input("Ingrese el ID del conductor: ")
                horario = input("Ingrese el horario: ")
                bus = self.obtener_bus(id_bus)
                conductor = self.obtener_conductor(id_conductor)

                if bus and conductor:
                    print(bus.asignar_conductor(horario, conductor))
                else:
                    if not bus:
                        print(f"El bus con ID {id_bus} no existe.")
                    if not conductor:
                        print(f"El conductor con ID {id_conductor} no existe.")

            elif opcion == "6":
                print("Saliendo del sistema de gestión de tickets.")
                break

            else:
                print("Opción no válida, intente de nuevo.")



admin = Admin()
admin.mostrar_menu()