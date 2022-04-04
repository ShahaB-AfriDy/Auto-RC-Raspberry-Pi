import cv2.cv2 as cv2
import math
class DistanceToCamera(object):

    def __init__(self):
        # camera params
        self.alpha = 8.0 * math.pi / 180
        self.v0 = 119.865631204
        self.ay = 332.262498472

    def calculate(self, v, h, x_shift, image):
        # compute and return the distance from the target point to the camera
        d = h / math.tan(self.alpha + math.atan((v - self.v0) / self.ay))
        if d > 0:
            cv2.putText(image, "%.1fcm" % d,
                        (image.shape[1] - x_shift, image.shape[0] - 20), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0),
                        2)
        return d


class ObjectDetection(object):

    def __init__(self):
        self.red_light = False
        self.green_light = False
        self.yellow_light = False

    def detect(self, cascade_classifier, gray_image, image):
        # y camera coordinate of the target point 'P'
        v = 0
        # minimum value to proceed traffic light state validation
        threshold = 150
        # detection
        cascade_obj = cascade_classifier.detectMultiScale(
            gray_image,
            scaleFactor=1.1,
            minNeighbors=5,
            minSize=(30, 30))
        # draw a rectangle around the objects
        for (x_pos, y_pos, width, height) in cascade_obj:
            cv2.rectangle(image, (x_pos + 5, y_pos + 5), (x_pos + width - 5, y_pos + height - 5), (255, 0, 255), 2)
            v = y_pos + height - 5
            # print(x_pos+5, y_pos+5, x_pos+width-5, y_pos+height-5, width, height)

            # stop sign
            if width / height == 1:
                cv2.putText(image, 'STOP', (x_pos, y_pos - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)

            # traffic lights
            else:
                roi = gray_image[y_pos + 10:y_pos + height - 10, x_pos + 10:x_pos + width - 10]
                mask = cv2.GaussianBlur(roi, (25, 25), 0)
                (minVal, maxVal, minLoc, maxLoc) = cv2.minMaxLoc(mask)

                # check if light is on
                if maxVal - minVal > threshold:
                    cv2.circle(roi, maxLoc, 5, (255, 0, 255), 2)

                     # Red light
                    if 1.0 / 8 * (height - 30) < maxLoc[1] < 4.0 / 8 * (height - 30):
                        cv2.putText(image, 'Red', (x_pos + 5, y_pos - 5), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)
                        self.red_light = True

                    # Green light
                    elif 5.5 / 8 * (height - 30) < maxLoc[1] < height - 30:
                        cv2.putText(image, 'Green', (x_pos + 5, y_pos - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0),2)
                        self.green_light = True

                    # yellow light
                    # elif 4.0/8*(height-30) < maxLoc[1] < 5.5/8*(height-30):
                    #    cv2.putText(image, 'Yellow', (x_pos+5, y_pos - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 255), 2)
                    #    self.yellow_light = True
        return v


if __name__ == "__main__":
    # h1: stop sign
    h1 = 15.5 - 10  # cm
    # h2: traffic light
    h2 = 15.5 - 10

    stop_flag = False
    stop_sign_active = True

    obj_detection = ObjectDetection()

    # cascade classifiers
    stop_cascade = cv2.CascadeClassifier(r'E:\Python in Sublime\Projects\Self-Driving-Autonomous-Car-using-Open-CV-and-Python-Neural-Network-Overtaking-Raspberry-Pi-master\computer\cascade_xml\stop_sign.xml')
    light_cascade = cv2.CascadeClassifier(r'E:\Python in Sublime\Projects\Self-Driving-Autonomous-Car-using-Open-CV-and-Python-Neural-Network-Overtaking-Raspberry-Pi-master\computer\cascade_xml\traffic_light.xml')

    d_to_camera = DistanceToCamera()
    d_stop_sign = 25
    d_light = 25

    stop_start = 0  # start time when stop at the stop sign
    stop_finish = 0
    stop_time = 0
    drive_time_after_stop = 0
    try:
            Cap = cv2.VideoCapture(0)
            while True:
                _,Image  = Cap.read()
                # object detection
                gray = cv2.cvtColor(Image,cv2.COLOR_BGR2GRAY)
                v_param1 = obj_detection.detect(stop_cascade, gray, Image)
                v_param2 = obj_detection.detect(light_cascade, gray, Image)
                # distance
                if v_param1 > 0 or v_param2 > 0:
                    d1 = d_to_camera.calculate(v_param1, h1, 300, Image)
                    d2 = d_to_camera.calculate(v_param2, h2, 100, Image)
                    d_stop_sign = d1
                    d_light = d2
                elif 0 < d_stop_sign < 25 and stop_sign_active:
                    print("Stop sign ahead")
                    # stop for 5 seconds
                    if stop_flag is False:
                        stop_start = cv2.getTickCount()
                        stop_flag = True
                    stop_finish = cv2.getTickCount()

                    # 5 seconds later, continue driving
                    if stop_time > 5:
                        print("Waited for 5 seconds")
                        stop_flag = False
                        stop_sign_active = False
                elif 0 < d_light < 30:
                    # print("Traffic light ahead")
                    if obj_detection.red_light:
                        print("Red light")
                    elif obj_detection.green_light:
                        print("Green light")
                        pass
                    elif obj_detection.yellow_light:
                        print("Yellow light flashing")
                        pass
                    d_light = 30
                    obj_detection.red_light = False
                    obj_detection.green_light = False
                    obj_detection.yellow_light = False
                else:
                    stop_start = cv2.getTickCount()
                    d_stop_sign = 25

                cv2.imshow("Image",Image)
                if cv2.waitKey(1) == 27:
                    cv2.destroyAllWindows()
                    break
    finally:
        print("End!!!")