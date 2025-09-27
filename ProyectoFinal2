class Paciente:
    def __init__(self, nombre, documento, edad, especialidad_necesitada, genero):
        self.nombre = nombre
        self.documento = documento
        self.edad = edad
        self.especialidad_necesitada = especialidad_necesitada
        self.genero = genero
        self.cita = None  # Relación 1:1 con Cita

    def pedir_cita(self, medico, fecha, hora):
        if medico.especialidad != self.especialidad_necesitada:
            print(f"No se puede asignar cita: el médico {medico.nombre} no coincide con la especialidad requerida ({self.especialidad_necesitada}).")
            return None
        self.cita = Cita(fecha, hora, medico, self)
        print(f"Cita creada exitosamente para el/la paciente {self.nombre}.")
        return self.cita

    def mostrar_informacion(self):
        print("----- Información del Paciente -----")
        print(f"Nombre: {self.nombre}")
        print(f"Documento: {self.documento}")
        print(f"Edad: {self.edad}")
        print(f"Especialidad Necesitada: {self.especialidad_necesitada}")
        print(f"Género: {self.genero}")
        if self.cita:
            print(f"Tiene cita asignada con el Dr. {self.cita.medico.nombre}.")


class Medico:
    def __init__(self, nombre, especialidad, consultorio):
        self.nombre = nombre
        self.especialidad = especialidad
        self.consultorio = consultorio
        self.cita_asignada = None  # Guarda la cita actual

    def atender_paciente(self):
        if self.cita_asignada:
            print(f"El Dr. {self.nombre} ha atendido al paciente {self.cita_asignada.paciente.nombre}.")
            # Eliminar la cita (composición)
            self.cita_asignada = None
        else:
            print(f"El Dr. {self.nombre} no tiene pacientes asignados en este momento.")

    def mostrar_informacion(self):
        print("----- Información del Médico -----")
        print(f"Nombre: {self.nombre}")
        print(f"Especialidad: {self.especialidad}")
        print(f"Consultorio: {self.consultorio}")
        if self.cita_asignada:
            print(f"Tiene una cita con el paciente {self.cita_asignada.paciente.nombre}.")


class Cita:
    def __init__(self, fecha, hora, medico: Medico, paciente: Paciente):
        self.fecha = fecha
        self.hora = hora
        self.medico = medico
        self.especialidad = paciente.especialidad_necesitada  # Desde paciente
        self.consultorio = medico.consultorio  # Desde médico
        self.paciente = paciente

        # Vincular la cita al médico
        medico.cita_asignada = self

    def mostrar_informacion(self):
        print("----- Información de la Cita -----")
        print(f"Fecha: {self.fecha}")
        print(f"Hora: {self.hora}")
        print(f"Especialidad: {self.especialidad}")
        print(f"Consultorio: {self.consultorio}")
        print(f"Médico: {self.medico.nombre}")
        print(f"Paciente: {self.paciente.nombre}")


pacientes = []
medicos = []
citas = []
while True:
    print("\n--- Menú Principal ---")
    print("1. Registrar  Paciente")
    print("2. Registrar Médico")
    print("3. Pedir Cita")
    print("4. Atender Paciente")
    print("5. Mostrar Información Paciente")
    print("6. Mostrar Información Médico")
    print("7. Mostrar Información Cita")
    print("0. Salir")

    opcion = input("Seleccione una opción: ")

    if opcion == "1":
            nombre = input("Nombre del paciente: ")
            documento = int(input("Documento del paciente: "))
            edad = int(input("Edad del paciente: "))
            especialidad_necesitada = input("Especialidad necesaria: ")
            genero = input("Género del paciente: ")
            paciente = Paciente(nombre, documento, edad, especialidad_necesitada, genero)
            pacientes.append(paciente)
            print(f"Paciente {nombre} se ha registrado exitosamente.")

    elif opcion == "2":
            nombre = input("Nombre del médico: ")
            especialidad = input("Especialidad del médico: ")
            consultorio = int(input("Número de consultorio: "))
            medico = Medico(nombre, especialidad, consultorio)
            medicos.append(medico)
            print(f"Médico {nombre} se ha registrado exitosamente.")

    elif opcion == "3":
            if not pacientes or not medicos:
                print("Debe haber al menos un paciente y un médico para pedir una cita.")
                continue
            print("Pacientes disponibles:")
            for i, p in enumerate(pacientes):
                print(f"{i + 1}. {p.nombre} (Especialidad necesaria: {p.especialidad_necesitada})")
            paciente_index = int(input("Seleccione el número del paciente: ")) - 1
            paciente = pacientes[paciente_index]

            print("Médicos disponibles:")
            for i, m in enumerate(medicos):
                print(f"{i + 1}. {m.nombre} (Especialidad: {m.especialidad})")
            medico_index = int(input("Seleccione el número del médico: ")) - 1
            medico = medicos[medico_index]

            fecha = input("Fecha de la cita (DD/MM/AAAA): ")
            hora = input("Hora de la cita (HH:MM): ")
            cita = paciente.pedir_cita(medico, fecha, hora)
            if cita:
                citas.append(cita)
        
    elif opcion == "4":
            if not medicos:
                print("No hay médicos registrados.")
                continue
            print("Médicos disponibles:")
            for i, m in enumerate(medicos):
                print(f"{i + 1}. {m.nombre}")
            medico_index = int(input("Seleccione el número del médico: ")) - 1
            medico = medicos[medico_index]
            medico.atender_paciente()
        
    elif opcion == "5":
            if not pacientes:
                print("No hay pacientes registrados.")
            else:
                input_nombre = input("Ingrese el nombre del paciente para ver su información (o 'todos' para ver todos): ")
                for p in pacientes:
                    if input_nombre == "todos":
                        p.mostrar_informacion()
                    elif p.nombre == input_nombre:                       
                        p.mostrar_informacion()
                    else:
                        print("Paciente no encontrado.")
        
    elif opcion == "6":
            if not medicos:
                print("No hay médicos registrados.")
            else:
                input_nombre = input("Ingrese el nombre del médico para ver su información (o 'todos' para ver todos): ")
                for m in medicos:
                    if input_nombre == "todos":
                        m.mostrar_informacion()
                    elif m.nombre == input_nombre:                       
                        m.mostrar_informacion()
                    else:
                        print("Médico no encontrado.")
    elif opcion == "7":
            if not citas:
                print("No hay citas registradas.")
            else:
                input_nombre = input("Ingrese el nombre del paciente para ver su cita (o 'todos' para ver todas): ")
                for c in citas:
                    if input_nombre == "todos":
                        c.mostrar_informacion()
                    elif c.paciente.nombre == input_nombre:                       
                        c.mostrar_informacion()
                    else:
                        print("Cita no encontrada.")

    elif opcion == "0":
            print("Saliendo del programa.")
            break
    else:
            print("Opción no válida. Intente de nuevo.")
