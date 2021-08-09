# draw head and rest of body
# create a set of words to pick from
# ask user for guess and check if right
# make game loop
# check if win
# use linear search

import turtle as t

t.ht()
boxDrawer = t.Turtle()
finishGame = t.Turtle()
t.color("white")
t.Screen().bgcolor("black")

draw = True
xpos = "head"
ypos = "head"
incorLet = []
corLet = []
global headxpos
global headypos
global bodyxpos
global bodyypos
global human
global onePart
global found
global a

onePart = 0
word = "sandwich"

numCorrectGuess = 0

letter = t.Turtle()
letter.color("white")
letter.pu()
letter.ht()
letter.goto(-275, -175)
letter.pd()
# letter.forward(350)

spacesMidpoint = []

for i in range(len(word)):
    letter.forward((350 // len(word)) / 2)
    spacesMidpoint.append(letter.xcor())
    letter.forward((350 // len(word)) / 2)
    letter.pu()
    letter.fd(30)

    letter.pd()

# print(spacesMidpoint)

t.speed(4)


# main frame/base
def base():
    t.pu()
    # t.ht()
    t.goto(-200, -80)
    t.pd()
    t.forward(150)
    t.right(180)
    t.forward(100)
    t.right(90)
    t.forward(200)
    t.right(90)
    t.forward(100)
    t.right(90)
    t.forward(50)

    xpos = t.xcor()
    ypos = t.ycor()
    # print(xpos)
    # print(ypos)


base()


def head():
    t.right(90)
    t.circle(15)
    t.pu()
    t.left(90)
    t.forward(30)
    t.pd()

    headxpos = t.xcor()
    headypos = t.ycor()
    # print(headxpos)
    # print(headypos)


def body(draw):
    if draw == True:
        # t.goto(headxpos,headypos)
        t.forward(50)
        bodyxpos = t.xcor()
        bodyypos = t.ycor()
        # print("This is body " + str(bodyxpos))
        # print(bodyypos)
        tuple = (bodyxpos, bodyypos)
        return tuple
    else:
        bodyxpos = t.xcor()
        bodyypos = t.ycor()
        # print("This is body " + str(bodyxpos))
        tuple = (bodyxpos, bodyypos)
        return tuple


def arm1(bodyxpos, bodyypos):
    t.bk(35)
    t.left(75)
    t.forward(20)
    t.bk(20)
    # print("This is body " + str(bodyxpos))
    # print(bodyypos)
    # t.goto(bodyxpos, bodyypos)


def arm2(bodyxpos, bodyypos):
    t.right(145)
    t.fd(20)
    t.bk(20)


def leg1():
    t.setheading(270)
    t.fd(33)
    t.right(45)
    t.fd(25)
    t.back(25)


def leg2():
    t.left(90)
    t.fd(25)

    finishGame.speed(0)
    # finishGame.right(90)
    finishGame.ht()
    finishGame.pu()
    finishGame.pencolor("black")
    finishGame.goto(-275, 175)
    finishGame.begin_fill()
    for i in range(2):
        finishGame.fd(600)
        finishGame.right(90)
        finishGame.fd(300)
        finishGame.right(90)
    finishGame.end_fill()

    finishGame.goto(0, 0)
    finishGame.pencolor("white")
    finishGame.fillcolor("blue")
    finishGame.pd()
    finishGame.begin_fill()
    finishGame.write("Game Over!", move=False, align="center", font=("Comic Sans MS", 45, "bold"))
    finishGame.end_fill()


def boxText():
    boxDrawer.color("white")
    boxDrawer.pu()
    boxDrawer.ht()
    boxDrawer.goto(50, 120)

    boxDrawer.pd()
    for i in range(2):
        boxDrawer.fd(250)
        boxDrawer.right(90)
        boxDrawer.fd(200)
        boxDrawer.right(90)
    boxDrawer.right(90)
    boxDrawer.fd(40)
    boxDrawer.fillcolor("red")
    boxDrawer.write(" Incorrect letters:", move=False, align="left", font=("Comic Sans MS", 20, "normal"))
    boxDrawer.fd(40)


def writeIncorLet():
    boxDrawer.fillcolor("white")
    boxDrawer.begin_fill()
    boxDrawer.write(incorLet, move=False, align="left", font=("Comic Sans MS", 20, "bold"))


boxText()


def drawHangman(onePart):
    if onePart == 0:
        head()
        # onePart += 1
        # print(onePart)
    elif onePart == 1:
        body(draw)
        # onePart += 1
        # print()
    elif onePart == 2:
        # Check this part without parameters inside
        arm1(body(False)[0], body(False)[1])
        # onePart += 1
    elif onePart == 3:
        arm2(body(False)[0], body(False)[1])
    elif onePart == 4:
        leg1()
    elif onePart == 5:
        leg2()
        # onePart += 1


def search(array, recurNum, onePart):
    while word != corLet:
        userLetter = input("Enter your guess: ")
        found = False
        if recurNum == len(array):
            pass
        else:
            for i in range(0, len(array)):
                if (array[i] == userLetter):
                    # t.speed(0)
                    # print("The entered letter is present in the word.")
                    # print(array)
                    letter.pu()
                    letter.goto(spacesMidpoint[i], -165)
                    letter.pd()
                    letter.fillcolor("white")
                    letter.begin_fill()
                    letter.write(userLetter, move=False, align="center", font=("Comic Sans MS", 24, "normal"))
                    letter.end_fill()
                    corLet.append(userLetter)
                    found = True
                    pass
                    # this is where we are going to write out the letters
                elif (found != True) and (i == len(array) - 1):
                    incorLet.append(" " + userLetter)
                    # print(incorLet)
                    writeIncorLet()
                    drawHangman(onePart)
                    # type the letter
                if (found != True) and (i == len(array) - 1):
                    return search(array, recurNum + 1, onePart + 1)
    checkWin()


def checkWin():
    if word == corLet:
        finishGame.speed(0)
        # finishGame.right(90)
        finishGame.ht()
        finishGame.pu()
        finishGame.pencolor("black")
        finishGame.goto(-275, 175)
        finishGame.begin_fill()
        for i in range(2):
            finishGame.fd(600)
            finishGame.right(90)
            finishGame.fd(300)
            finishGame.right(90)
        finishGame.end_fill()

        finishGame.goto(0, 0)
        finishGame.pencolor("white")
        finishGame.fillcolor("blue")
        finishGame.pd()
        finishGame.begin_fill()
        finishGame.write("You Won!", move=False, align="center", font=("Comic Sans MS", 45, "bold"))
        finishGame.end_fill()


def main():
    search(word, 0, 0)


main()
