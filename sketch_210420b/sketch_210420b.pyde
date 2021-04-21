# Processing has many built in functions to draw colorful
# shapes very easily. Lets do a quick example:
def setup():
    # The size(width, height) function creates a window with
    # the specified with and height 
    size(800, 600)


def draw():
    # background() draws the color or image onto the window.
    # In this case the '#FFFFFF' is white
    background('#FFFFFF')
    
    # fill() sets the color. In this case, it's Blue
    # You can create custom colors using Tools->Color Selector
    fill('#0000FF')

    # ellipse() draws an ellipse that follows the mouse position
    # (mouseX and mouseY) with the following inputs:
    #         x,      y,   width, height
    ellipse(mouseX, mouseY,  100,   100)
    
    # The code below checks of the mouse was pressed and draws
    # a red ellipse over the blue one
    if mousePressed:
        fill('#FF0000')
        ellipse(mouseX, mouseY,  100,   100)
        

    # TODO: Add some other shapes with different sizes and colors
    if mousePressed:
        fill('#4EFF0A')
        rect(mouseX+10, mouseY+10, 100, 100)
        fill('#C703FF')
        triangle(mouseX+50, mouseY+50, mouseX+100, mouseY+100, mouseX+150,mouseY+50)
    
