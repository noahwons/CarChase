# ====================================================================================================
# Program:
# Author:
# Description:
# Date Modified:
# Version:
# ====================================================================================================
# Import Libraries
from car_chase_final_classes_edited import *
import time
from time import perf_counter
import csv

# ====================================================================================================
# User-Defined Functions


def drawRoadLines():
    """Draw the lines in the road that differentiates the lanes"""
    roadLines = []
    for i in range(window.getHeight()):
        if i % 110 == 0:
            roadLine = RoadLine(ROADSPEED, (window.getWidth() / 2) - 5, i, (window.getWidth() / 2) + 5, i + 70, "white",
                                window)
            roadLines.append(roadLine)
    return roadLines


def respawnRoadLines(roadLines):
    """Takes roadLines as a parameter, a list of RoadLine objects, and respawns them when they are off of the window"""
    for roadLine in range(len(roadLines)):
        if roadLines[roadLine].getY1() > window.getHeight():
            roadLines[roadLine].setY1(-65)
            roadLines[roadLine].setY2(0)
            rectangle = roadLines[roadLine].getRectangle()
            rectangle.p1 = Point((window.getWidth() / 2) - 5, -65)
            rectangle.p2 = Point((window.getWidth() / 2) + 5, 0)


def sideWalkCollision():
    """Detect of the Car has collided with the sidewalk"""
    if Rectangle.testCollision_RectVsRect(car.getRectangle(), leftSidewalk) or Rectangle.testCollision_RectVsRect(
            car.getRectangle(), rightSidewalk):
        return True
    else:
        return False


def obstacleCollision():
    """Check of the obstacle has collided with the car"""
    if Rectangle.testCollision_RectVsRect(car.getRectangle(), obstacle.getRectangle()):
        return True
    else:
        return False


def respawnObstacle():
    """Respawn the Rectangle at the top of the screen after it goes off the bottom of the screen"""
    if obstacle.getY() + obstacle.getSize() / 2 > window.getHeight():
        obstacleSize = obstacle.getSize()
        rectangleRep = obstacle.getRectangle()
        xCord = random.randrange(100 + obstacleSize * 2, (window.getWidth()) - 100 - obstacleSize * 2)
        yCord = 0 - obstacleSize
        obstacle.setSize(obstacleSize)
        obstacle.setY(yCord)
        obstacle.setX(xCord)
        rectangleRep.p1 = Point(xCord, yCord)
        rectangleRep.p2 = Point(xCord + obstacleSize, yCord + obstacleSize)


def textUpdate(text):
    """Update the text of the game"""
    text.undraw()
    counter = perf_counter() - listOfTimes[0]  # listOfTimes[0] contains the time the user spent in the menu
    text.setText(f"Time: {counter:.4}")
    text.setStyle("bold")
    text.draw(window)
    return counter


def drawGameOverText(deathTime):
    """Draw the game over text of the game with the amount of time elapsed"""
    gameOverText = Text(Point(window.getWidth() / 2, window.getHeight() / 2), f"You Crashed! Score: {deathTime:.4}s")
    gameOverText.setFill("white")
    gameOverText.setSize(24)
    gameOverText.setStyle("bold")
    gameOverText.draw(window)


def drawHighScoreText():
    """Draw the game over text of the game with the amount of time elapsed"""
    with open("highscore.csv") as file:
        reader = csv.reader(file)
        for row in reader:
            highscore = row[0]
            gameOverText = Text(Point(window.getWidth() / 2, (window.getHeight() / 2) - 50), f"High-score: {highscore:.4}s")
            gameOverText.setFill("white")
            gameOverText.setSize(24)
            gameOverText.setStyle("bold")
            gameOverText.draw(window)
            break


def drawNewHighScore():
    """Draws a 'New High-Score' Text object"""
    newHighScoreText = Text(Point(window.getWidth() / 2, (window.getHeight() / 2) + 50), "New High-Score!")
    newHighScoreText.setFill("lime")
    newHighScoreText.setSize(24)
    newHighScoreText.setStyle("bold")
    newHighScoreText.draw(window)


