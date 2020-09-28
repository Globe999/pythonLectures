from math import sin, cos, radians
import random

# TODO: Deal with all TODOs in this file and also remove the TODO and HINT comments.

""" This is the model of the game"""


class Game:
    """ Create a game with a given size of cannon (length of sides) and projectiles (radius) """

    def __init__(self, cannonSize, ballSize):
        # TODO: "pass" means the constructor does nothing. Clearly it should be doing something.
        # HINT: This constructor needs to create two players according to the rules specified in the assignment text
        self.cannonSize = cannonSize
        self.ballSize = ballSize
        self.players = [Player(self, "blue", True, -90, True),
                        Player(self, "red", False, 90, False)]
        self.wind = 0

    """ A list containing both players """

    def getPlayers(self):
        return self.players

    """ The height/width of the cannon """

    def getCannonSize(self):
        return self.cannonSize

    """ The radius of cannon balls """

    def getBallSize(self):
        return self.ballSize

    """ The current player, i.e. the player whose turn it is """

    def getCurrentPlayer(self):
        for p in self.players:
            if p.isActive:
                return p

    """ The opponent of the current player """

    def getOtherPlayer(self):
        for p in self.players:
            if not p.isActive:
                return p

    """ The number (0 or 1) of the current player. This should be the position of the current player in getPlayers(). """

    def getCurrentPlayerNumber(self):
        for p in self.players:
            if p.isActive:
                return self.players.index(p)

    """ Switch active player """

    def nextPlayer(self):
        for p in self.players:
            if p.isActive:
                p.isActive = False
            else:
                p.isActive = True
    """ Set the current wind speed, only used for testing """

    def setCurrentWind(self, wind):
        self.wind = wind

    def getCurrentWind(self):
        return self.wind

    """ Start a new round with a random wind value (-10 to +10) """

    def newRound(self):
        # HINT: random.random() gives a random value between 0 and 1
        # multiplying this by 20 gives a random value between 0 and 20
        # how do you shift a value between 0 and 20 to one between -10 and +10?
        self.setCurrentWind(random.random() * 20) - 10
        pass  # TODO: this should do something instead of nothing


""" Models a player """


class Player:
   # TODO: You need to create a constructor here.
   # HINT: It should probably take the Game that creates it as parameter and some additional properties that differ between players (like firing-direction, position and color)
    def __init__(self, game, color, firesRight, position, isActive):
        self.game = game
        self.color = color
        self.firesRight = firesRight
        self.position = position
        self.isActive = isActive  # Bool
        self.score = 0
        self.aim = 45
        self.velocity = 40
    """ Create and return a projectile starting at the centre of this players cannon. Replaces any previous projectile for this player. """

    def fire(self, angle, velocity):
        # The projectile should start in the middle of the cannon of the firing player
        # HINT: Your job here is to call the constructor of Projectile with all the right values
        # Some are hard-coded, like the boundaries for x-position, others can be found in Game or Player
        self.aim = angle
        self.velocity = velocity
        if not self.firesRight:
            self.aim = 180 - angle
        return Projectile(self.aim, self.velocity, self.game.getCurrentWind(), self.position, self.game.cannonSize / 2, -110, 110)

        """ Gives the x-distance from this players cannon to a projectile. If the cannon and the projectile touch (assuming the projectile is on the ground and factoring in both cannon and projectile size) this method should return 0"""

    def projectileDistance(self, proj):

        # HINT: both self (a Player) and proj (a Projectile) have getX()-methods.
        # HINT: This method should give a negative value if the projectile missed to the left and positive if it missed to the right.
        # The distance should be how far the projectile and cannon are from touching, not the distance between their centers.
        # You probably need to use getCannonSize and getBallSize from Game to compensate for the size of cannons/cannonballs
        otherPlayer = self.game.getOtherPlayer()
        diff = abs(proj.xPos - otherPlayer.getX())
        hitRange = self.game.ballSize + self.game.cannonSize / 2

        print('projX: ' + str(proj.xPos))
        print('playerX: ' + str(otherPlayer.getX()))
        print('diff: ' + str(diff))
        print('hitRange: ' + str(hitRange))
        
        if diff < hitRange:
            print('Skickar tillbaka 0')
            print('--------')
            return 0
        else:
            # Check if proj distance is longer than box, if it is, return neg value
            if otherPlayer.getX() < proj.xPos and self.firesRight: 
                print('player mindre än proj, skjuter från vänster, retunerar pos värde')
                print('--------')
                return diff - hitRange
            elif otherPlayer.getX() < proj.xPos and not self.firesRight:
                print('player mindre än proj, skjuter från höger retunerar neg värde')
                print('--------')
                return -1 * (diff - hitRange)

            elif otherPlayer.getX() > proj.xPos and self.firesRight:
                print('player större än proj, skjuter från höger retunerar neg värde')
                print('--------')
                return -1 * (diff - hitRange)

            elif otherPlayer.getX() > proj.xPos and not self.firesRight:
                print('player större än proj, skjuter från höger retunerar neg värde')
                print('--------')
                return diff - hitRange
        
    """ The current score of this player """

    def getScore(self):
        return self.score

    """ Increase the score of this player by 1."""

    def increaseScore(self):
        self.score += 1

    """ Returns the color of this player (a string)"""

    def getColor(self):
        return self.color

    """ The x-position of the centre of this players cannon """

    def getX(self):
        return self.position

    """ The angle and velocity of the last projectile this player fired, initially (45, 40) """

    def getAim(self):
        return self.aim, self.velocity


""" Models a projectile (a cannonball, but could be used more generally) """


class Projectile:
    """
        Constructor parameters:
        angle and velocity: the initial angle and velocity of the projectile 
            angle 0 means straight east (positive x-direction) and 90 straight up
        wind: The wind speed value affecting this projectile
        xPos and yPos: The initial position of this projectile
        xLower and xUpper: The lowest and highest x-positions allowed
    """

    def __init__(self, angle, velocity, wind, xPos, yPos, xLower, xUpper):
        self.yPos = yPos
        self.xPos = xPos
        self.xLower = xLower
        self.xUpper = xUpper
        theta = radians(angle)
        self.xvel = velocity*cos(theta)
        self.yvel = velocity*sin(theta)
        self.wind = wind

    """ 
        Advance time by a given number of seconds
        (typically, time is less than a second, 
         for large values the projectile may move erratically)
    """

    def update(self, time):
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

    """ A projectile is moving as long as it has not hit the ground or moved outside the xLower and xUpper limits """

    def isMoving(self):
        return 0 < self.getY() and self.xLower < self.getX() < self.xUpper

    def getX(self):
        return self.xPos

    """ The current y-position (height) of the projectile". Should never be below 0. """

    def getY(self):
        return self.yPos
