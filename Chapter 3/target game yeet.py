def hit_the_target():
    
    # hit_the_target accepts no arguments
    # asks user for the projectile's force and angle
    # shoots projectile and checks if it hit the target
    
    import turtle
    
    # named constants
    
    SCREEN_WIDTH = 600
    SCREEN_HEIGHT = 600
    TARGET_LEFT_X = 100
    TARGET_LEFT_Y = 250
    TARGET_WIDTH = 25
    FORCE_FACTOR = 30
    PROJECTILE_SPEED = 1
    NORTH = 90
    SOUTH = 270
    EAST = 0
    WEST = 180
    
    # set up the turtle window\
    turtle.clear()
    turtle.setup(SCREEN_WIDTH, SCREEN_HEIGHT)
    turtle.speed(PROJECTILE_SPEED)
    turtle.shape('turtle')
    
    # draw the target
    
    turtle.hideturtle()
    turtle.speed(0)
    turtle.penup()
    turtle.goto(TARGET_LEFT_X, TARGET_LEFT_Y)
    turtle.pendown()
    turtle.setheading(EAST)
    turtle.forward(TARGET_WIDTH)
    turtle.setheading(NORTH)
    turtle.forward(TARGET_WIDTH)
    turtle.setheading(WEST)
    turtle.forward(TARGET_WIDTH)
    turtle.setheading(SOUTH)
    turtle.forward(TARGET_WIDTH)
    turtle.penup()
    
    # ask the user
    
    projectile_angle = float(input('''Enter the projectile's angle: '''))
    launch_force = float(input('Enter the launch force (1-10): '))
    
    
    # launch time
    
    turtle.goto(0,0)
    turtle.setheading(projectile_angle)
    turtle.pendown()
    turtle.forward(FORCE_FACTOR * launch_force)
    
    # figure out if it hit the target
    
    x = round(turtle.xcor(), 0)
    y = round(turtle.ycor(), 0)
    
    if x in range(TARGET_LEFT_X, 125) and y in range(TARGET_LEFT_Y, (TARGET_LEFT_Y + 25)):
        print('Target hit!')
    
    else:
        print('Here are some hints:')
        
        if y < TARGET_LEFT_Y:
            print('- Try using more power')
            
        if y > TARGET_LEFT_Y:
            print('- Try using less power')