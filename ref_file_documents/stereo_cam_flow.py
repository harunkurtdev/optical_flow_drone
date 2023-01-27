import cv2

left = cv2.VideoCapture(1,cv2.CAP_DSHOW)
right = cv2.VideoCapture(2,cv2.CAP_DSHOW)

while(True):

    try:
        
        # left.read()
        # if not (left.grab() and right.grab()):
        #     print("No more frames")
        #     break
            
        leftgrab, leftFrame = left.read()
        cv2.waitKey(25)
        rightgrab, rightFrame = right.read()
        print(leftgrab,rightgrab)
        if not (leftgrab and rightgrab):
            print("No more frames")
            break
        # print(leftFrame)
        cv2.imshow('left', leftFrame)
        cv2.imshow('right', rightFrame)

    except Exception:
        import time
        time.sleep(0.5)
        
        # pass
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

left.release()
# right.release()
cv2.destroyAllWindows()