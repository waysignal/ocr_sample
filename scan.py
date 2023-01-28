import cv2
import pytesseract
import random
import time 
import re


pytesseract.pytesseract.tesseract_cmd = r'/usr/bin/tesseract'

img_cv = cv2.imread(r'image.png')
print(img_cv.shape)



class PointsStore:
    def __init__(self):
        self.points = []

def mousePoints(event,x,y,flags,myPoints:PointsStore):
    global counter,point1,point2,counter2,circles,myColor
    
    if event == cv2.EVENT_LBUTTONDOWN:
        if counter==0:
            point1=int(x//scale),int(y//scale)
            counter +=1
            myColor = (random.randint(0,2)*200,random.randint(0,2)*200,random.randint(0,2)*200 )
        elif counter ==1:
            point2=int(x//scale),int(y//scale)
            myPoints.points.append([point1,point2])
            counter=0
        circles.append([x,y,myColor])
        counter2 += 1

def Crop(data_vec: list, roi:list) :
    for x,r in enumerate(roi):
        #img_crop = img_cv[170:205, 270:330 ]
        print(r[0][1], r[1][1])
        img_crop = img_cv[r[0][1]:r[1][1], r[0][0]:r[1][0]]
        while True: 
            cv2.imshow(str(x), img_crop)

            the_word = pytesseract.image_to_string(img_crop, config = '--psm 10').strip()
            
            if cv2.waitKey(1) & 0xFF == ord('s'):
                data_vec.append(the_word[0])
                print(the_word[0])
                break


scale = 4
points1 = PointsStore()
circles = []
counter = 0
counter2 = 0
point1=[]
point2=[]

img = img_cv
img = cv2.resize(img, (0, 0), None, scale, scale)


while True==False:
    # To Display points
    for x,y,color in circles:
        cv2.circle(img,(x,y),3,color,cv2.FILLED)
    cv2.imshow("Original Image ", img)
    cv2.setMouseCallback("Original Image ", mousePoints, points1)
    if cv2.waitKey(1) & 0xFF == ord('s'):
        #print(points1.points)
        roi = points1.points
        #print("roi",roi)
        break
#roi = [[(94, 74), (128, 96)], [(226, 108), (256, 130)], [(36, 180), (62, 210)], [(420, 180), (446, 204)]]
data_vec = ['y','m','c','a']
#Crop(data_vec, roi)
print(data_vec)
##^ completed char extractio and now in vec

song_vec= ["Young man, there's no need to feel down",
"I said, young man, pick yourself off the ground",
"I said, young man, 'cause you're in a new town",
"There's no need to be unhappy",
"Young man, there's a place you can go",
"I said, young man, when you're short on your dough",
"You can stay there, and I'm sure you will find",
"Many ways to have a good time",
"It's fun to stay at the 0",
"It's fun to stay at the 0",
"They have everything for you men to enjoy",
"You can hang out with all the boys",
"It's fun to stay at the 0",
"It's fun to stay at the 0",
"You can get yourself clean, you can have a good meal",
"You can do what ever you feel",
"Young man, are you listening to me?",
"I said, young man, what do you want to be?",
"I said, young man, you can make real your dreams",
"But you got to know this one thing",
"No man does it all by himself",
"I said, young man, put your pride on the shelf",
"And just go there, to the 0",
"I'm sure they can help you today",
"It's fun to stay at the 0",
"It's fun to stay at the 0",
"They have everything for you men to enjoy",
"You can hang out with all the boys",
"It's fun to stay at the 0",
"It's fun to stay at the 0",
"You can get yourself clean, you can have a good meal",
"You can do what ever you feel",
"Young man, I was once in your shoes",
"I said, I was down and out with the blues",
"I felt no man cared if I were alive",
"I felt the whole world was so tight",
"That's when someone came up to me",
"And said, young man, take a walk up the street",
"There's a place there called the 0",
"They can start you back on your way",
"It's fun to stay at the 0",
"It's fun to stay at the 0",
"They have everything for you men to enjoy",
"You can hang out with all the boys",
"0, it's fun to stay at the 0",
"Young man, young man, there's no need to feel down",
"Young man, young man, pick yourself off the ground",
"0, it's fun to stay at the 0",
"Young man, young man, are you listening to me",
"Young man, young man, what do you wanna be?",
"0, you'll find it at the 0",
"No man, young man, does it all by himself",
"Young man, young man, put your pride on the shelf",
"0, and just go to the 0",
"Young man, young man I was once in your shoes",
"Young man, young man I was down with the blues, 0"]


for row,words in enumerate(song_vec): 
    clean =  re.sub('[^a-zA-Z0]+','', words)
    song_vec[row] = clean

final_word = ''
for x in data_vec:
    final_word = final_word + x

for rows,words in enumerate(song_vec):
    song_vec[rows] = words.replace('0',final_word)
    song_vec[rows] = song_vec[rows].lower()

##^ vec is cleaned and upper cased ready to work with
print(song_vec)

import numpy as np
import pandas as pd

df = pd.DataFrame(columns=['row','character','value'])

values = {chr(i): i - 96 for i in range(ord("a"), ord("a") + 26 )}

for index, row in enumerate(song_vec):
    for element in row:
        df.loc[len(df)] = [index, element,values[element]]


print(df.head())

import statsmodels.api as sm
import statsmodels.formula.api as smf
import matplotlib.pyplot as plt

df = df.drop('character', axis=1)
model = smf.quantreg('value ~ row',
                     df).fit(q=0.5)
 

print(model.summary())
# define figure and axis
fig, ax = plt.subplots(figsize=(10, 8))
 

row = df['row'].to_numpy()
value = df['value'].to_numpy()
# get y values
y_line = lambda a, b: a + row
y = y_line(model.params['Intercept'],
           model.params['row'])
 
# Plotting data points with the help
# pf quantile regression equation
ax.plot(df['row'], y, color='black')
ax.scatter(row, value, alpha=.3)
ax.set_xlabel('row', fontsize=20)
ax.set_ylabel('value', fontsize=20)
 
# Save the plot
fig.savefig('quantile_regression.png')