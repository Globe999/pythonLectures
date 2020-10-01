#------------------------------------------------------
#This module contains all graphics-classes for the game
#Most classes are wrappers around model classes, e.g. 
#  * GraphicGame is a wrappoer around Game
#  * GraphicPlayer is a wrapper around Player
#  * GraphicProjectile is a wrapper around Projectile
#In addition there are two UI-classes that have no 
#counterparts in the model:
#  * Button
#  * InputDialog
#------------------------------------------------------



# This is the only place where graphics should be imported!
from graphics import *

# TODO: There needs to be a class called GraphicGame here. 
# Its constructor should take only a Game object.
# TODO: In addition to the methods of Game, GraphicGame needs to have a getWindow method that returns the main GraphWin object the game is played in
# HINT: Look at the other classes in this file, the GraphicGame class should "wrap around" a Game object the same way GraphicPlayer wraps around a Player
# HINT: These lines are good for creating a window:
#  win = GraphWin("Cannon game" , 640, 480, autoflush=False)
#  win.setCoords(-110, -10, 110, 155)
# HINT: Don't forget to call draw() on every component you create, otherwise they will not be visible
# HINT: You need to get the Players from the Game object (the model), wrap them into GraphicPlayers and store them, and all get-methods for players (e.g. getCurrentPlayer) must return the Graphical versions
class GraphicGame:
    def __init__(self, game):
        self.game = game
        self.win = GraphWin("Cannon game", 640, 480, autoflush=False)
        self.win.setCoords(-110, -10, 110, 155)
        self.players = [GraphicPlayer(self.game.players[0], self), GraphicPlayer(self.game.players[1], self)]
    def getWindow(self):
        return self.win

    def getPlayers(self):
        return self.players

    def getCannonSize(self):
        return self.game.getCannonSize()
    def getBallSize(self):
        return self.game.getBallSize()

    def getCurrentPlayer(self):
        if self.game.players[0].isActive:
            return self.players[0]
        else:
            return self.players[1]
        
    def getOtherPlayer(self):
        if self.game.players[0].isActive:
            return self.players[1]
        else:
            return self.players[0]
    def getCurrentPlayerNumber(self):
        return self.game.getCurrentPlayerNumber()
    def nextPlayer(self):
        return self.game.nextPlayer()
    def setCurrentWind(self, wind):
        return self.game.setCurrentWind(wind)
    def getCurrentWind(self):
        return self.game.getCurrentWind()
    def newRound(self):
        return self.game.newRound()

class GraphicPlayer:
    # TODO: We need a constructor here! The constructor needs to take a Player object as parameter and store it in self.player for the methods below to work.
    # HINT: The constructor should create and draw the graphical elements of the player (score and cannon)
    # HINT: The constructor probably needs a few additional parameters e.g. to access the game window.
    def __init__(self, player, ggame):
        self.player = player
        self.ggame = ggame
        self.proj = None

        x = self.player.getX()
        cannonSize = self.ggame.getCannonSize()
        self.gCannon = Rectangle(Point(x - cannonSize/2, cannonSize),(Point(x + cannonSize/2, 0)))
        self.gCannon.setFill(self.player.getColor())
        self.gCannon.draw(self.ggame.getWindow())

        p1 = Point(x, -5)
        self.gText = Text(p1, "Score: %s" % self.player.getScore())
        
        self.gText.draw(self.ggame.getWindow())

    def fire(self, angle, vel): 
        # Fire the cannon of the underlying player object
        proj = self.player.fire(angle, vel)

        if self.proj is not None:
            self.proj.undraw()
            
        self.proj = GraphicProjectile(proj, self.ggame, self.player.getColor())
        #TODO: We need to undraw the old GraphicProjectile for this player (if there is one).
        
        # TODO: proj is a Projectile, but we should return a GraphicProjectile here! We need to create a GraphicProjectile "wrapping" around proj.
        return self.proj
    
    def getAim(self):
        return self.player.getAim()
        
    def getColor(self):
        return self.player.getColor()

    def getX(self):
        return self.player.getX()

    def getScore(self):
        return self.player.getScore()
        
    def increaseScore(self):
        self.player.increaseScore()
        self.gText.setText("Score %s" % self.player.getScore())
        # TODO: This seems like a good place to update the score text.


