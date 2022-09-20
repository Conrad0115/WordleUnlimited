import random
f = open("words.txt", "r")
words = []

for line in f:
    strippedWord = line.strip()
    words.append(strippedWord)
    

def pickWord(words):
    word = random.choice(words)
    return word

def main(words):
    correctL = []
    placeL = []
    notInWord = []
    word = pickWord(words)
    word = word.lower()
    for i in range(6):
        win = False
        guess = input("write 5 letter word: ")
        print("guess: " + guess)
        if guess == word:
            print("correct!")
            win = True
            break
        for i in range(len(word)):
            if guess[i] == word[i]:
                if (guess[i] + ", letter # " + str(i+1)) not in placeL: 
                    placeL.append(guess[i] + ", letter # " + str(i+1))
            elif guess[i] in word:
                if guess[i] not in correctL and (guess[i] + ", letter # " + str(i+1)) not in placeL:
                    correctL.append(guess[i])
            else:
                if guess[i] not in notInWord:
                    notInWord.append(guess[i])
        
        print("correctly placed letters(s): " + str(placeL))
        print("incorrect placed letter(s) in word: " + str(correctL))
        print("letter(s) not in word: " + str(notInWord))
        print()
    print(word)
    return win
def game(words):
    if main(words) == True:
        print("congrats! you won!")
    else:
        print("sorry, you lose!")

game(words)
