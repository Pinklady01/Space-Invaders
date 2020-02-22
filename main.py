import turtle
import os
import math
import random


if __name__ == "__main__":
    #set the screen
    wn = turtle.Screen()
    wn.bgcolor("black")
    wn.title("Space Invaders")
    wn.bgpic("space_invaders_background.gif")

    #Register Shapes
    turtle.register_shape("invader.gif")
    turtle.register_shape("player.gif")

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

    #Set the score to 0
    score = 0

    #Draw the score
    score_pen = turtle.Turtle()
    score_pen.color("White")
    score_pen.penup()
    score_pen.setposition(boundarie_left + 10, -boundarie_down + 20)
    scorestring = "Score: %s" %score
    score_pen.write(scorestring, False, align="left", font=("Arial", 14, "normal"))
    score_pen.hideturtle()

    #Create the player turtle
    player = turtle.Turtle()
    player.color("blue")
    player.shape("player.gif")
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

    #Choose a number of enemies
    number_of_enemies = 5
    #Create an empty list of enemies
    enemies = []

    #Add enemies to the list
    for i in range(number_of_enemies):
        enemies.append(turtle.Turtle())
    for enemy in enemies:
        enemy.color("red")
        enemy.shape("invader.gif")
        enemy.penup()
        enemy.speed(0)
        x = random.randint(boundarie_left + 100, -boundarie_down - 50)
        y = random.randint(100,  -boundarie_down)
        enemy.setposition(x, y)

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
        if distance <= 20:
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
        for enemy in enemies:
        #Move the enemy
            x = enemy.xcor()
            x += enemyspeed
            enemy.setx(x)

            if enemy.xcor() > -boundarie_left - 50:
                #Move all the enemies down
                for e in enemies:
                    y = e.ycor()
                    y -= 40
                    e.sety(y)
                #change enemy direction
                enemyspeed *= -1

            if enemy.xcor() < boundarie_left + 50:
                # Move all the enemies down
                for e in enemies:
                    y = e.ycor()
                    y -= 40
                    e.sety(y)
                # change enemy direction
                enemyspeed *= -1

            # Check for a collision between the bullet and the enemy
            if isCollision(bullet, enemy):
                # Reset the bullet
                bullet.hideturtle()
                bulletstate = "ready"
                bullet.setposition(10, boundarie_down - 300)
                # Reset the enemy
                x = random.randint(boundarie_left + 100, -boundarie_down - 50)
                y = random.randint(100, -boundarie_down)
                enemy.setposition(x, y)
                #Update score
                score += 10
                scorestring = "Score: %s" % score
                score_pen.clear()
                score_pen.write(scorestring, False, align="left", font=("Arial", 14, "normal"))
                score_pen.hideturtle()


            # Set game over
            if isCollision(player, enemy):
                player.hideturtle()
                enemy.hideturtle()
                print("Game Over")
                break

        # Move the bullet
        y = bullet.ycor()
        y += bulletspeed
        bullet.sety(y)

        #Check to see if the bullet has gone to the top
        if bullet.ycor() > - boundarie_down - 20:
            bullet.hideturtle()
            bulletstate = "ready"








    turtle.mainloop()
    delay = input("Press enter to finish.")
