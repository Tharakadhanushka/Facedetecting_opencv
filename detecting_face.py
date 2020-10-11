import cv2

face_cascade = cv2.CascadeClassifier('face.xml')    #load the classifier

#img = cv2.imread('ab.jpg')       //selected image
vid = cv2.VideoCapture(0)
while True:
    _,img  = vid.read() 

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) #rgb images convert into gray scale images


    faces = face_cascade.detectMultiScale(gray, 1.1, 5) #grayscale, skill factor, minimum

    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x, y), (x+w, y+h), (0, 155, 0), 4)

    cv2.imshow('img', img)
    b = cv2.waitKey(30) & 0xff
    if b==27:
        break               #break the loop


vid.release() 