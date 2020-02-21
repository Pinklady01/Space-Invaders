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
    player.setposition(0, boundarie_down + 50)
    player.setheading(90)

    playerspeed = 15
    #Create an enemy
    enemy = turtle.Turtle()
    enemy.color("red")
    enemy.shape("circle")
    enemy.penup()
    enemy.speed(0)
    enemy.setposition(boundarie_left + 100, -boundarie_down - 50)

    enemyspeed = 2


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


    #Main game loop
    while True:
        #Move the enemy
        x = enemy.xcor()
        x += enemyspeed
        enemy.setx(x)

        if enemy.xcor() > -boundarie_left - 20:
            y = enemy.ycor()
            y -= 40
            enemyspeed *= -1
            enemy.sety(y)

        if enemy.xcor() < boundarie_left + 20:
            y = enemy.ycor()
            y -= 40
            enemyspeed *= -1
            enemy.sety(y)




    turtle.mainloop()
    delay = input("Press enter to finish.")
