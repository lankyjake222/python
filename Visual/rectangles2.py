from graphics import *

graphicswindow = GraphWin("Visualisation", 600, 600)

with open('data.txt','r') as file:
    while True:
        
        x1str = file.readline()
        if not x1str: break
        y1str = file.readline()
        x2str = file.readline()
        y2str = file.readline()

        x1 = float(x1str)*4
        y1 = float(y1str)*4
        x2 = float(x2str)*4
        y2 = float(y2str)*4
        
        #I am multiplying the data by 4, as it makes the graphics look a lot better an is easy to divide back to the original number.

        box = Rectangle(Point(x1,y1),Point(x2,y2))
        box.setOutline(color_rgb(112,46,178))
        box.draw(graphicswindow)

graphicswindow.getMouse()