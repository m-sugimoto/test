
import cv2

cap = cv2.VideoCapture(0)

#ret, frame = cap.read()
while(True):
    ret, frame = cap.read()
    cv2.imshow('frame',frame)
    key = cv2.waitKey(1) & 0xFF
    if key == ord('c'):
        cv2.imwrite("/Users/sugimotomamoru/python/結果画像/picture2-1.jpg", frame)
        n += 1
    elif key == ord('q'):
        break