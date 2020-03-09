from graphics import *

# CONSTANTS

def idle():
    return None

COLOR_DICT = {"red" : "d63447", "gray" : "f6eedf", "blacker gray" : "d1cebd" }


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

        self.rect.setFill(COLOR_DICT["blacker gray"])

        textCounterPos = Point(self.anchor.x, self.anchor.y - (self.p1.y / 2) - 80)
        self.textCounter = Text(textCounterPos, "Quantity: " + str(self.counter))

    def print_obj(self, win):

        self.rect.draw(win)
        self.text.draw(win)

        if self.showCounter is True:
            self.textCounter.draw(win)

    def is_pressed(self, p, win):
        return self.p1.x < p.x < self.p2.x and self.p1.y < p.y < self.p2.y

    def rect_color(self, win):

    def increase_quantity(self, win):
        self.counter += 1

        self.rect.undraw()
        self.rect.setFill(COLOR_DICT["red"])
        self.rect.draw(win)

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
        self.addedObjects = []

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
                        obj.increase_quantity(self.win)

    def print_all(self):
        for obj in self.addedObjects:
            obj.print_obj(self.win)
