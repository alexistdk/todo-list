from BaseDeDatos import *


class Tarea:

    def __init__(self, titulo, descripcion, completa):
        self.titulo = titulo
        self.descripcion = descripcion
        self.completa = completa

    @staticmethod
    def agregar_tarea():
        print("Agregar tarea\n")
        titulo = input("Título: ")
        descripcion = input("Descripción: ")
        BaseDeDatos.crear_tarea(titulo, descripcion)

    @staticmethod
    def modificar_tarea():
        print("Modificar tarea\n")
        id_tarea = input("ID de la tarea: ")
        BaseDeDatos.actualizar_tarea(id_tarea)

    @staticmethod
    def cambiar_estado():
        print("Actualizar estado\n")
        id_tarea = input("ID de la tarea: ")
        BaseDeDatos.cambiar_estado(id_tarea)

    @staticmethod
    def eliminar_tarea():
        id_tarea = input("ID de la tarea que desea eliminar: ")
        BaseDeDatos.eliminar_tarea(id_tarea)

    @staticmethod
    def mostrar_tareas(): BaseDeDatos.listar_tareas()
