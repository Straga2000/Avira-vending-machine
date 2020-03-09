from utilities import *

# GLOBAL FUNCTIONS


def increment(point, x=0, y=0):
    return Point(point.x + x, point.y + y)

# CONSTANTS


imageLineHeight = 225
imageHeight = 154
imageWidth = 88
imgList = ["data/antivirusPRIME.png", "data/antivirusPRO.png",
           "data/passwordManager.png", "data/optimizer.png", "data/systemSPEEDUP.png", "data/phantomVPN.png"]

buttonHeight = 50
buttonWidth = 150

buttonWidthTo2 = buttonWidth / 2
buttonHeightTo2 = buttonHeight / 2

incrementer = 200

# MAIN


system = Window("Hello", 1200, 500)

pLine = Point(100, imageLineHeight)
pLine1 = Point(100, imageLineHeight + 150)

for i in range(len(imgList)):
    system.add_image(pLine, imgList[i])
    pLine = increment(pLine, incrementer)
    buttonName = imgList[i].split(".")[0].split('/')[-1]
    system.add_button(increment(pLine1, -buttonWidthTo2, -buttonHeightTo2),
                      increment(pLine1, buttonWidthTo2, buttonHeightTo2), True, buttonName)
    pLine1 = increment(pLine1, incrementer)

system.add_image(Point(100, 50), "data/logo1.png")
system.add_button(Point(1025, 420), Point(1175, 470), False, "Buy")

system.print_all()

while True:
    obj = system.get_action()
    if obj is not None:
        #  functie database

