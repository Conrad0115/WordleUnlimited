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
    for i in range(5):
        win = False
        guess = input("write 5 letter word")
        print("guess: " + guess)
        if guess == word:
            print("correct!")
            win = True
            break
        for i in range(len(word)):
            if guess[i] == word[i].lower():
                if guess[i] not in placeL: 
                    placeL.append(guess[i])
            elif guess[i] in word.lower():
                if guess[i] not in correctL:
                    correctL.append(guess[i])
            else:
                if guess[i] not in notInWord:
                    notInWord.append(guess[i])
        
        print("correctly placed letters(s): " + str(placeL))
        print("incorrect placed letter(s) in word: " + str(correctL))
        print("letter(s) not in word: " + str(notInWord))
        print()
    print("the word was: " + word)
    return win
def game(words):
    if main(words) == True:
        print("congrats! you won!")
    else:
        print("sorry, you lose!")
       

game(words)
