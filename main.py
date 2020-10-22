from Usuario import *
from ActualizaDDBB import *

if __name__ == '__main__':
    ActualizaDDBB.conectar_a_ddbb()
    Usuario.pantalla_principal()
