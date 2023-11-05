import cv2
planetImg=cv2.imread("solar-system.jpg")
cv2.putText(planetImg,
           "sun",
           (20,300),
           cv2.FONT_HERSHEY_COMPLEX,
           0.5,
           (255,0,255)
)

cv2.putText(planetImg,
           "mercury",
           (20,300),
           cv2.FONT_HERSHEY_COMPLEX,
           0.5,
           (255,0,255)
)

cv2.putText(planetImg,
           "venus",
           (29,367),
           cv2.FONT_HERSHEY_COMPLEX,
           0.5,
           (255,,255)
)

cv2.putText(planetImg,
           "earth",
           (35,399),
           cv2.FONT_HERSHEY_COMPLEX,
           0.5,
           (255,0,255)
)

cv2.putText(planetImg,
           "mars",
           (45,440),
           cv2.FONT_HERSHEY_COMPLEX,
           0.5,
           (255,0,255)
)

cv2.putText(planetImg,
           "jupiter",
           (55,460),
           cv2.FONT_HERSHEY_COMPLEX,
           0.5,
           (255,0,255)
)

cv2.putText(planetImg,
           "saturn",
           (65,490),
           cv2.FONT_HERSHEY_COMPLEX,
           0.5,
           (255,0,255)
)


cv2.putText(planetImg,
           "neptune",
           (75,520),
           cv2.FONT_HERSHEY_COMPLEX,
           0.5,
           (255,0,255)
)

cv2.putText(planetImg,
           "uranus",
           (95,570),
           cv2.FONT_HERSHEY_COMPLEX,
           0.5,
           (255,0,255)
)



cv2.imshow("result",planetImg)
cv2.imwrite("Solar_systemwithname.jpg",planetImg)      
cv2.waitKey(0)