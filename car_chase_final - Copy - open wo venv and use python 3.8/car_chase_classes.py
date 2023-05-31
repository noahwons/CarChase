# ====================================================================================================
# Program:
# Author:
# Description:
# Date Modified:
# Version:
# ====================================================================================================
# Import Libraries
from graphics import *
import random
from time import perf_counter
# ====================================================================================================
# User-Defined Classes


class Car(object):
    """A template for creating car objects"""
    def __init__(self, speed, x, y, size, window, cop=False):
        """Constructs car objects"""
        self.__speed = speed
        self.__size = size
        self.__window = window
        self.__direction = None
        self.__x = x
        self.__y = y
        self.__car = Rectangle(Point(self.__x - self.__size / 2, self.__y - self.__size / 2), Point(self.__x + self.__size / 2, self.__y + self.__size / 2))
        self.carImageIndex = 0
        self.copImageIndex = 0
        self.__cop = cop
        self.carDriveForwardImages = []
        self.copDriveForwardImages = []
        self.loadCarImages()
        self.loadCopImages()

    def __str__(self):
        """Returns a string representation of the car object"""
        return f"Direction: {self.__direction}\nX cord: {self.__x}\nY cord: {self.__y}\nIs Cop? : {self.__cop}"

    def getSpeed(self):
        """Returns the speed of the Car"""
        return self.__speed

    def getSize(self):
        """Returns the size of the Car"""
        return self.__size

    def getX(self):
        """Returns the X coordinate of the Car"""
        return self.__x

    def getY(self):
        """Returns the X coordinate of the Car"""
        return self.__y

    def getDir(self):
        """Returns the direction of the Car"""
        return self.__direction

    def getRectangle(self):
        """Returns the rectangle representation of the Car"""
        return self.__car

    def loadCarImages(self):
        """Load all images of the Car object driving forward"""
        if not self.__cop:
            for i in range(1, 7):
                image = Image(Point(self.__x, self.__y), f"sports_car/sports car-{i}.png.png")
                image.transform(scale=.13)
                self.carDriveForwardImages.append(image)

    def loadCopImages(self):
        """Load all images of the Car object driving forward"""
        if self.__cop:
            for i in range(1, 5):
                image = Image(Point(self.__x, self.__y), f"cop_car/cop car-{i}.png.png")
                image.transform(scale=.15)
                self.copDriveForwardImages.append(image)

    def drawCarImage(self):
        """Draws the Car Image Representation"""
        self.carDriveForwardImages[int(self.carImageIndex)].draw(self.__window)

    def undrawCarImage(self):
        """Un-draws the Car Image Representation"""
        self.carDriveForwardImages[int(self.carImageIndex)].undraw()

    def drawCopImage(self):
        """Draws the Cop Image Representation"""
        self.copDriveForwardImages[int(self.copImageIndex)].draw(self.__window)

    def undrawCopImage(self):
        """Un-draws the Cop Image Representation"""
        self.copDriveForwardImages[int(self.copImageIndex)].undraw()

    def move(self):
        """Moves the car object based on the user input"""
        if self.__direction == "right":
            self.__car.move(self.__speed, 0)
            self.__x += self.__speed
            if not self.__cop:
                self.carDriveForwardImages[int(self.carImageIndex)].anchor.x = self.__x
            if self.__cop:
                self.copDriveForwardImages[int(self.copImageIndex)].anchor.x = self.__x

        if self.__direction == "left":
            self.__car.move(-1*self.__speed, 0)
            self.__x -= self.__speed
            if not self.__cop:
                self.carDriveForwardImages[int(self.carImageIndex)].anchor.x = self.__x
            if self.__cop:
                self.copDriveForwardImages[int(self.copImageIndex)].anchor.x = self.__x

    def animateCars(self):
        if self.carImageIndex > 5 and not self.__cop:
            self.carImageIndex = 0
        if self.copImageIndex > 3 and self.__cop:
            self.copImageIndex = 0
        else:
            if self.__cop:
                self.copImageIndex += 0.09
            if not self.__cop:
                self.carImageIndex += 0.4

    def changeDirection(self):
        """Change the direction/column of the Car object based on user input"""
        keys = self.__window.checkKeys()

        if "a" in keys:
            self.__direction = "left"
        if "d" in keys:
            self.__direction = "right"
        if "A" in keys:
            self.__direction = "left"
        if "D" in keys:
            self.__direction = "right"

    def update(self):
        """Updates the Car objects on the window"""
        if not self.__cop:
            self.undrawCarImage()
        if self.__cop:
            self.undrawCopImage()
        self.animateCars()
        self.changeDirection()
        self.move()
        if self.__cop:
            self.drawCopImage()
        if not self.__cop:
            self.drawCarImage()


