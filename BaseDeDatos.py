from datetime import date
from ConectarDDBB import *


class BaseDeDatos(ConectarDDBB):

    @classmethod
    def crear_tarea(cls, titulo, descripcion):
        try:
            db = cls.conexion()
            cursor = db.cursor()
            fecha = date.today()
            cursor.execute(cls.insertar_tarea(), (fecha, titulo, descripcion, 0))
        except Error:
            print("Error ", Error)
        finally:
            db.commit()

    @classmethod
    def existe_tarea(cls, titulo):
        try:
            db = cls.conexion()
            cursor = db.cursor()
            cursor.execute(cls.busca_tarea, titulo)
            return True
        except Error:
            print("Error ", Error)

    @classmethod
    def actualizar_tarea(cls, id_tarea):
        try:
            db = cls.conexion()
            cursor = db.cursor()
            descripcion = input("Descripción nueva: ")
            cursor.execute(cls.actualizar_descripcion(), (descripcion, id_tarea))
        except Error:
            print("No existe la tarea!", Error)
        finally:
            db.commit()

    @classmethod
    def cambiar_estado(cls, id_tarea):
        try:
            db = cls.conexion()
            cursor = db.cursor()
            cursor.execute(cls.actualizar_estado(), (id_tarea, ))
        except Error:
            print("Error ", Error)
        finally:
            db.commit()

    @classmethod
    def listar_tareas(cls):
        try:
            db = cls.conexion()
            cursor = db.cursor()
            cursor.execute(cls.seleccionar_tareas())
            records = cursor.fetchall()
            print("\nLista de tareas\n ")
            for row in records:
                print("ID = ", row[0])
                print("Fecha = ", row[1])
                print("Título  = ", row[2])
                print("Descripción  = ", row[3])
                print("Estado = ", row[4], "\n")
        except Error:
            print("Error al leer la lista de tareas", Error)

    @classmethod
    def eliminar_tarea(cls, id_tarea):
        try:
            db = cls.conexion()
            cursor = db.cursor()
            cursor.execute(cls.borrar_tarea(), (id_tarea,))
        except Error:
            print("Error al eliminar la tarea", Error)
        finally:
            db.commit()
