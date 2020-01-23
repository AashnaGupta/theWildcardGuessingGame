from Tkinter import *
from PIL import Image, ImageTk
import threading

window = Tk()
window.title("The Wildcard Guessing Game")
window.geometry("750x500")
currentLevel = 1
hint = 0
answer = 0
MAX_LEVELS = 10
MAX_TIME = 20
stopClock = False

WildcardGuessingGameDict = {
    1: ["A Toy", "BEACH BALL"],
    2: ["It flies in the wind", "KITE"],
    3: ["A building for people to live in", "HOUSE"],
    4: ["A frozen treat", "ICE CREAM"],
    5: ["A cartoon created by Walt Disney", "MICKEY MOUSE"],
    6: ["A character from Despecable Me", "MINION"],
    7: ["Sssssslither!", "SNAKE"],
    8: ["An instrument", "DRUMS"],
    9: ["One of the world's larget companies", "GOOGLE"],
    10: ["A candymaker who owns a chocolate factory", "WILLY WONKA"]
}

def onHint():
    imageInfo = WildcardGuessingGameDict.get(currentLevel)
    imageHint = imageInfo[0]
    hintLbl["text"] = imageHint

def onNext():
    global currentLevel
    global guessBoxEntry
    global photo
    global timer
    global stopClock
    currentLevel = currentLevel + 1
    levelLbl["text"] = "Level: " + str(currentLevel)
    hintLbl["text"] = ""
    answerLbl["text"] = ""
    guessBoxEntry.delete(0, END)
    nextBtn["state"] = DISABLED
    submitBtn["state"] = NORMAL
    hintBtn["state"] = NORMAL
    image = Image.open(str(currentLevel) + ".png")
    image = image.resize((250, 250), Image.ANTIALIAS)
    photo = ImageTk.PhotoImage(image)
    imageLabel = Label(image=photo)
    imageLabel.grid(row=1, column=2)
    timer = threading.Timer(MAX_TIME, onTimer)
    timer.start()
    stopClock = False
    countdown(MAX_TIME)   


def onSubmit():
    global timer
    global stopClock
    userGuess = guessBoxEntry.get()
    if userGuess == "":
        answerLbl["fg"] = "orange"
        answerLbl["text"] = "Please type your answer or take a hint"
        return

    timer.cancel()
    stopClock = True
    submitBtn["state"] = DISABLED
    hintBtn["state"] = DISABLED
    userGuess = userGuess.upper()
    imageInfo = WildcardGuessingGameDict.get(currentLevel)
    imageName = imageInfo[1]

    guessBoxEntry.delete(0, END)

    if userGuess == imageName:
        answerLbl["fg"] = "green"
        answerLbl["text"] = "Correct! This is a " + userGuess.lower()
        nextBtn["state"] = NORMAL
        hintBtn["state"] = DISABLED
        if currentLevel == MAX_LEVELS:
            gameOverLbl["fg"] = "red"
            gameOverLbl["text"] = "GAME OVER"
            nextBtn["state"] = DISABLED
            hintBtn["state"] = DISABLED
            submitBtn["state"] = DISABLED

    else:
        answerLbl["fg"] = "red"
        answerLbl["text"] = "Sorry! This is a " + imageName.lower()


def initialState():
    pass

def onTimer():
    submitBtn["state"] = DISABLED
    hintBtn["state"] = DISABLED
    answerLbl["fg"] = "red"
    answerLbl["text"] = "TIME'S UP"

image = Image.open(str(currentLevel)+".png")
image = image.resize((250, 250), Image.ANTIALIAS)
photo = ImageTk.PhotoImage(image)
imageLabel = Label(image=photo)
imageLabel.grid(row = 1, column = 2)

levelLbl = Label(window, text ="Level: " + str(currentLevel), font ="Arial 24")
levelLbl.grid(row = 0, column = 0)

timerLbl = Label(window, text ="Timer:", font ="Arial 24")
timerLbl.grid(row = 0, column = 4)


hintLbl = Label(window, text ="", font ="Arial 24")
hintLbl.grid(row = 14, column = 2)

answerLbl = Label(window, text ="", font ="Arial 24")
answerLbl.grid(row = 12, column = 2)

gameOverLbl = Label(window, text ="", font ="Arial 24")
gameOverLbl.grid(row = 16, column = 2)

guessBoxEntry = Entry(window, width = 50)
guessBoxEntry.grid(row = 10, column = 2)

directionsLbl = Label(window, text ="What is this object?", font ="Arial 24")
directionsLbl.grid(row = 0, column = 2)

timer2Lbl = Label(window, text = "", font = "Arial 24", fg = "red")
timer2Lbl.grid(row = 0, column = 5)

submitBtn = Button(window, text ="Submit", font ="Arial 24", command = onSubmit)
submitBtn.grid(row = 11, column = 2)

nextBtn = Button(window, text ="Next >", font ="Arial 24", state = DISABLED, command = onNext)
nextBtn.grid(row = 10, column = 4)                                        

hintBtn = Button(window, text = "Hint", command = onHint, font = "Arial 24")
hintBtn.grid(row = 13, column = 2)

timer = threading.Timer(MAX_TIME, onTimer)
timer.start()

def countdown(remainder = None):
    global remaining
    if remainder is not None:
        remaining = remainder
         
    if remaining <= 0:
        timer2Lbl.configure(text="0")
    else:
        timer2Lbl.configure(text="%d" % remaining)
        remaining = remaining - 1
        if stopClock == False:
            window.after(1000, countdown)

remaining = 0
countdown(MAX_TIME)

window.mainloop()