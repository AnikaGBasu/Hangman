# draw head and rest of body
# create a set of words to pick from
# ask user for guess and check if right
# make game loop
# check if win
# use binary search to check letters (ascii)

import turtle as t

draw = True

xpos = "head"
ypos = "head"
global headxpos
global headypos
global bodyxpos
global bodyypos
global human

word = "puppy"

numCorrectGuess = 0

letter = t.Turtle()
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


def arms(bodyxpos, bodyypos):
    t.bk(35)
    t.left(75)
    t.forward(20)
    t.bk(20)
    t.right(145)
    t.fd(20)
    t.bk(20)
    # print("This is body " + str(bodyxpos))
    # print(bodyypos)
    # t.goto(bodyxpos, bodyypos)


def legs():
    t.right(90)
    t.fd(25)


'''
t.st()
t.speed(4)
base()
head()
print("The tuple is " + str(body()))
arms(body()["head"],body()[1])
legs()
'''


def search(array, userLetter, k):
    j = 0
    if k == len(array):
        pass
    else:
        for i in range(0, len(array)):
            if (array[i] == userLetter):
                print("The entered letter is present in the word.")
                print(array)
                letter.pu()
                letter.goto(spacesMidpoint[i], -165)
                letter.pd()
                letter.write(userLetter, move=False, align="center", font=("Arial", 24, "normal"))
                search(array, userLetter, k + 1)
                break
                # this is where we are going to write out the letters
            else:
                if j == 0:
                    head()
                    j += 1
                    print(j)
                elif j == 1:
                    body(draw)
                    j += 1
                elif j == 2:
                    # Check this part without parameters inside
                    arms(body(False)[0], body(False)[1])
                    j += 1
                elif j == 3:
                    legs()
                    j += 1
                    # type the letter
        return -1


def main():
    while len(word) != 0:
        userLetter = input("Enter your guess: ")
        search(word, userLetter, 0)


if __name__ == '__main__':
    main()
