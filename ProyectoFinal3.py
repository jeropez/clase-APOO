from dataclasses import dataclass, field
from abc import ABC, abstractmethod
from typing import Dict, List


# ----- Excepciones personalizadas -----
class ErrorCita(Exception):
    pass

class PacienteNoEncontrado(ErrorCita):
    pass

class MedicoNoEncontrado(ErrorCita):
    pass

class EspecialidadNoCoincide(ErrorCita):
    pass

class ConflictoHorario(ErrorCita):
    pass

class EntradaInvalida(ErrorCita):
    pass


# ----- Clase abstracta base (herencia y polimorfismo) -----
class Persona(ABC):
    @abstractmethod
    def mostrar_informacion(self) -> None:
        pass


@dataclass
class Paciente(Persona):
    nombre: str
    documento: int
    edad: int
    especialidad_necesitada: str
    genero: str
    citas: List["Cita"] = field(default_factory=list)

    def mostrar_informacion(self) -> None:
        print("----- Información del Paciente -----")
        print(f"Nombre: {self.nombre}")
        print(f"Documento: {self.documento}")
        print(f"Edad: {self.edad}")
        print(f"Especialidad Necesitada: {self.especialidad_necesitada}")
        print(f"Género: {self.genero}")
        print(f"Citas asignadas: {len(self.citas)}")


@dataclass
class Medico(Persona):
    nombre: str
    documento: int
    especialidad: str
    consultorio: int
    citas_asignadas: List["Cita"] = field(default_factory=list)

    def atender_paciente(self) -> None:
        if not self.citas_asignadas:
            print(f"El Dr. {self.nombre} no tiene pacientes en cola.")
            return
        cita = self.citas_asignadas.pop(0)
        if cita in cita.paciente.citas:
            cita.paciente.citas.remove(cita)
        print(f"✅ El Dr. {self.nombre} atendió al paciente {cita.paciente.nombre}.")

    def mostrar_informacion(self) -> None:
        print("----- Información del Médico -----")
        print(f"Nombre: {self.nombre}")
        print(f"Documento: {self.documento}")
        print(f"Especialidad: {self.especialidad}")
        print(f"Consultorio: {self.consultorio}")
        print(f"Citas asignadas: {len(self.citas_asignadas)}")


@dataclass
class Cita:
    fecha: str
    hora: str
    medico: Medico
    paciente: Paciente

    def mostrar_informacion(self) -> None:
        print("----- Información de la Cita -----")
        print(f"Fecha: {self.fecha}")
        print(f"Hora: {self.hora}")
        print(f"Médico: {self.medico.nombre}")
        print(f"Consultorio: {self.medico.consultorio}")
        print(f"Paciente: {self.paciente.nombre}")


# ----- Administrador de citas (composición) -----
class AppointmentManager:
    def __init__(self):
        self.pacientes: Dict[int, Paciente] = {}
        self.medicos: Dict[int, Medico] = {}
        self.citas: List[Cita] = []  # compuesto por el manager

    def registrar_paciente(self, nombre, documento, edad, especialidad, genero):
        if documento in self.pacientes:
            raise EntradaInvalida("Ya existe un paciente con ese documento.")
        p = Paciente(nombre, documento, edad, especialidad, genero)
        self.pacientes[documento] = p
        return p

    def registrar_medico(self, nombre, documento, especialidad, consultorio):
        if documento in self.medicos:
            raise EntradaInvalida("Ya existe un médico con ese documento.")
        m = Medico(nombre, documento, especialidad, consultorio)
        self.medicos[documento] = m
        return m

    def obtener_paciente(self, documento):
        if documento not in self.pacientes:
            raise PacienteNoEncontrado
        return self.pacientes[documento]

    def obtener_medico(self, documento):
        if documento not in self.medicos:
            raise MedicoNoEncontrado
        return self.medicos[documento]

    def crear_cita(self, documento_paciente, documento_medico, fecha, hora):
        paciente = self.obtener_paciente(documento_paciente)
        medico = self.obtener_medico(documento_medico)

        if paciente.especialidad_necesitada.lower() != medico.especialidad.lower():
            raise EspecialidadNoCoincide("Especialidad no coincide.")

        for c in medico.citas_asignadas:
            if c.fecha == fecha and c.hora == hora:
                raise ConflictoHorario("El médico ya tiene una cita en ese horario.")
        for c in paciente.citas:
            if c.fecha == fecha and c.hora == hora:
                raise ConflictoHorario("El paciente ya tiene una cita en ese horario.")

        cita = Cita(fecha, hora, medico, paciente)
        self.citas.append(cita)
        medico.citas_asignadas.append(cita)
        paciente.citas.append(cita)
        return cita

    def cancelar_cita(self, cita):
        if cita in self.citas:
            self.citas.remove(cita)
        if cita in cita.medico.citas_asignadas:
            cita.medico.citas_asignadas.remove(cita)
        if cita in cita.paciente.citas:
            cita.paciente.citas.remove(cita)


