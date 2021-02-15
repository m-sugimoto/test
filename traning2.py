import cv2

img = cv2.imread('/Users/sugimotomamoru/python/glasspicture/1608088589000.jpg')

cascade_file = 'haarcascade_frontalface_alt.xml'
cascade = cv2.CascadeClassifier(cascade_file)

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

face_list = cascade.detectMultiScale(gray,
                                    scaleFactor=1.11,
                                    minNeighbors = 5,
                                    minSize =(128,128))
                                    #flag = cv2.CASCADE_SCALE_IMAGE)

color = (0,0,255)

#if len(face_list) > 0:

for face in face_list:
  x,y,w,h = face
  cv2.rectangle(img,(x,y),(x+w,y+h),color,thickness=2)


#return img

#cap = cv2.VideoCapture(1)

#while True:
  #ret, frame = cap.read()

  #img = Face_Cut(frame)

  #cv2.imshow('Frame', img)

  #k = cv2.waitKey(1)
  #if k == 27:
   #  break

cap.release()
cv2.destroyAllWindows()
