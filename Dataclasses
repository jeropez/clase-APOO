from dataclasses import dataclass, field, asdict
import Operaciones
from typing import List

@dataclass
class Persona:
    __nombre: str = field(repr=False)
    edad: int = field(default=35)

    @property
    def retornar_edad_por_2(self) -> int:
        return print(self.edad * 2)
    
@dataclass
class Puesto:
    nombre: str
    persona: Persona

@dataclass
class Grupo:
    personas: List[Persona] = field(default_factory=list)

persona1 = Persona('Juan', 36)
persona2 = Persona('Camila')

print(persona1.retornar_edad_por_2)

puesto1 = Puesto('Desarrollador', persona1)

grupo1 = Grupo()
grupo1.personas.append(persona1)
grupo1.personas.append(persona2)

print(grupo1)
print(puesto1)
print(asdict(persona1))

print(Operaciones.suma(persona1.edad, persona2.edad))

if persona1 == persona2:
    print('Son iguales')
else: 
    print('No son iguales')

