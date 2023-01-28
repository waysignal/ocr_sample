import cv2
import pytesseract
import random

pytesseract.pytesseract.tesseract_cmd = r'/usr/bin/tesseract'

#img_cv = cv2.imread(r'image.png')


#scale = 4
#circles = []
#counter = 0
#counter2 = 0
#point1=[]
#point2=[]
#myPoints = []
#myColor=[]
class PointsStore:
    def __init__(self):
        self.points = []

def mousePoints(event,x,y,flags,myPoints:PointsStore):
    
#    scale = 4
    #circles = []
    #counter = 0
    #counter2 = 0
    #point1=[]
    #point2=[]
    
    global counter,point1,point2,counter2,circles,myColor
    scale = 4
    
    myColor=[]
    if event == cv2.EVENT_LBUTTONDOWN:
        if counter==0:
            point1=int(x//scale),int(y//scale)
            counter +=1
            myColor = (random.randint(0,2)*200,random.randint(0,2)*200,random.randint(0,2)*200 )
        elif counter ==1:
            point2=int(x//scale),int(y//scale)
            
            #type = input('what is this')
            myPoints.points.append([point1,point2])
            print(myPoints)
            counter=0
        circles.append([x,y,myColor])
        counter2 += 1
    #return params
    

#img = img_cv
#img = cv2.resize(img, (0, 0), None, scale, scale)

#while True:
#    # To Display points
#    for x,y,color in circles:
#        cv2.circle(img,(x,y),3,color,cv2.FILLED)
#    cv2.imshow("Original Image ", img)
#    cv2.setMouseCallback("Original Image ", mousePoints)
#    if cv2.waitKey(1) & 0xFF == ord('s'):
#        print(myPoints)
#        break