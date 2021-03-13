import cv2

if __name__ == '__main__':

  img = cv2.imread("/Users/sugimotomamoru/python/テスト画像/fanza3-1.jpg")

  cascade_file_face = "face.xml"
  cascade_face = cv2.CascadeClassifier(cascade_file_face)

  img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
  face_list = cascade_face.detectMultiScale(img_gray, minSize=(10, 10))

  for (x, y, w, h) in face_list:
    color = (0, 0, 255)
    pen_w = 2
    cv2.rectangle(img, (x, y), (x+w, y+h), color, thickness = pen_w)

cv2.imwrite("/Users/sugimotomamoru/python/結果画像/fanza3-1face.jpg", img)