# ----- Menú principal -----
def main():
    manager = AppointmentManager()

    while True:
        print("\n--- MENÚ ---")
        print("1 Registrar Paciente")
        print("2 Registrar Médico")
        print("3 Crear Cita")
        print("4 Atender Paciente")
        print("5 Mostrar Paciente")
        print("6 Mostrar Médico")
        print("7 Mostrar Citas")
        print("8 Cancelar Cita")
        print("0 Salir")

        try:
            op = input("Opción: ").strip()

            if op == "1":
                nombre = input("Nombre: ")
                doc = int(input("Documento: "))
                edad = int(input("Edad: "))
                esp = input("Especialidad requerida: ")
                gen = input("Género: ")
                manager.registrar_paciente(nombre, doc, edad, esp, gen)
                print("Paciente registrado ✅")

            elif op == "2":
                nombre = input("Nombre: ")
                doc = int(input("Documento: "))
                esp = input("Especialidad: ")
                cons = int(input("Consultorio: "))
                manager.registrar_medico(nombre, doc, esp, cons)
                print("Médico registrado ✅")

            elif op == "3":
                dp = int(input("Documento paciente: "))
                dm = int(input("Documento médico: "))
                fecha = input("Fecha (DD/MM/AAAA): ")
                hora = input("Hora (HH:MM): ")
                cita = manager.crear_cita(dp, dm, fecha, hora)
                print("Cita creada ✅")
                cita.mostrar_informacion()

            elif op == "4":
                dm = int(input("Documento médico: "))
                m = manager.obtener_medico(dm)
                m.atender_paciente()

            elif op == "5":
                dp = int(input("Documento (0 todos): "))
                if dp == 0:
                    for p in manager.pacientes.values():
                        p.mostrar_informacion()
                else:
                    manager.obtener_paciente(dp).mostrar_informacion()

            elif op == "6":
                dm = int(input("Documento (0 todos): "))
                if dm == 0:
                    for m in manager.medicos.values():
                        m.mostrar_informacion()
                else:
                    manager.obtener_medico(dm).mostrar_informacion()

            elif op == "7":
                if not manager.citas:
                    print("No hay citas.")
                else:
                    for c in manager.citas:
                        c.mostrar_informacion()

            elif op == "8":
                if not manager.citas:
                    print("No hay citas para cancelar.")
                else:
                    for i, c in enumerate(manager.citas, start=1):
                        print(f"{i}. {c.paciente.nombre} - {c.medico.nombre} {c.fecha} {c.hora}")
                    idx = int(input("Número de cita a cancelar: ")) - 1
                    manager.cancelar_cita(manager.citas[idx])
                    print("Cita cancelada ✅")

            elif op == "0":
                print("Saliendo...")
                break

            else:
                print("⚠️ Opción inválida")

        except ErrorCita as e:
            print(f"[ERROR] {e}")
        except Exception:
            print("[ERROR] Entrada inválida")


if __name__ == "__main__":
    main()
