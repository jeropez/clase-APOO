from typing import List, Optional

class Persona:
    def __init__(self, nombre, correo):
        self.nombre = nombre
        self.correo = correo
    
    def presentarse(self):
        return f"Hola, mi nombre es {self.nombre}."
    
class Empleado(Persona):
    def __init__(self, nombre, correo, salario):
        super().__init__(nombre, correo)
        self.__salario = salario
        if salario < 0:
            raise ValueError("El salario no puede ser negativo.")
        self.salario = float(salario)
    
    def calcular_bono(self, proyecto: Optional["Proyecto"] = None):
        return 0.0
    
    def presentarse(self):
        base = super().presentarse()
        return base
       
class Desarrollador(Empleado):
    def __init__(self, nombre, correo, salario, lenguaje_principal):
        super().__init__(nombre, correo, salario)
        self.lenguaje_principal = lenguaje_principal
    
    def calcular_bono(self, proyecto: Optional["Proyecto"] = None):
        porcentaje = 0.10
        if proyecto is not None:
            if proyecto.numero_tareas() > 5:
                porcentaje += 0.01
        bono = self.salario * porcentaje
        return bono
    
    def presentarse(self):
        return f"{super().presentarse()} Soy Desarrollador/a, mi lenguaje principal es: {self.lenguaje_principal})."

class Analista(Empleado):
    def __init__(self, nombre, correo, salario, seniority):
        super().__init__(nombre, correo, salario)
        self.seniority = seniority.lower()

    def calcular_bono(self, proyecto: Optional["Proyecto"] = None):
        porcentaje = 0.08
        if self.seniority == "senior":
            porcentaje += 0.03
        return self.salario * porcentaje

    def presentarse(self) -> str:
        return f"{super().presentarse()} Soy Analista '{self.seniority}')."
    
class Gerente(Empleado):
    def __init__(self, nombre, correo, salario):
        super().__init__(nombre, correo, salario)
        self._empleados_a_cargo: List[Empleado] = []

    def agregar_empleado(self, e: Empleado) -> None:
        if e is self:
            raise ValueError("Un gerente no puede agregarse a sí mismo como subordinado.")
        if any(emp.correo == e.correo for emp in self._empleados_a_cargo):
            raise ValueError(f"Empleado con correo {e.correo} ya está en el equipo.")
        self._empleados_a_cargo.append(e)

    def remover_empleado(self, e: Empleado):
        for e in self._empleados_a_cargo:
            if e.correo == e.correo:
                self._empleados_a_cargo.remove(e)
                return
        raise ValueError("Empleado no encontrado en el equipo.")

    def listar_equipo(self) -> List[str]:
        return [f"{emp.nombre} <{emp.correo}>" for emp in self._empleados_a_cargo]

    def calcular_bono(self, proyecto: Optional["Proyecto"] = None) -> float:
        return self.salario * 0.12

    def presentarse(self):
        equipo = ", ".join(self.listar_equipo()) or "sin subordinados"
        return f"{super().presentarse()} Soy Gerente. Equipo: {equipo}."
    
class Tarea:
    def __init__(self, tarea_id: int, descripcion, horas_estimadas):
        if horas_estimadas < 0:
            raise ValueError("Las horas estimadas no pueden ser negativas.")
        self.id = tarea_id
        self.descripcion = descripcion
        self.horas_estimadas = float(horas_estimadas)
        self.asignado_a: Optional[Empleado] = None

    def asignar(self, empleado: Empleado) -> None:
        self.asignado_a = empleado

    def desasignar(self) -> None:
        self.asignado_a = None

    def __str__(self):
        asign = f"{self.asignado_a.nombre}<{self.asignado_a.correo}>" if self.asignado_a else "sin asignar"
        return f"Tarea[{self.id}]: {self.descripcion} ({self.horas_estimadas}h) - {asign}"
    
