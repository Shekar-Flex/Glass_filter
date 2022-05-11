from cv2 import cv2
import cvzone
import datetime

cap=cv2.VideoCapture(0)
cc=cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
layout=cv2.imread('sunglass.png',cv2.IMREAD_UNCHANGED)

while True:
    try:
        _,img=cap.read()
        gray_scale=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
        face=cc.detectMultiScale(gray_scale)
        for (x,y,w,h) in face:
            # cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),2)
            lay_resize=cv2.resize(layout,(int(w*1.5),int(h*1.5)))
            framse=cvzone.overlayPNG(img,lay_resize,[x-42,y-72])
        # cv2.imshow('output',img)
        cv2.imshow('output',framse)
        if cv2.waitKey(11)==ord('s'):
            cv2.imwrite(f'photo{datetime.date.today()}.png',framse)
            break
        if cv2.waitKey(10)==ord('q'):
            print(cv2.waitKey(10),ord('q'))
            break
    except Exception as e:
        print("Face is not detected....")
        continue
