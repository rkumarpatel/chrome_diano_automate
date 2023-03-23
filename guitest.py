import pyautogui
from PIL import Image, ImageGrab
import time
import cv2
import numpy as np
#from numpy import asarray


def hit(key):
    #pyautogui.keyDown(key)
    pyautogui.press(key)
    return

def isCollide(data):

    for i in range(300, 415):
        for j in range(410, 563):
            if data[i, j] < 100:
                hit("down")
                return

    for i in range(310, 415):
        for j in range(563, 650):
            if data[i, j] < 100:
                hit("up")
                return



def printRectangle():

    image = ImageGrab.grab().convert('L')
    data = image.load()

    for i in range(300, 415):
        for j in range(410, 563):
            data[i, j] = 150

    for i in range(300, 320):
        for j in range(650, 680):
            data[i, j] = 0

    image.show()


if __name__ == "__main__":

    # Specify resolution
    resolution = (1920, 1080)

    # Specify video codec
    codec = cv2.VideoWriter_fourcc(*"XVID")

    # Specify name of Output file
    filename = "Recording.avi"

    # Specify frames rate. We can choose any
    # value and experiment with it
    fps = 60.0

    # Creating a VideoWriter object
    out = cv2.VideoWriter(filename, codec, fps, resolution)

    # Create an Empty window
    cv2.namedWindow("Live", cv2.WINDOW_NORMAL)

    # Resize this window
    cv2.resizeWindow("Live", 480, 270)

    time.sleep(5)
    hit("up")
    while True:
        #pyautogui.displayMousePosition()
        #pyautogui.keyDown('down')
        img = ImageGrab.grab()
        frame = np.array(img)
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        out.write(frame)
        image = ImageGrab.grab().convert('L')
        data = image.load()
        isCollide(data)
            #pyautogui.press('up',presses=5)
        #printRectangle()
            # Stop recording when we press 'q'
        if cv2.waitKey(1) == ord('q'):
            break
    out.release()
    cv2.destroyAllWindows()
