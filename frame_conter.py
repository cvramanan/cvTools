import cv2 

cnt = 0

cam = cv2.VideoCapture("datainput/testvid_alfa.mp4")

while True:
    ret, frame = cam.read()
    # cv2.imshow("frame", frame)
    if ret == True:
        cnt += 1
        print(cnt)
    else:
        break
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break