""" A graphic wrapper around the Projectile class (adapted from ShotTracker in book)"""
class GraphicProjectile:
    # TODO: This one also needs a constructor, and it should take a Projectile object as parameter and store it in self.proj.
    # Hint: We are also going to need access to the game window
    # Hint: There is no color attribute in the Projectile class, either it needs to be passed to the constructor here or Projectile needs to be modified.
    def __init__(self, proj, ggame, color):
        self.proj = proj
        self.ggame = ggame
        self.color = color

        p1 = Point(self.proj.getX(), self.proj.getY())
        self.ball = Circle(p1, self.ggame.getBallSize())
        self.ball.setFill(color)
        self.ball.draw(self.ggame.getWindow())
        update()

    def update(self, dt):
        # update the projectile
        oldX = self.proj.getX()
        oldY = self.proj.getY()
        self.proj.update(dt)
        self.ball.move(self.proj.getX() - oldX, self.proj.getY() - oldY)
        
    def getX(self):
        return self.proj.getX()

    def getY(self):
        return self.proj.getY()

    def isMoving(self):
        return self.proj.isMoving()

    def undraw(self):
        self.ball.undraw()

    # TODO: There needs to be a way of undrawing the projectile.
    # HINT: All graphical components in graphics.py have undraw()-methods    


""" A somewhat specific input dialog class (adapted from the book) """
class InputDialog:
    """ Takes the initial angle and velocity values, and the current wind value """
    def __init__ (self, angle, vel, wind):
        self.win = win = GraphWin("Fire", 200, 300)
        win.setCoords(0,4.5,4,.5)
        Text(Point(1,1), "Angle").draw(win)
        self.angle = Entry(Point(3,1), 5).draw(win)
        self.angle.setText(str(angle))
        
        Text(Point(1,2), "Velocity").draw(win)
        self.vel = Entry(Point(3,2), 5).draw(win)
        self.vel.setText(str(vel))
        
        Text(Point(1,3), "Wind").draw(win)
        self.height = Text(Point(3,3), 5).draw(win)
        self.height.setText("{0:.2f}".format(wind))
        
        self.fire = Button(win, Point(1,4), 1.25, .5, "Fire!")
        self.fire.activate()
        self.quit = Button(win, Point(3,4), 1.25, .5, "Quit")
        self.quit.activate()

    """ Runs a loop until the user presses either the quit or fire button """
    def interact(self):
        while True:
            pt = self.win.getMouse()
            if self.quit.clicked(pt):
                return "Quit"
            if self.fire.clicked(pt):
                return "Fire!"

    """ Returns the current values of (angle, velocity) as entered by the user"""
    def getValues(self):
        a = float(self.angle.getText())
        v = float(self.vel.getText())
        return a,v

    def close(self):
        self.win.close()



""" A general button class (from the book) """
class Button:

    """A button is a labeled rectangle in a window.
    It is activated or deactivated with the activate()
    and deactivate() methods. The clicked(p) method
    returns true if the button is active and p is inside it."""

    def __init__(self, win, center, width, height, label):
        """ Creates a rectangular button, eg:
        qb = Button(myWin, Point(30,25), 20, 10, 'Quit') """ 

        w,h = width/2.0, height/2.0
        x,y = center.getX(), center.getY()
        self.xmax, self.xmin = x+w, x-w
        self.ymax, self.ymin = y+h, y-h
        p1 = Point(self.xmin, self.ymin)
        p2 = Point(self.xmax, self.ymax)
        self.rect = Rectangle(p1,p2)
        self.rect.setFill('lightgray')
        self.rect.draw(win)
        self.label = Text(center, label)
        self.label.draw(win)
        self.deactivate()

    def clicked(self, p):
        "RETURNS true if button active and p is inside"
        return self.active and \
               self.xmin <= p.getX() <= self.xmax and \
               self.ymin <= p.getY() <= self.ymax

    def getLabel(self):
        "RETURNS the label string of this button."
        return self.label.getText()

    def activate(self):
        "Sets this button to 'active'."
        self.label.setFill('black')
        self.rect.setWidth(2)
        self.active = 1

    def deactivate(self):
        "Sets this button to 'inactive'."
        self.label.setFill('darkgrey')
        self.rect.setWidth(1)
        self.active = 0