import cv2
import datetime as dt

if __name__ == "__main__":
    for i in range(6):
        cap_conteo = cv2.VideoCapture("Conteo-foto\Square-640-480.mov")
        cap_video = cv2.VideoCapture(1)
        tiempoA = dt.datetime.now()
        path = 'Nueva carpeta/'
        while (cap_conteo.isOpened()):
            isclosed = 0
            ret_vid, imagen_conteo = cap_conteo.read()
            ret, imagen_cap = cap_video.read()
            if ret_vid == True:
                imagen_cap = cv2.flip(imagen_cap,1)
                suma = cv2.add(imagen_conteo,imagen_cap)
                tiempoB = dt.datetime.now()
                tiempoTranscurrido = tiempoB - tiempoA
                cv2.namedWindow("video cap", cv2.WND_PROP_FULLSCREEN)
                cv2.setWindowProperty("video cap", cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)
                cv2.imshow('video cap', suma)
                if tiempoTranscurrido.seconds >= 3 :
                    cv2.imwrite("Nueva carpeta/imagen " + str(i) + ".jpg",imagen_cap)
            
            #Se debe establecer un nuevo tiempoA
                    tiempoA = dt.datetime.now() 
                    print(tiempoTranscurrido)
                    break

           
                if cv2.waitKey(15) == 27:
                    break

            else:break
               
        
    
        cap_flash = cv2.VideoCapture("Conteo-foto\Flash.mov")
        while (cap_flash.isOpened()):
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

        cv2.destroyWindow("video cap")
        cv2.destroyWindow("video_flash")

    
    cap_video.release()
    