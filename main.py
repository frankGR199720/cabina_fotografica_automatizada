import cv2
import fpdf
import random
import win32api
import win32print
from pynput import keyboard as kb
from tkinter import messagebox
import os
import datetime as dt
import shutil as sh



          
direccion_de_loading = "multimedia\loading\Loading_1.mov"
direccion_pro_pantalla = "multimedia/protector de pantalla/Protector de pantallas ampliado.mov"
direccion_instructivo = "multimedia\instructivo\Instrucciones ampliado - full.mov"
direccion_flash = "multimedia/videos_conteo/Flash.mov"
direccion_imp = "multimedia/imprimiendo/Imprimiendo ampliado - full.mov"
direccion_des = "multimedia/despedida/Despedida.mov"
direccion_de_seciones_guardadas = "seciones guardadas/"
nombre_secion = dt.datetime.now().strftime('secion %m-%y-%H-%M')
direccion_de_seciones_en_album = "album de fotos/carpeta "



    


class Procesos:
            
    def detector_de_cara(vid, dibujar= True):
        face_classifier = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
        gray_image = cv2.cvtColor(vid, cv2.COLOR_BGR2GRAY)
        faces = face_classifier.detectMultiScale(gray_image, 1.7, 5, minSize=(40, 40))
        if dibujar:
            for (x, y, w, h) in faces:
                cv2.rectangle(vid, (x, y), (x + w, y + h), (0, 255, 0), 4)
        return faces
    
    def pdf(ev):
        while escuchador.is_alive():

            # numero_al = random.randint(0,5)
            numero_al = random.randint(0,3)
           
            pdf = fpdf.FPDF()
            pdf.add_page()
            # Agregamos una imagen
    

            pdf.image("album de fotos/carpeta "+ str(ev) + "/imagen 0.jpg",10,29,92,69)

            pdf.image("album de fotos/carpeta "+ str(ev) + "/imagen 1.jpg",108,29,92,69)

            pdf.image("album de fotos/carpeta "+ str(ev) + "/imagen 2.jpg",10,105,92,69)

            pdf.image("album de fotos/carpeta "+ str(ev) + "/imagen 3.jpg",108,105,92,69)

            pdf.image("album de fotos/carpeta "+ str(ev) + "/imagen 4.jpg",10,181,92,69)

            pdf.image("album de fotos/carpeta "+ str(ev) + "/imagen 5.jpg",108,181,92,69)

            #pdf.image("plantillas/Plantilla cabina " + str(numero_al) + ".png", 0, 0)

            pdf.image("plantillas/Plantillas RBTD/Plantilla RBTD 6XF-0" + str(numero_al) + ".png", 0, 0)

            # Guardamos el documento
            pdf.output("album de fotos/carpeta "+ str(ev) + "/documento.pdf")
            break

    def imprimir(ev):
        ghostscript = os.path.abspath(os.getcwd()) + "/adit/gs10.04.0/bin/gswin64.exe"
        gsprint = os.path.abspath(os.getcwd()) + "/adit/GSPRINT/gsprint.exe"
        ruta_de_impresion =os.path.abspath(os.getcwd()) + "/album de fotos/carpeta " + str(ev)+ "/documento.pdf"
        while escuchador.is_alive():
            impresora = win32print.GetDefaultPrinter()
            
            win32api.ShellExecute(0,
                                   'print',
                                     ruta_de_impresion,
                                       win32print.GetDefaultPrinter(),
                                         '.',
                                           0)
            break

    def creacion_de_carpeta(ev):
        while escuchador.is_alive():
            ruta_de_carpeta = "album de fotos/carpeta " + str(ev)
            if not os.path.exists(ruta_de_carpeta):
                print("carpeta creada: ", ruta_de_carpeta)
                os.makedirs(ruta_de_carpeta)
                break
            
    
