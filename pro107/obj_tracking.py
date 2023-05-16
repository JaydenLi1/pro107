import cv2

vid = cv2.VideoCapture('G:/Coding/python/pro107/footvolleyball.mp4')

tracker = cv2.TrackerCSRT_create()

ret, frame = vid.read()
bbox = cv2.selectROI("tracking", frame, False)
tracker.init(frame, bbox)

def drawBox(frame, bbox):
    x,y,w,h = int(bbox[0]), int(bbox[1]), int(bbox[2]), int(bbox[3]),
    cv2.rectangle(frame, (x,y), ((x+w), (y+h)), (255, 0, 255), 3)
    cv2.putText(frame, 'tracking', (75, 90), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0,255,0), 2)

while True:
    ret, frame = vid.read()
    success, bbox = tracker.update(frame)

    if success:
        drawBox(frame, bbox)
    else:
        cv2.putText(frame, 'Lost',(75,90), cv2.FONT_HERSHEY_DUPLEX, 0.7, (0,0,255), 2)

    cv2.imshow('Soccer', frame)

    key = cv2.waitKey(27)
    if key == 27:
        print('Closing')
        break
vid.release()
cv2.destroyAllWindows()  
