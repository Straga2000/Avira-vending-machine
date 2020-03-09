from graphics import *

# FUNCTIONS


def idle():
    return None

# CONSTANTS


COLOR_DICT = {"red" : "#CC0000", "gray" : "#D9D2D2", "blacker gray" : "#D1CEBD", "orange" : "#F57B51", "light pink" : "#e2afaf", "white" : "#FFFFFF", "green" : "#61c616", "yellow" : "#eff692"}


class Button:
    def __init__(self, p1, p2, showCounter= False, text=""):

        self.name = "button"
        self.counter = 0
        self.showCounter = showCounter

        self.p1 = p1
        self.p2 = p2
        self.anchor = Point((p1.x + p2.x) / 2, (p1.y + p2.y) / 2)
        self.rect = Rectangle(p1, p2)
        self.text = Text(self.anchor, text)


        self.textColor = COLOR_DICT["white"]
        self.mainColor = COLOR_DICT["red"]
        self.pressedColor = COLOR_DICT["yellow"]

        self.text.setTextColor(self.textColor)

        self.rect.setFill(self.mainColor)
        self.rect.setWidth(0)

        textCounterPos = Point(self.anchor.x, self.anchor.y - (self.p1.y / 2) - 80)
        self.textCounter = Text(textCounterPos, "Quantity: " + str(self.counter))

    def get_text_name(self):
        return self.text.getText()

    def print_obj(self, win):

        self.rect.draw(win)
        self.text.draw(win)

        if self.showCounter is True:
            self.textCounter.draw(win)

    def unprint_obj(self):

        self.rect.undraw()
        self.text.undraw()
        self.textCounter.undraw()

    def is_pressed(self, p):
        return self.p1.x < p.x < self.p2.x and self.p1.y < p.y < self.p2.y

    def rect_color(self, win, color):
        self.rect.setFill(color)
        self.unprint_obj()
        self.print_obj(win)
        time.sleep(0.3)

    def increase_quantity(self, win):
        self.counter += 1
        if self.showCounter is True:
            self.textCounter.undraw()
            self.textCounter.setText("Quantity: " + str(self.counter))
            self.textCounter.draw(win)

        self.rect_color(win, self.pressedColor)
        self.rect_color(win, self.mainColor)

        if self.showCounter is True:
            self.textCounter.undraw()
            self.textCounter.setText("Quantity: " + str(self.counter))
            self.textCounter.draw(win)


class ImageHolder:
    def __init__(self, p, name):

        self.name = "image"
        self.img = Image(p, name)
        self.width = self.img.getWidth()
        self.height = self.img.getHeight()
        anchor = self.img.getAnchor()

        self.p1 = Point(anchor.getX() - (self.width / 2), anchor.getY() - (self.height / 2))
        self.p2 = Point(anchor.getX() + (self.width / 2), anchor.getY() + (self.height / 2))

        self.rect = Rectangle(self.p1, self.p2)

    def is_pressed(self, p):
        return self.p1.x < p.x < self.p2.x and self.p1.y < p.y < self.p2.y

    def print_obj(self, win):
        self.img.draw(win)

class Window:
    def __init__(self, name, width, height):
        self.width = width
        self.height = height
        self.win = GraphWin(name, self.width, self.height)

        self.win.setBackground(COLOR_DICT["blacker gray"])

        self.addedObjects = []
        self.boughtList = {}

    def add_button(self, p1, p2, id, text=""):
        obj = Button(p1, p2, id, text)
        self.addedObjects.append(obj)

    def add_image(self, anchor, name):
        obj = ImageHolder(anchor, name)
        self.addedObjects.append(obj)

    def add_entry(self, anchor, width):
        obj = Entry(anchor, width)
        self.addedObjects.append(obj)

    def get_action(self):
        mouse = self.win.checkMouse()
        if mouse is not None:
            for obj in self.addedObjects:
                if obj.name == "button":
                    #print(obj.is_pressed(mouse))
                    if obj.is_pressed(mouse):

                        if obj.get_text_name == "Buy":
                            obj.increase_quantity(self.win)
                            return self.boughtList
                        else:
                            obj.increase_quantity(self.win)
                            self.boughtList[obj.get_text_name()] = obj.counter
        return None

    def print_all(self):
        for obj in self.addedObjects:
            obj.print_obj(self.win)
