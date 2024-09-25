import cv2
import numpy as np


video_cap = cv2.VideoCapture(1)



video_con = cv2.VideoCapture("videos\Conte grande ampliado.mov")

while True:
    ret_con, frame_con = video_con.read()
    ret, frame_cap = video_cap.read()
   
    

    
    
    

    
    if ret_con == True:
        
        #frame_con = cv2.resize(frame_con,(640,480))
        frame_cap = cv2.resize(frame_cap,(1823,1367))
        suma = cv2.add(frame_con,frame_cap)
        print("video:", frame_cap.shape)
        print("conteo:", frame_con.shape)
        #cv2.imshow("video cap", frame_cap)
        #cv2.imshow("video con", frame_con)
        cv2.namedWindow("combinado:", cv2.WND_PROP_FULLSCREEN)
        cv2.setWindowProperty("combinado:", cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)
        cv2.imshow("combinado:", suma)
        
        cv2.waitKey(1) 
            
            
    else:break
       
    


cv2.destroyAllWindows()

    
    
    
    
    

