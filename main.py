from ConectarDDBB import *
from Menu import *

if __name__ == '__main__':
    ConectarDDBB.conectar_a_ddbb()
    Menu.menu_principal()
    Menu.elegir_opcion()
