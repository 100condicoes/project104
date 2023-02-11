import cv2

img = cv2.imread("solar-system.jpg")
cv2.putText(img,"Sol",(100,80), cv2.FONT_HERSHEY_COMPLEX, 2, (0,0,255))
cv2.putText(img,"Mercurio",(125,250), cv2.FONT_HERSHEY_COMPLEX, 0.5, (0,0,255))
cv2.putText(img,"Venus",(215,250), cv2.FONT_HERSHEY_COMPLEX, 0.5, (0,0,255))
cv2.putText(img,"Terra",(305,260), cv2.FONT_HERSHEY_COMPLEX, 0.5, (0,0,255))
cv2.putText(img,"Marte",(410,250), cv2.FONT_HERSHEY_COMPLEX, 0.5, (0,0,255))
cv2.putText(img,"Jupiter",(600,375), cv2.FONT_HERSHEY_COMPLEX, 0.5, (0,0,255))
cv2.putText(img,"Saturno",(735,110), cv2.FONT_HERSHEY_COMPLEX, 0.5, (0,0,255))
cv2.putText(img,"Urano",(1000,290), cv2.FONT_HERSHEY_COMPLEX, 0.5, (0,0,255))
cv2.putText(img,"Neturno",(1150,290), cv2.FONT_HERSHEY_COMPLEX, 0.5, (0,0,255))

cv2.imshow =("planetas", img)
cv2.waitKey(0)
cv2.imwrite("SYS.jpg", img)