def checkHighscore(deathTime):  # There must be a value in the csv file or an IndexError is raised
    """Determines if the new score is greater than the current High-Score located in 'highscore.csv'"""
    with open("highscore.csv", "r") as fileR:
        reader = csv.reader(fileR)
        for row in reader:
            try:
                if float(row[0]) < float(deathTime):
                    with open("highscore.csv", "w") as fileW:
                        writer = csv.writer(fileW)
                        writer.writerow([deathTime])
                    return True
            except IndexError:
                pass


def changeRoadSpeed(roadLines):
    """Changes the speed of all objects falling towards Cop and Car objects"""
    t = perf_counter()

    if 10.019 > t > 10:
        global ROADSPEED
        ROADSPEED += 2
        obstacle.setSpeed(ROADSPEED)
        for roadline in roadLines:
            roadline.setSpeed(ROADSPEED)
    if 20.019 > t > 20:
        ROADSPEED += 2
        obstacle.setSpeed(ROADSPEED)
        for roadline in roadLines:
            roadline.setSpeed(ROADSPEED)


def drawControls():
    controls = Text(Point(window.getWidth()/2, 50, ), "Use 'a' and 'd' to move left to right")
    controls.setFill("white")
    controls.setSize(24)
    controls.undraw()
    return controls


# ====================================================================================================
# Global Variables

listOfTimes = []
ROADSPEED = 10
SIZE = 65
window = GraphWin("Car Chase", 1000, 700, autoflush=False)
car = Car(15, window.getWidth() / 2, window.getHeight() / 2 + 160, SIZE, window, cop=False)
obstacle = Obstacle(ROADSPEED, random.randrange(100, window.getWidth() - 100), -65, 150, "green", window)
obsSize = obstacle.getSize()
rect = obstacle.getRectangle()
x = random.randrange(100 + obsSize * 2, (window.getWidth()) - 100 - obsSize * 2)
y = 0 - obsSize
obstacle.setSize(obsSize)
obstacle.setY(y)
obstacle.setX(x)
rect.p1 = Point(x, y)
rect.p2 = Point(x + obsSize, y + obsSize)
cop = Car(10, window.getWidth() / 2, window.getHeight() / 2 + 290, SIZE, window, cop=True)
window.setBackground("gray")
leftSidewalk = Rectangle(Point(0, 0), Point(100, window.getHeight()+10))
leftSidewalk.setFill("tan")
leftSidewalk.draw(window)
rightSidewalk = Rectangle(Point(window.getWidth() - 100, 0), Point(window.getWidth(), window.getHeight()+10))
rightSidewalk.setFill("tan")
rightSidewalk.draw(window)
timeText = Text(Point(window.getWidth()/2, 50, ), "Time: 0")
timeText.setFill("white")
timeText.setSize(24)
menu = StartMenu(window)
timer = Timer()

# ====================================================================================================
# Main Function


def main():

    # Draw the roadLine(s)
    roadLines = drawRoadLines()

    # Draw a description of the controls
    gameControls = drawControls()
    gameControls.draw(window)

    # Start the timer
    timer.startTimer()

    # Create window and update objects
    while not window.closed:

        # Generate the start button
        menu.updateMenu()

        if not menu.get_view():

            # Gets the time the user spends in the menu
            timer.stop()

            # Get elapsed time including the time spend in the menu screen
            elapsedTime = timer.getTime()

            # Append all times to listOfTimes
            listOfTimes.append(elapsedTime)

            # Un-draw controls description
            gameControls.undraw()

            # Change the speed of the road-based on 10s time intervals ending at 20s
            changeRoadSpeed(roadLines)

            # Respawn Road-lines based on edge collision
            respawnRoadLines(roadLines)

            # Move roadLine objects
            for roadLine in range(len(roadLines)):
                roadLines[roadLine].update()

            # Update the timeText
            textUpdate(timeText)
            deathTime = textUpdate(timeText)

            # Update the Car object
            car.update()

            # Update the Cop object
            cop.update()

            # Check for Obstacle-Edge collision
            respawnObstacle()

            # Update the Obstacle Object
            obstacle.update()

            # Check for edge collision
            if obstacleCollision() or sideWalkCollision():
                timeText.undraw()
                drawHighScoreText()
                drawGameOverText(deathTime)
                if checkHighscore(deathTime):  # check High-score returns a bool
                    drawNewHighScore()
                window.getMouse()
                window.close()

        # Update the window
        window.update()
        time.sleep(0.005)


# ====================================================================================================
# Call the Main Function


main()
