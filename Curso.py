__author__= "Juan Sebastian Ibarra Salas"
__License__="GPL"
__Version__="1.0.0"
__Email__="juan.ibarrasalas@campusucc.edu.co"

class Curso:
    notaMaxima = 5.0
    notaMinima = 1.5
    
    def __init__(self, codigo="", nombre="", departamento="", creditos=0, nota=0.0):
        # Atributos
        self.__codigo = codigo
        self.__nombre = nombre
        self.__departamento = departamento
        self.__creditos = creditos
        self.__nota = nota
    
    # Métodos
    def darCodigo(self):
        return self.__codigo

    def darNombre(self):
        return self.__nombre

    def darDepartamento(self):
        return self.__departamento

    def darCreditos(self):
        return self.__creditos

    def darNota(self):
        return self.__nota

    # Asigna la nota al curso
    def asignarNota(self, nota):
        if self.notaMinima <= nota <= self.notaMaxima:
            self.__nota = nota
            return True
        return False
    
    # Evalua si el curso esta calificado
    def estaCalificado(self):
        return self.__nota != 0.0