class Obstacle(object):
    """A template for creating Obstacle objects"""
    def __init__(self, speed, x, y, size, color, window):
        """Constructs Obstacle Objects"""
        self.__speed = speed
        self.__size = size
        self.__color = color
        self.__window = window
        self.__x = x
        self.__y = y
        self.__obs = Rectangle(Point(self.__x - self.__size / 2, self.__y - self.__size / 2), Point(self.__x + self.__size / 2, self.__y + self.__size / 2))
        self.__image = Image(Point(self.__x, self.__y), "misc_imgs/roadblock.png")
        self.__image.transform(scale=2)

    def __str__(self):
        """Returns a string representation of the Obstacle object"""
        return f"X cord: {self.__x}\nY cord: {self.__y}\n"

    def getSpeed(self):
        """Returns the speed of the Obstacle"""
        return self.__speed

    def getSize(self):
        """Returns the size of the Obstacle"""
        return self.__size

    def getX(self):
        """Returns the X coordinate of the Obstacle"""
        return self.__x

    def getY(self):
        """Returns the X coordinate of the Obstacle"""
        return self.__y

    def getImage(self):
        """Returns the image object"""
        return self.__image

    def setX(self, newX):
        """Sets the x-coordinate of the Obstacle to the newX"""
        self.__x = newX
        self.__image.anchor.x = newX + self.__size/2

    def getRectangle(self):
        """Returns the rectangle representation of the Obstacle"""
        return self.__obs

    def setY(self, newY):
        """Sets the y-coordinate of the Obstacle to the newY"""
        self.__y = newY

    def setSize(self, newSize):
        """Sets the size of the Obstacle to the newSize"""
        self.__size = newSize

    def setPosition(self, newX, newY):
        """Sets the position of the obstacle to the newPos"""
        self.setY(newY)
        self.setX(newX)

    def setSpeed(self, newSpeed):
        """Sets the speed od the Obstacle to the newSpeed"""
        self.__speed = newSpeed

    def move(self):
        """Moves the Obstacle object"""
        self.__obs.move(0, self.__speed)
        self.__y += self.__speed
        self.__image.anchor.y = self.__y + self.__size/2

    def update(self):
        """Updates the Obstacle objects on the window"""
        self.__image.undraw()
        self.move()
        self.__image.draw(self.__window)


class RoadLine(object):
    """A template for creating RoadLine obects"""
    def __init__(self, speed, x1, y1, x2, y2, color, window):
        """Constructs road line objects"""
        self.__speed = speed
        self.__x1 = x1
        self.__y1 = y1
        self.__y2 = y2
        self.__x2 = x2
        self.__color = color
        self.__window = window
        self.__line = Rectangle(Point(self.__x1, self.__y1), Point(self.__x2, self.__y2))
        self.__line.setFill(self.__color)

    def __str__(self):
        """Returns a string representation of the Obstacle object"""
        return f"X cord1: {self.__x1}\nX cord2: {self.__x2}Y cord1: {self.__y1}\nYcord2: {self.__y2}"

    def getX1(self):
        """Returns the X1 value of RoadLine objects"""
        return self.__x1

    def getX2(self):
        """Returns the X2 value of RoadLine objects"""
        return self.__x2

    def getY1(self):
        """Returns the Y1 value of RoadLine objects"""
        return self.__y1

    def getY2(self):
        """Returns the X2 value of RoadLine objects"""
        return self.__y1

    def getRectangle(self):
        """Returns the rectangle representation of the Obstacle"""
        return self.__line

    def getSpeed(self):
        """Returns the speed of the RoadLine object"""
        return self.__speed

    def setX1(self, newX):
        """Sets the value of X1 to the newX"""
        self.__x1 = newX

    def setX2(self, newX):
        """Sets the value of X2 to the newX"""
        self.__x2 = newX

    def setY1(self, newY):
        """Sets the value of Y1 to newY"""
        self.__y1 = newY

    def setY2(self, newY):
        """Sets the value of Y2 to newY"""
        self.__y2 = newY

    def setSpeed(self, newSpeed):
        """Sets the speed of the RoadLine object to the new speed"""
        self.__speed = newSpeed

    def move(self):
        """Moves the RoadLines object"""
        self.__line.move(0, self.__speed)
        self.__y1 += self.__speed
        self.__y2 += self.__speed

    def update(self):
        """Updates the RoadLines objects on the window"""
        self.__line.undraw()
        self.move()
        self.__line.draw(self.__window)


class StartMenu(object):
    def __init__(self, window):
        self.__window = window
        self.__startButton = Rectangle(Point(250, 205), Point(870, 500))
        self.__image = Image(Point(self.__window.getWidth()//2, self.__window.getHeight()//2), "misc_imgs/Start_button.png")
        self.__image.transform(scale=1)
        self.__firstClick = True
        self.__view = True

    def get_view(self):
        """Returns the viewing state of the start menu"""
        return self.__view

    def updateMenu(self):
        self.__image.undraw()
        if self.__view:
            self.__image.draw(self.__window)
        self.testCollision()
        return False

    def testCollision(self):
        """Detects if the mouse has clicked the start button"""
        mouse = self.__window.getCurrentMouseLocation()

        if self.__window.mousePressed and self.__firstClick:
            self.__firstClick = False
            if Rectangle.testCollision_RectVsPoint(self.__startButton, mouse):
                self.__image.undraw()
                self.__view = False
        elif not self.__window.mousePressed and not self.__firstClick:
            self.__firstClick = True


class Timer(object):
    def __init__(self):
        """Constructs Timer object"""
        self.start = 0
        self.finish = 0
        self.elapsedTime = 0

    def startTimer(self):
        """Start the Timer"""
        self.start = perf_counter()

    def stop(self):
        """Stop the Timer"""
        self.finish = perf_counter()

    def getTime(self):
        """Generate the difference and return value"""
        self.elapsedTime = self.finish - self.start
        return self.elapsedTime
