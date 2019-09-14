import cv2

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()

    if ret:
        cv2.imshow("Window", frame)

    key = cv2.waitKey(1)

    # if ord('q') == 0xff & key:
    #     break

cap.release()
cv2.destroyAllWindows()

