import turtle
import os


if __name__ == "__main__":
    #set the screen
    wn = turtle.Screen()
    wn.bgcolor("black")
    wn.title("Space Invaders")

    #draw border
    border_pen = turtle.Turtle()
    border_pen.speed(0)
    border_pen.color("White")
    border_pen.penup()
    boundarie_down = -300
    boundarie_left = -300
    border_pen.setposition(boundarie_left, boundarie_down)
    border_pen.pendown()
    border_pen.pensize(2)
    for side in range(4):
        border_pen.fd(600)
        border_pen.lt(90)
    border_pen.hideturtle()

    #Create the player turtle
    player = turtle.Turtle()
    player.color("blue")
    player.shape("triangle")
    player.penup()
    player.speed(0)
    player.setposition(0, -250)
    player.setheading(90)

    playerspeed = 15

    # move left and right
    def move_left():
        x = player.xcor()
        x -= playerspeed
        if x < boundarie_left + 20:
            x = boundarie_left + 20
        player.setx(x)


    def move_right():
        x = player.xcor()
        x += playerspeed
        if x > -boundarie_left - 20:
            x = -boundarie_left - 20
        player.setx(x)


    #Create keyboard bindings
    turtle.listen()
    turtle.onkey(move_left, "Left")
    turtle.onkey(move_right, "Right")
    turtle.mainloop()

    delay = input("Press enter to finish.")