class Animaciones:

    def bucle_striming_maxc(vid,car_min,car_max):
        video_capture = cv2.VideoCapture(1)
        while escuchador.is_alive():
            is_closed = False
            video_pro_pan = cv2.VideoCapture(vid)
            
            while escuchador.is_alive():
                ret_cap, video_frame = video_capture.read()
                ret_pan, frame = video_pro_pan.read()
                video_frame = cv2.flip(video_frame,1)
                info_caras = Procesos.detector_de_cara(video_frame)
                info_caras = len(info_caras)
                print("on/off_cap: ", ret_cap)
                print("on/off_pan: ", ret_pan)
                if ret_pan == True:
                    cv2.namedWindow("animacion", cv2.WND_PROP_FULLSCREEN)
                    cv2.setWindowProperty("animacion", cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)
                    cv2.imshow("animacion",frame)
                    #cv2.imshow("detector de gestos", video_frame)
                    if (info_caras == car_min and info_caras <= car_max):
                        is_closed = True
                        break
                    cv2.waitKey(1)
                else: break
                
            if is_closed:
                break
        video_capture.release()
        cv2.destroyAllWindows
           
    def captura_fotos(ev):
       
        
        Procesos.creacion_de_carpeta(ev)
        for i in range(6):
            cap_conteo = cv2.VideoCapture("multimedia/videos_conteo/ConteoNumerado/Conteo Ampliado " + str(i+1) +  ".mov")
            cap_video = cv2.VideoCapture(1)
            tiempoA = dt.datetime.now()
            
            while escuchador.is_alive():
                
                ret_vid, imagen_conteo = cap_conteo.read()
                ret, imagen_cap = cap_video.read()
                if ret_vid == True:
                    imagen_conteo = cv2.resize(imagen_conteo,(640,480))
                    imagen_cap = cv2.flip(imagen_cap,1)
                    suma = cv2.add(imagen_conteo,imagen_cap)
                    tiempoB = dt.datetime.now()
                    tiempoTranscurrido = tiempoB - tiempoA
                    cv2.namedWindow("video cap", cv2.WND_PROP_FULLSCREEN)
                    cv2.setWindowProperty("video cap", cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)
                    cv2.imshow('video cap', suma)
                    if tiempoTranscurrido.seconds >= 3 :
                        cv2.imwrite("album de fotos/carpeta " + str(ev) + "/imagen " + str(i) + ".jpg",imagen_cap)
            
                        # Se debe establecer un nuevo tiempoA
                        tiempoA = dt.datetime.now() 
                        print(tiempoTranscurrido)
                        break

           
                    if cv2.waitKey(1) == 27:
                        break

                else:break
               
        
    
            cap_flash = cv2.VideoCapture(direccion_flash)
            while escuchador.is_alive():
                ret_flash,imagen_flas = cap_flash.read()
                ret, imagen_cap = cap_video.read()        
                if ret_flash == True:
                    imagen_cap = cv2.flip(imagen_cap,1)
                    suma = cv2.add(imagen_flas,imagen_cap)
                    cv2.namedWindow("video_flash", cv2.WND_PROP_FULLSCREEN)
                    cv2.setWindowProperty("video_flash", cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)
                    cv2.imshow("video_flash", suma)

                    if cv2.waitKey(27) ==27:
                
                        break

                else:break

            cv2.destroyAllWindows()

    
        cap_video.release()        
        
    def video(video_es, tiempo):
        video = cv2.VideoCapture(video_es)
        
        while escuchador.is_alive():
            ret, frame = video.read()
            
            print("on/off_vid", ret)
            if ret == True:
                cv2.namedWindow("video", cv2.WND_PROP_FULLSCREEN)
                cv2.setWindowProperty("video", cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)
                cv2.imshow("video", frame)
                

            cv2.waitKey(tiempo)
            if not ret:
                break
        
            
        
        cv2.destroyAllWindows()

        
def pulsa(tecla):
	    print('Se ha pulsado la tecla ' + str(tecla))

def suelta(tecla):
           
	if tecla == kb.KeyCode.from_char('q'):
            if os.listdir("album de fotos/"):
                carpeta =1 
                while True:
                    isclosed = 0
                    if not os.path.exists(direccion_de_seciones_guardadas + nombre_secion):
                        os.makedirs(direccion_de_seciones_guardadas + nombre_secion)
                        print("carpeta creada: ", direccion_de_seciones_guardadas + nombre_secion)
            
                    while True:
                        if os.path.exists(direccion_de_seciones_en_album + str(carpeta)):
                            print("carpeta existente")
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
            else: 
                print("no existen carpetas")
            exit()
        


 


if __name__ == "__main__":

    escuchador = kb.Listener(pulsa, suelta)
    escuchador.start()

    Animaciones.video(direccion_de_loading, 30 )
    evento = 0
    
    while escuchador.is_alive():
    
        Animaciones.bucle_striming_maxc(direccion_pro_pantalla,1,1)
        evento = evento +1
        
        Animaciones.video(direccion_instructivo,15)
        Animaciones.captura_fotos(evento)
        
        Procesos.pdf(evento)
        #Procesos.imprimir(evento)
        Animaciones.video(direccion_imp,30)
        
        Animaciones.bucle_striming_maxc(direccion_des,0,0)
                
    print("programa cerrado")
    messagebox.showinfo(message="Pocesos y sistemas apagados", title="on/off")

 