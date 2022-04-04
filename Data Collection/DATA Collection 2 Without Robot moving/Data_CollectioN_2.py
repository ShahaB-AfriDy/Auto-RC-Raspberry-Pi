
import cv2.cv2 as cv2
from datetime import datetime
import os
import Util



Dir = os.getcwd()+'\\'+Util.Create_Dir()
# ------------------------------------------------------------------
CameraBrightness = 100
ModuelVal = 10 # save every iTh Frame to avoid Repetition
Min_Blur = 250  # same value means more blurriness present


Video = cv2.VideoCapture(0)
Video.set(3,320)
Video.set(4,120)
Video.set(10,CameraBrightness)




def Main():
    save_count = 0
    count = 0
    while Video.isOpened():
        Ret_True ,Frame = Video.read()

        Image = cv2.cvtColor(Frame,cv2.COLOR_BGR2GRAY)
        blur = cv2.Laplacian(Image,cv2.CV_64F).var()
        if blur > Min_Blur and count % ModuelVal == 0:
            Time_Now = datetime.now()
            File_Name = Dir + f'\\{int(blur)}_' + Time_Now.strftime('%H_%M_%S') + '.jpg'
            cv2.imwrite(File_Name,Image)
            save_count += 1
            print("Saved: -->> ",save_count)
        count +=1
        cv2.imshow("Frame",Frame)
        if cv2.waitKey(1) == 27:
            break


    Video.release()
    cv2.destroyAllWindows()

    print("Total Images->>>>>>>> ",len(os.listdir(Dir)))
    print("Total Frame-->>>>>>>> ",save_count)

if __name__ == "__main__":
    Main()