class Proyecto:
    def __init__(self, nombre: str, presupuesto: float):
        if presupuesto < 0:
            raise ValueError("El presupuesto no puede ser negativo.")
        self.nombre = nombre
        self.presupuesto = float(presupuesto)
        # composición: el proyecto crea y controla la vida de sus tareas
        self._tareas: List[Tarea] = []
        self._next_tarea_id = 1

    # composición -> las tareas son creadas por el proyecto
    def agregar_tarea(self, descripcion: str, horas_estimadas: float) -> Tarea:
        tarea = Tarea(self._next_tarea_id, descripcion, horas_estimadas)
        self._tareas.append(tarea)
        self._next_tarea_id += 1
        return tarea

    def eliminar_tarea(self, tarea_id: int) -> None:
        for t in self._tareas:
            if t.id == tarea_id:
                self._tareas.remove(t)
                return
        raise ValueError(f"Tarea con id {tarea_id} no encontrada en el proyecto {self.nombre}.")

    def asignar_empleado(self, tarea_id: int, empleado: Empleado) -> None:
        tarea = self._buscar_tarea_por_id(tarea_id)
        tarea.asignar(empleado)

    def desasignar_empleado(self, tarea_id: int) -> None:
        tarea = self._buscar_tarea_por_id(tarea_id)
        tarea.desasignar()

    def _buscar_tarea_por_id(self, tarea_id: int) -> Tarea:
        for t in self._tareas:
            if t.id == tarea_id:
                return t
        raise ValueError(f"Tarea id {tarea_id} no existe en proyecto {self.nombre}.")

    def listar_tareas(self) -> List[str]:
        return [str(t) for t in self._tareas]

    def numero_tareas(self) -> int:
        return len(self._tareas)

    def tareas_asignadas_a(self, empleado: Empleado) -> List[Tarea]:
        return [t for t in self._tareas if t.asignado_a is not None and t.asignado_a.correo == empleado.correo]

    def __str__(self):
        return f"Proyecto '{self.nombre}' (presupuesto {self.presupuesto:.2f}) con {len(self._tareas)} tareas."


class Empresa:
    def __init__(self, nombre: str):
        self.nombre = nombre
        self.empleados: List[Empleado] = []
        self.proyectos: List[Proyecto] = []

    def agregar_empleado(self, e: Empleado) -> None:
        if any(emp.correo == e.correo for emp in self.empleados):
            raise ValueError(f"Empleado con correo {e.correo} ya existe en la empresa.")
        self.empleados.append(e)

    def crear_proyecto(self, nombre: str, presupuesto: float) -> Proyecto:
        proyecto = Proyecto(nombre, presupuesto)
        self.proyectos.append(proyecto)
        return proyecto

    def eliminar_proyecto(self, proyecto: Proyecto) -> None:
        # Eliminando del registro de la empresa deja que el proyecto y sus tareas desaparezcan (composición)
        if proyecto in self.proyectos:
            self.proyectos.remove(proyecto)
        else:
            raise ValueError("Proyecto no encontrado en la empresa.")

    def asignar_empleado_a_proyecto(self, proyecto: Proyecto, tarea_id: int, empleado: Empleado) -> None:
        if proyecto not in self.proyectos:
            raise ValueError("El proyecto no pertenece a la empresa.")
        if empleado not in self.empleados:
            raise ValueError("El empleado no pertenece a la empresa.")
        proyecto.asignar_empleado(tarea_id, empleado)

    def buscar_empleado_por_correo(self, correo: str) -> Optional[Empleado]:
        for e in self.empleados:
            if e.correo == correo:
                return e
        return None

    def listar_empleados(self) -> List[str]:
        return [f"{e.nombre} <{e.correo}> ({e.__class__.__name__})" for e in self.empleados]

    def listar_proyectos(self) -> List[str]:
        return [str(p) for p in self.proyectos]

print('Bienvenido al sistema de gestión de la empresa.')

