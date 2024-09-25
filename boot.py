import os
from os import rmdir
import datetime as dt
import shutil as sh

direccion_de_seciones_guardadas = "seciones guardadas/"
nombre_secion = dt.datetime.now().strftime('secion %m-%y-%H-%M')
direccion_de_seciones_en_album = "album de fotos/carpeta "

if __name__ == "__main__":
    #os.makedirs(direccion_de_almacen + nombre_secion)
    
    carpeta = 1
    
    while True:
        isclosed = 0
        if not os.path.exists(direccion_de_seciones_guardadas + nombre_secion):
            os.makedirs(direccion_de_seciones_guardadas + nombre_secion)
            print("carpeta creada: ", direccion_de_seciones_guardadas + nombre_secion)
            
            while True:
                if os.path.exists(direccion_de_seciones_en_album + str(carpeta)):
                    print("carpeta existente")
                    if os.listdir(direccion_de_seciones_en_album + str(carpeta)):
                        sh.move(direccion_de_seciones_en_album + str(carpeta), direccion_de_seciones_guardadas + nombre_secion)
                        carpeta =carpeta+1

                    else:
                        print("carpeta vacia... borrar directorio")
                        os.rmdir(direccion_de_seciones_en_album + str(carpeta))

                else:
                    print("no existe la carpeta ")
                    isclosed = 1
                    break
        

        if isclosed:
            break

                




        

            


     
    

        
    
   