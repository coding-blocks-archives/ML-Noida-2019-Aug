import cv2
import numpy as np

cap = cv2.VideoCapture(0)
count = 0

classifier = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

while True:
    ret, frame = cap.read()

    if ret:
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        faces = classifier.detectMultiScale(gray)

        if len(faces) > 0:
            index = np.array(faces)[:, 2:].prod(axis=1).argmax()
            face = faces[0]
            x, y, w, h = face
            crop = gray[y:y+h, x:x+w]

            crop = cv2.resize(crop, (200, 200))
            cv2.imshow("Crop", crop)

        # cv2.imshow("Window", gray)



    key = cv2.waitKey(1)

    if ord('q') == 0xff & key:
        break

    if ord('c') == 0xff & key:
        cv2.imwrite("{}.png".format(count), frame)
        count += 1


cap.release()
cv2.destroyAllWindows()

