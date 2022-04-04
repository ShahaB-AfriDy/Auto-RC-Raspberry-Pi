import cv2.cv2 as cv2

# Stop Sign Cascade Classifier xml
# stop_sign = cv2.CascadeClassifier(r"E:\Python in Sublime\Projects\Self-Driving-Autonomous-Car-using-Open-CV-and-Python-Neural-Network-Overtaking-Raspberry-Pi-master\computer\cascade_xml\traffic_light.xml")
stop_sign = cv2.CascadeClassifier('Cascade_stop_sign.xml')

def Stop_Sign(Image,Box_Display = True):
    detect = False
    gray = cv2.cvtColor(Image, cv2.COLOR_BGR2GRAY)
    stop_sign_scaled = stop_sign.detectMultiScale(gray, 1.3, 5)
    for (x, y, w, h) in stop_sign_scaled:
        if Box_Display:
            stop_sign_rectangle = cv2.rectangle(img, (x, y),(x + w, y + h),(0, 255, 0), 3)
            stop_sign_text = cv2.putText(img=stop_sign_rectangle,
                                         text="Stop Sign",
                                         org=(x, y + h + 30),
                                         fontFace=cv2.FONT_HERSHEY_SIMPLEX,
                                         fontScale=0.5, color=(0, 0, 255),
                                         thickness=2, lineType=cv2.LINE_4)
        detect = True
    return detect


if __name__ == "__main__":
    cap = cv2.VideoCapture(0)

    while cap.isOpened():
        _, img = cap.read()
        Detect = Stop_Sign(img)
        if Detect:
            print(Detect)
        elif Detect==False:
            print(Detect)
        cv2.imshow("img", img)
        if cv2.waitKey(1) == 27:
            cap.release()
            cv2.destroyAllWindows()
            break