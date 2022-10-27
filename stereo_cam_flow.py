import cv2

left = cv2.VideoCapture(1)
# right = cv2.VideoCapture(2)

while(True):

    try:
        # if not (left.grab() and right.grab()):
        #     print("No more frames")
        #     break
            
        _, leftFrame = left.retrieve()
        # _, rightFrame = right.retrieve()
        
        print(leftFrame)
        cv2.imshow('left', leftFrame)
        # cv2.imshow('right', rightFrame)

    except Exception:
        import time
        time.sleep(0.5)
        
        # pass
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

left.release()
# right.release()
cv2.destroyAllWindows()