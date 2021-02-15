import cv2
img1 = cv2.imread('/Users/sugimotomamoru/python/glasspicture/DSC_0022.JPG')
img2 = cv2.imread('/Users/sugimotomamoru/python/glasspicture/1608088589000.jpg')

img1 = cv2.resize(img1, img2.shape[1::-1])

img = cv2.addWeighted(img1, 0.5, img2, 0.5, 0)

cv2.imshow('image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
