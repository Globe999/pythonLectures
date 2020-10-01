from math import sin, cos, radians, copysign
import random

class Game:
    """ This is the model of the game"""

    def __init__(self, cannonSize, ballSize):
        """ Create a game with a given size of cannon (length of sides) and projectiles (radius) """

        #Init game with given parameters, left side always goes first
        self.cannonSize = cannonSize
        self.ballSize = ballSize
        self.players = [Player(self, "blue", True, -90, True),
                        Player(self, "red", False, 90, False)]
        self.wind = (random.random() * 20 - 10)


    def getPlayers(self):
        """ A list containing both players """
        return self.players


    def getCannonSize(self):
        """ The height/width of the cannon """
        return self.cannonSize


    def getBallSize(self):
        """ The radius of cannon balls """
        return self.ballSize


    def getCurrentPlayer(self):
        """ The current player, i.e. the player whose turn it is """
        for p in self.players:
            if p.isActive:
                return p


    def getOtherPlayer(self):
        """ The opponent of the current player """
        for p in self.players:
            if not p.isActive:
                return p


    def getCurrentPlayerNumber(self):
        """ The number (0 or 1) of the current player. This should be the position of the current player in getPlayers(). """
        for p in self.players:
            if p.isActive:
                return self.players.index(p)


    def nextPlayer(self):
        """ Switch active player """
        for p in self.players:
            if p.isActive:
                p.isActive = False
            else:
                p.isActive = True

    def setCurrentWind(self, wind):
        """ Set the current wind speed """
        self.wind = wind

    def getCurrentWind(self):
        """Returns current wind speed"""
        return self.wind

    def newRound(self):
        """ Start a new round with a random wind value (-10 to +10) """
        self.setCurrentWind((random.random() * 20 - 10))




class Player:
    """ Models a player """
    def __init__(self, game, color, firesRight, position, isActive):
        """Creates a player with relevant attributes"""
        self.game = game
        self.color = color 
        self.firesRight = firesRight
        self.position = position
        self.isActive = isActive  # Bool
        self.score = 0
        self.aim = 45
        self.velocity = 40

    def fire(self, angle, velocity):
        """ Create and return a projectile starting at the centre of this players cannon. Replaces any previous projectile for this player. """
        self.aim = angle
        self.velocity = velocity

        #reverse angle if it shoots from right to left
        if not self.firesRight:
            angle = 180 - angle
        return Projectile(angle, self.velocity, self.game.getCurrentWind(), self.position, self.game.cannonSize / 2, -110, 110)


    def projectileDistance(self, proj):
        """ Gives the x-distance from this players cannon to a projectile. If the cannon and the projectile touch (assuming the projectile is on the ground and factoring in both cannon and projectile size) this method should return 0"""
        diff = abs(proj.xPos - self.getX())
        hitRange = self.game.ballSize + self.game.cannonSize / 2
        
        if diff < hitRange:
            return 0
        else:
            return copysign(diff - hitRange, (proj.xPos - self.getX()))
        

    def getScore(self):
        """ The current score of this player """
        return self.score


    def increaseScore(self):
        """ Increase the score of this player by 1."""
        self.score += 1


    def getColor(self):
        """ Returns the color of this player (a string)"""
        return self.color


    def getX(self):
        """ The x-position of the centre of this players cannon """
        return self.position


    def getAim(self):
        """ The angle and velocity of the last projectile this player fired, initially (45, 40) """
        return self.aim, self.velocity




class Projectile:
    """ Models a projectile (a cannonball, but could be used more generally) """

    def __init__(self, angle, velocity, wind, xPos, yPos, xLower, xUpper):
        """
            Constructor parameters:
            angle and velocity: the initial angle and velocity of the projectile 
                angle 0 means straight east (positive x-direction) and 90 straight up
            wind: The wind speed value affecting this projectile
            xPos and yPos: The initial position of this projectile
            xLower and xUpper: The lowest and highest x-positions allowed
        """
        self.yPos = yPos
        self.xPos = xPos
        self.xLower = xLower
        self.xUpper = xUpper
        theta = radians(angle)
        self.xvel = velocity*cos(theta)
        self.yvel = velocity*sin(theta)
        self.wind = wind


    def update(self, time):
        """ 
            Advance time by a given number of seconds
            (typically, time is less than a second, 
            for large values the projectile may move erratically)
        """
        # Compute new velocity based on acceleration from gravity/wind
        yvel1 = self.yvel - 9.8*time
        xvel1 = self.xvel + self.wind*time

        # Move based on the average velocity in the time period
        self.xPos = self.xPos + time * (self.xvel + xvel1) / 2.0
        self.yPos = self.yPos + time * (self.yvel + yvel1) / 2.0

        # make sure yPos >= 0
        self.yPos = max(self.yPos, 0)

        # Make sure xLower <= xPos <= mUpper
        self.xPos = max(self.xPos, self.xLower)
        self.xPos = min(self.xPos, self.xUpper)

        # Update velocities
        self.yvel = yvel1
        self.xvel = xvel1


    def isMoving(self):
        """ A projectile is moving as long as it has not hit the ground or moved outside the xLower and xUpper limits """
        return 0 < self.getY() and self.xLower < self.getX() < self.xUpper

    def getX(self):
        return self.xPos


    def getY(self):
        """ The current y-position (height) of the projectile". Should never be below 0. """
        return self.yPos
