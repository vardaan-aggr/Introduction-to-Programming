import random
words=[
    "Apple", "Beach", "Brain", "Bread", "Brush", "Chair", "Chest", "Chord", "Click", "Clock", 
    "Cloud", "Dance", "Diary", "Drink", "Earth", "Flute", "Fruit", "Ghost", "Grape", "Green", 
    "Happy", "Heart", "House", "Juice", "Light", "Money", "Music", "Party", "Pizza", "Plant", 
    "Radio", "River", "Salad", "Sheep", "Shoes", "Smile", "Snack", "Snake", "Spice", "Spoon", 
    "Storm", "Table", "Toast", "Tiger", "Train", "Water", "Whale", "Wheel", "Woman", "World", "Write", "Youth"
]

gess_word=words[random.randint(0,49)]

print(gess_word)  #can un comment to see the word                            imp imp

your_guess=(input()).capitalize()
count=0
new_word=[]
while count <=5:#take 5 as one guess is take above
    if your_guess==gess_word:
        print ("correct guess",gess_word)
        break
    else:
        count+=1
        if your_guess[0]==gess_word[0]:new_word.append(your_guess[0])
        else:new_word.append("_")
        if your_guess[1]==gess_word[1]:new_word.append(your_guess[1])
        else:new_word.append("_")
        if your_guess[2]==gess_word[2]:new_word.append(your_guess[2])
        else:new_word.append("_")
        if your_guess[3]==gess_word[3]:new_word.append(your_guess[3])
        else:new_word.append("_")
        if your_guess[4]==gess_word[4]:new_word.append(your_guess[4])
        else:new_word.append("_")
        print ("".join(new_word))
        your_guess=(input()).capitalize()
        new_word=[]
