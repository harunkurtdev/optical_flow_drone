import cv2

left = cv2.VideoCapture(2)
right = cv2.VideoCapture(2)

while(True):
    if not (left.grab() and right.grab()):
        print("No more frames")
        break

    try:
        
        _, leftFrame = left.retrieve()
        _, rightFrame = right.retrieve()
        
        
        cv2.imshow('left', leftFrame)
        cv2.imshow('right', rightFrame)

    except Exception:
        import time
        time.sleep(0.5)
        
        # pass
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

left.release()
right.release()
cv2.destroyAllWindows()