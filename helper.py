import re

#song_clean= re.sub('[a-zA-Z]+','',song)
#print(song_clean)



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


print(song_vec)