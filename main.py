import numpy as np
import cv2 as cv
import random as r

def mouse_event(event, x, y, flags, param):
    if event == cv.EVENT_LBUTTONDOWN:
        param[0] = True
        param[1] = (x, y)
    elif event == cv.EVENT_LBUTTONUP:
        param[0] = False
    elif event == cv.EVENT_MOUSEMOVE and param[0]:
        param[1] = (x, y)

img_arr = np.fromfile("./data/test.png", np.uint8)
img = cv.imdecode(img_arr, cv.IMREAD_COLOR)

if img is not None:
    mouse_state = [False, (-1, -1)]
    cv.namedWindow("Pick and Delete")
    cv.setMouseCallback("Pick and Delete", mouse_event, mouse_state)

    while True:
        mouse_click, mouse_xy = mouse_state

        if mouse_click:
            x, y = mouse_xy
            target = img[y][x]
            print("Pick Color : ", target)

            img[np.where((img == target).all(axis = 2))] = [r.randint(0, 255), r.randint(0, 255), r.randint(0, 255)]


        cv.imshow("Pick and Delete", img)

        key = cv.waitKey(1)
        if key == 27:
            cv.imwrite("./result/test_result.png", img)
            break

    cv.destroyAllWindows()