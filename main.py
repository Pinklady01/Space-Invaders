import turtle
import os
import math


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

    #Create the player's bullet
    bullet = turtle.Turtle()
    bullet.color("yellow")
    bullet.shape("triangle")
    bullet.penup()
    bullet.speed(0)
    bullet.setheading(90)
    bullet.shapesize(0.5, 0.5)
    bullet.hideturtle()

    bulletspeed = 30
    #Define bullet state
    #ready - ready to fire
    #fire - bullet is firing
    bulletstate = "ready"

    #Create an enemy
    enemy = turtle.Turtle()
    enemy.color("red")
    enemy.shape("circle")
    enemy.penup()
    enemy.speed(0)
    enemy.setposition(boundarie_left + 100, -boundarie_down - 50)

    enemyspeed = 10


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
        if x > - boundarie_left - 20:
            x = - boundarie_left - 20
        player.setx(x)


    def fire_bullet():
        #declare bulletstate as global if it needs change
        global bulletstate
        if bulletstate == "ready":
            bulletstate = "fire"
            #Move the bullet just above the player
            x = player.xcor()
            y = player.ycor() + 10
            bullet.setposition(x, y)
            bullet.showturtle()

    def isCollision(t1, t2):
        distance = math.sqrt(math.pow(t1.xcor() - t2.xcor(), 2) + math.pow(t1.ycor() - t2.ycor(), 2))
        if distance <= 15:
            return True
        else:
            return False

    #Create keyboard bindings
    turtle.listen()
    turtle.onkey(move_left, "Left")
    turtle.onkey(fire_bullet, "space")
    turtle.onkey(move_right, "Right")

    #Main game loop
    while True:
        #Move the enemy
        x = enemy.xcor()
        x += enemyspeed
        enemy.setx(x)

        if enemy.xcor() > -boundarie_left - 40:
            y = enemy.ycor()
            y -= 40
            enemyspeed *= -1
            enemy.sety(y)

        if enemy.xcor() < boundarie_left + 40:
            y = enemy.ycor()
            y -= 40
            enemyspeed *= -1
            enemy.sety(y)

        # Move the bullet
        y = bullet.ycor()
        y += bulletspeed
        bullet.sety(y)

        #Check to see if the bullet has gone to the top
        if bullet.ycor() > - boundarie_down - 20:
            bullet.hideturtle()
            bulletstate = "ready"

        #Check for a collision between the bullet and the enemy
        if isCollision(bullet, enemy):
            #Reset the bullet
            bullet.hideturtle()
            bulletstate = "ready"
            bullet.setposition(0, boundarie_down-300)
            #Reset the enemy
            enemy.setposition(boundarie_left + 100, -boundarie_down - 50)

            #Set game over
        if isCollision(player, enemy):
            player.hideturtle()
            enemy.hideturtle()
            print("Game Over")
            break




    turtle.mainloop()
    delay = input("Press enter to finish.")
