from ActualizaDDBB import *


class Tarea:

    def __init__(self, titulo, descripcion, completa):
        self.titulo = titulo
        self.descripcion = descripcion
        self.completa = completa

    usuario_logueado = 0

    @classmethod
    def usuario_logueado(cls, id_usuario): cls.usuario_logueado = id_usuario

    @classmethod
    def agregar_tarea(cls):
        print("Agregar tarea\n")
        titulo = input("Título: ")
        descripcion = input("Descripción: ")
        ActualizaDDBB.crear_tarea(titulo, descripcion, cls.usuario_logueado)

    @staticmethod
    def modificar_tarea():
        print("Modificar tarea\n")
        id_tarea = input("ID de la tarea: ")
        ActualizaDDBB.actualizar_tarea(id_tarea)

    @staticmethod
    def cambiar_estado():
        print("Actualizar estado\n")
        id_tarea = input("ID de la tarea: ")
        ActualizaDDBB.cambiar_estado(id_tarea)

    @staticmethod
    def eliminar_tarea():
        id_tarea = input("ID de la tarea que desea eliminar: ")
        ActualizaDDBB.eliminar_tarea(id_tarea)

    @classmethod
    def mostrar_tareas(cls): ActualizaDDBB.listar_tareas(cls.usuario_logueado)
