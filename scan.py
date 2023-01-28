import cv2
import pytesseract
import random
import re


pytesseract.pytesseract.tesseract_cmd = r'/usr/bin/tesseract'

img_cv = cv2.imread(r'image.png')
print(img_cv.shape)
scale = 4
img = cv2.resize(img_cv, (0, 0), None, scale, scale)
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
        img_crop = img_cv[r[0][1]:r[1][1], r[0][0]:r[1][0]]
        while True: 
            cv2.imshow(str(x), img_crop)
            the_word = pytesseract.image_to_string(img_crop, config = '--psm 10').strip()
            if cv2.waitKey(1) & 0xFF == ord('s'):
                data_vec.append(the_word[0])
                print(the_word[0])
                break

points1 = PointsStore()
circles = []
counter = 0
counter2 = 0
point1=[]
point2=[]

while True:
    for x,y,color in circles:
        cv2.circle(img,(x,y),3,color,cv2.FILLED)
    cv2.imshow("Original Image ", img)
    cv2.setMouseCallback("Original Image ", mousePoints, points1)
    if cv2.waitKey(1) & 0xFF == ord('s'):
        roi = points1.points
        break

#roi = [[(94, 74), (128, 96)], [(226, 108), (256, 130)], [(36, 180), (62, 210)], [(420, 180), (446, 204)]]
data_vec = []
Crop(data_vec, roi)
print(data_vec)

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

song_vec_2 = ["Yahoo!",
"This is your celebration",
"Yahoo!",
"This is your celebration",
"Celebrate good times, come on",
"Let's celebrate",
"Celebrate good times, come on",
"Let's celebrate",
"There's a party going on right here",
"A celebration to last throughout the years",
"So bring your good times and your laughter too",
"We gonna celebrate your party with you, come on",
"Celebration",
"Let's all celebrate and have a good time",
"Celebration",
"We gonna celebrate and have a good time",
"It's time to come together",
"It's up to you",
"What's your pleasure",
"Everyone around the world, come on",
"Yahoo!",
"It's a celebration",
"Yahoo!",
"Celebrate good times, come on",
"It's a celebration",
"Celebrate good times, come on",
"Let's celebrate",
"There's a party going on right here",
"A dedication to last throughout the years",
"So bring your good times and your laughter too",
"We gonna celebrate your party with you",
"Come on now",
"Celebration",
"Let's all celebrate and have a good time, yeah, yeah",
"Celebration",
"We gonna celebrate and have a good time",
"It's time to come together",
"It's up to you",
"What's your pleasure",
"Everyone around the world, come on",
"Yahoo!",
"It's a celebration",
"Yahoo!",
"It's a celebration",
"Celebrate good times, come on",
"Let's celebrate, come on now",
"Celebrate good times, come on",
"Let's celebrate",
"We're gonna have a good time tonight",
"Let's celebrate, it's all right",
"We're gonna have a good time tonight",
"Let's celebrate, it's all right, baby",
"We're gonna have a good time tonight (Celebration)",
"Let's celebrate, it's all right",
"We're gonna have a good time tonight (Celebration)",
"Let's celebrate, it's all right",
"Yahoo!",
"Yahoo!",
"Celebrate good times, come on",
"Ooh, ooh, ooh, hoo",
"Celebrate good times, come on",
"It's a celebration",
"Celebrate good times, come on {Let's celebrate}",
"Come on and celebrate tonight",
"Celebrate good times, come on",
"'Cause everything's gonna be all right",
"Let's celebrate",
"Celebrate good times, come on {Let's celebrate}",
"Ooh, hoo, hoo",
"Celebrate good times, come on",
"Let's have a great time, celebrate",
"Celebrate good times, come on"]

song_vec.extend(song_vec_2)

for row,words in enumerate(song_vec): 
    clean =  re.sub('[^a-zA-Z0]+','', words)
    song_vec[row] = clean

final_word = ''
for x in data_vec:
    final_word = final_word + x

for rows,words in enumerate(song_vec):
    song_vec[rows] = words.replace('0',final_word)
    song_vec[rows] = song_vec[rows].lower()

print(song_vec)

import numpy as np
import pandas as pd

df = pd.DataFrame(columns=['row','row_length','character','value'])

values = {chr(i): i - 96 for i in range(ord("a"), ord("a") + 26 )}

for index, row in enumerate(song_vec):
    for element in row:
        df.loc[len(df)] = [index, len(row), element,values[element]]

print(df.head())

df2 = df.groupby(['row','row_length'])['value'].sum().reset_index()
print(df2.head())
df = df2.drop('row', axis=1)
print(df.head())

import statsmodels.api as sm
import statsmodels.formula.api as smf
import matplotlib.pyplot as plt
from statsmodels.regression.quantile_regression import QuantReg

mod = smf.quantreg('value ~ row_length', df)
res = mod.fit(q=0.5)
quantiles = np.arange(0.05, 0.96, 0.2)

def fit_model(q):
    res = mod.fit(q=q)
    return [q, res.params["Intercept"], res.params["row_length"]] + res.conf_int().loc[
        "row_length"
    ].tolist()

models = [fit_model(x) for x in quantiles]
models = pd.DataFrame(models, columns=["q", "a", "b", "lb", "ub"])
print(models)
fig, ax = plt.subplots(1,1,figsize=(6, 4))
 
row = df['row_length'].to_numpy()
value = df['value'].to_numpy()
get_y = lambda a, b: a + b * row

for i in range(models.shape[0]):
    y = get_y(models.a[i], models.b[i])
    ax.plot(row, y, linestyle="dotted", color="grey")

ax.plot(row, y, color='black')
ax.scatter(row, value, alpha=.2)
ax.set_xlabel('# of characters in lyric row', fontsize=10)
ax.set_ylabel('Summed value of lyric row', fontsize=10)
fig.savefig('quantile_regression_quantiles.png')

fig, ax = plt.subplots(1,1,figsize=(6, 4))
n = models.shape[0]
p1 = ax.plot(models.q, models.b, color="black", label="Quantile Reg.")
p2 = ax.plot(models.q, models.ub, linestyle="dotted", color="black")
p3 = ax.plot(models.q, models.lb, linestyle="dotted", color="black")
ax.set_ylabel(r"$\beta_{row_length}$")
ax.set_xlabel("Quantiles of the conditional value distribution")
ax.legend()
fig.savefig('quantile_regression.png')