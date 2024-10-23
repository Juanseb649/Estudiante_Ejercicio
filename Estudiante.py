__author__= "Juan Sebastian Ibarra Salas"
__License__="GPL"
__Version__="1.0.0"
__Email__="juan.ibarrasalas@campusucc.edu.co"

from Curso import Curso
from Departamento import Departamento

class Estudiante:
    
    NOTA_PRUEBA_ACADEMICA = 3.25
    CANDIDATO_BECA = 4.75

    def __init__(self, nombre, apellido, codigo):
        # Atributos
        self.__nombre = nombre
        self.__apellido = apellido
        self.__codigo = codigo
        self.__Curso1 = Curso()
        self.__Curso2 = Curso()
        self.__Curso3 = Curso()
        self.__Curso4 = Curso()
    
    # Métodos
    def darNombre(self):
        return self.__nombre

    def darApellido(self):
        return self.__apellido

    def darCodigo(self):
        return self.__codigo

    def darCurso1(self):
        return self.__Curso1

    def darCurso2(self):
        return self.__Curso2

    def darCurso3(self):
        return self.__Curso3

    def darCurso4(self):
        return self.__Curso4

    # Permite calcular el promedio de las notas de los cursos con los creditos
    
    def calcularPromedioEstudiante(self):
        notaCurso1 = self.__Curso1.darNota() * self.__Curso1.darCreditos()
        notaCurso2 = self.__Curso2.darNota() * self.__Curso2.darCreditos()
        notaCurso3 = self.__Curso3.darNota() * self.__Curso3.darCreditos()
        notaCurso4 = self.__Curso4.darNota() * self.__Curso4.darCreditos()

        creditosTotales = self.__Curso1.darCreditos() + self.__Curso2.darCreditos() + \
    self.__Curso3.darCreditos() + self.__Curso4.darCreditos()

        return (notaCurso1 + notaCurso2 + notaCurso3 + notaCurso4) / creditosTotales

    # Evalúa si el promedio del estudiante es menor a la nota prueba académica
    def estaEnPrueba(self):
        return self.calcularPromedioEstudiante() <= Estudiante.NOTA_PRUEBA_ACADEMICA

    # Evalúa si el estudiante es candidato apto para la beca
    
    def esCandidatoBeca(self):
        return self.calcularPromedioEstudiante() >= Estudiante.CANDIDATO_BECA
    
    # Se busca un curso con su código
    
    def buscarCurso(self, codigo):
        if codigo == self.__Curso1.darCodigo():
            return self.__Curso1
        elif codigo == self.__Curso2.darCodigo():
            return self.__Curso2
        elif codigo == self.__Curso3.darCodigo():
            return self.__Curso3
        elif codigo == self.__Curso4.darCodigo():
            return self.__Curso4
        else:
            return None
    
    # Asigna una nota a un curso con su codigo
    
    def asignarNotaCurso(self, codigo, nota):
        curso = self.buscarCurso(codigo)
        if curso is not None:
            curso.asignarNota(nota)
            return True
        return False
    
    # Cambia la información de un curso en base a su código
    
    def cambiarCurso(self, codigoActual, codigoNuevo, nombre, departamento, creditos):
        curso = self.buscarCurso(codigoActual)
        if curso is not None:
            curso = Curso(codigoNuevo, nombre, departamento, creditos, 0.0)
            return True
        return False