while True:
    print("\nMenú Principal:")
    print("1. Crear Empresa")
    print("2. Agregar Empleado")
    print("3. Crear Proyecto")
    print("4. Agregar Tarea a Proyecto")
    print("5. Asignar Empleado a Tarea")
    print("6. Listar Empleados")
    print("7. Listar Proyectos")
    print("8. Calcular Bono de Empleado")
    print("0. Salir")

    opcion = int(input("Seleccione una opción: "))

    if opcion == 1:
        nombre_empresa = input("Ingrese el nombre de la empresa: ")
        empresa = Empresa(nombre_empresa)
        print(f"Empresa '{nombre_empresa}' creada exitosamente.")

    elif opcion == 2:
        if 'empresa' not in locals():
            print("Primero debe crear una empresa.")
            continue
        nombre = input("Nombre del empleado: ")
        correo = input("Correo del empleado: ")
        salario = float(input("Salario del empleado: "))
        tipo = input("Tipo de empleado (Desarrollador/Analista/Gerente): ").strip().lower()

        try:
            if tipo == 'desarrollador':
                lenguaje = input("Lenguaje principal: ")
                empleado = Desarrollador(nombre, correo, salario, lenguaje)
            elif tipo == 'analista':
                seniority = input("Seniority (junior/senior): ")
                empleado = Analista(nombre, correo, salario, seniority)
            elif tipo == 'gerente':
                empleado = Gerente(nombre, correo, salario)
            else:
                print("Tipo de empleado no válido.")
                continue

            empresa.agregar_empleado(empleado)
            print(f"Empleado '{nombre}' agregado exitosamente.")
        except ValueError as ve:
            print(f"Error: {ve}")

    elif opcion == 3:
        if 'empresa' not in locals():
            print("Primero debe crear una empresa.")
            continue
        nombre_proyecto = input("Nombre del proyecto: ")
        presupuesto = float(input("Presupuesto del proyecto: "))
        try:
            proyecto = empresa.crear_proyecto(nombre_proyecto, presupuesto)
            print(f"Proyecto '{nombre_proyecto}' creado exitosamente.")
        except ValueError as ve:
            print(f"Error: {ve}")

    elif opcion == 4:
        if 'empresa' not in locals() or not empresa.proyectos:
            print("Primero debe crear una empresa y un proyecto.")
            continue
        print("Proyectos disponibles:")
        for idx, p in enumerate(empresa.proyectos):
            print(f"{idx + 1}. {p.nombre}")
        proyecto_idx = int(input("Seleccione el proyecto por número: ")) - 1
        if proyecto_idx < 0 or proyecto_idx >= len(empresa.proyectos):
            print("Proyecto no válido.")
            continue    
        descripcion = input("Descripción de la tarea: ")
        horas_estimadas = float(input("Horas estimadas para la tarea: "))
        try:
            tarea = empresa.proyectos[proyecto_idx].agregar_tarea(descripcion, horas_estimadas)
            print(f"Tarea '{descripcion}' agregada al proyecto '{empresa.proyectos[proyecto_idx].nombre}'.")
        except ValueError as ve:
            print(f"Error: {ve}")
            

    elif opcion == 5:
        if 'empresa' not in locals() or not empresa.proyectos or not empresa.empleados:
            print("Primero debe crear una empresa, un proyecto y agregar empleados.")
            continue
        print("Proyectos disponibles:")
        for idx, p in enumerate(empresa.proyectos):
            print(f"{idx + 1}. {p.nombre}")
        proyecto_idx = int(input("Seleccione el proyecto por número: ")) - 1
        if proyecto_idx < 0 or proyecto_idx >= len(empresa.proyectos):
            print("Proyecto no válido.")
            continue
        proyecto = empresa.proyectos[proyecto_idx]
        if not proyecto._tareas:
            print("El proyecto no tiene tareas. Primero agregue una tarea.")
            continue
        print("Tareas disponibles:")
        for t in proyecto._tareas:
            print(f"{t.id}. {t.descripcion} ({t.horas_estimadas}h)")
        tarea_id = int(input("Seleccione la tarea por ID: "))
        correo_empleado = input("Ingrese el correo del empleado a asignar: ")
        empleado = empresa.buscar_empleado_por_correo(correo_empleado)
        if empleado is None:
            print("Empleado no encontrado.")
            continue
        try:
            empresa.asignar_empleado_a_proyecto(proyecto, tarea_id, empleado)
            print(f"Empleado '{empleado.nombre}' asignado a la tarea '{tarea_id}' en el proyecto '{proyecto.nombre}'.")
        except ValueError as ve:
            print(f"Error: {ve}")

    elif opcion == 6:
        if 'empresa' not in locals():
            print("Primero debe crear una empresa.")
            continue
        print("Empleados en la empresa:")
        for emp in empresa.listar_empleados():
            print(emp)
        
    elif opcion == 7:   
        if 'empresa' not in locals():
            print("Primero debe crear una empresa.")
            continue
        print("Proyectos en la empresa:")
        for proj in empresa.listar_proyectos():
            print(proj)
    
    elif opcion == 8:
        if 'empresa' not in locals() or not empresa.empleados:
            print("Primero debe crear una empresa y agregar empleados.")
            continue
        correo_empleado = input("Ingrese el correo del empleado para calcular su bono: ")
        empleado = empresa.buscar_empleado_por_correo(correo_empleado)
        if empleado is None:
            print("Empleado no encontrado.")
            continue
        bono = empleado.calcular_bono()
        print(f"El bono para el empleado '{empleado.nombre}' es: {bono:.2f}")
    
    elif opcion == 0:
        print("Saliendo del sistema. ¡Hasta luego!")
        break
    
