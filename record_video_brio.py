import os  
import time
# from tkinter import Frame
import cv2 


class Camera: 
    def __init__(self):  
        self.camId = "/dev/v4l/by-id/usb-046d_Logitech_BRIO_E2FCDB73-video-index0"
        # self.camId = "/dev/video2"
        
        
        self.device = cv2.VideoCapture(self.camId,cv2.CAP_V4L)
        self.setParams()
    
    def fetchImage(self):
        ret_value,frame = self.device.read()
        if ret_value == True:
            return frame


        else:
            exit()


    def setParams(self):



        # os.system("v4l2-ctl --device /dev/v4l/by-id/usb-046d_Logitech_BRIO_E2FCDB73-video-index0 --set-ctrl=exposure_auto=1 ")
        # os.system("v4l2-ctl --device /dev/v4l/by-id/usb-046d_Logitech_BRIO_E2FCDB73-video-index0 --set-ctrl=exposure_absolute=17 ")
        # os.system("v4l2-ctl --device /dev/v4l/by-id/usb-046d_Logitech_BRIO_E2FCDB73-video-index0 --set-ctrl=focus_auto=0 ")
        # os.system("v4l2-ctl --device /dev/v4l/by-id/usb-046d_Logitech_BRIO_E2FCDB73-video-index0 --set-ctrl=focus_absolute=25 ")
        # os.system("v4l2-ctl --device /dev/v4l/by-id/usb-046d_Logitech_BRIO_E2FCDB73-video-index0 --set-ctrl=white_balance_temperature_auto=0 ")
        # os.system("v4l2-ctl --device /dev/v4l/by-id/usb-046d_Logitech_BRIO_E2FCDB73-video-index0 --set-ctrl=white_balance_temperature=5000 ")
        # os.system("v4l2-ctl --device /dev/v4l/by-id/usb-046d_Logitech_BRIO_E2FCDB73-video-index0 --set-ctrl=gain=0 ")
        os.system("v4l2-ctl --device "+self.camId+" --set-fmt-video=width=4096,height=2160,pixelformat=MJPG")
        
        time.sleep(1)
        # self.device.set(cv2.CV_CAP_PROP_FOURCC,cv2.VideoWriter_fourcc(*'MJPEG'))
        # cv2.VideoWriter_fourcc(*'MJPEG')
        
        # self.device.set(cv2.CAP_PROP_FORMAT,('M', 'J', 'P', 'G'))
        # self.device.set(cv2.CAP_PROP_FORMAT, cv2.VideoWriter.fourcc('M','J','P','G'))
        # self.device.set(3,4096)
        # self.device.set(4,2160)

        

if __name__ == "__main__":
    cam = Camera()
    pT = 0
    while True:
        t = time.time()
        image = cam.fetchImage()
        # print("hi")
        print("fps: ",1/(time.time()-t))

        if time.time() - pT > 0.1:
            cv2.imwrite( "./temp/"+str(time.time())+ "image.png",image)
            
            pT = time.time()


        # cv2.imshow("video",image)
        print(image.shape)
        cv2.waitKey(1)

                 

        
