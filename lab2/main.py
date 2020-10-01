from gamemodel import *
from gamegraphics import *
import sys

# Here is a nice little method you get for free
# It fires a shot for the current player and animates it until it stops
def graphicFire(game, angle, vel):
    """Fires a shot and animates it, returns a graphical projectile"""
    #This is a gplayer
    player = game.getCurrentPlayer()
    # create a shot and track until it hits ground or leaves window
    gproj = player.fire(angle, vel)
    while gproj.isMoving():
        gproj.update(1/50)
        update(50)
    return gproj

def graphicPlay():
    """Game loop, handles input from player"""
    game = GraphicGame(Game(10, 4))
    game.newRound()

    while True:
        player = game.getCurrentPlayer()
        angle, vel = player.getAim()

        dialog = InputDialog(angle, vel, game.getCurrentWind())
        if not dialog.interact() == "Fire!":
            sys.exit(0)
        
        angle, vel = dialog.getValues()
        dialog.close()

        #This is a graphical projectile
        proj = graphicFire(game, angle, vel)
        finishShot(game, proj)


def finishShot(game, proj):
    """Cleans up the shot, check if it hit, awards points"""
    # The current player
    player = game.getCurrentPlayer()
    # The player opposing the current player
    other = game.getOtherPlayer()

    # Check if we won
    distance = other.projectileDistance(proj) 
    if distance == 0.0:
        player.increaseScore()
        game.newRound()
    # Switch active player
    game.nextPlayer()
    
# Run the game with graphical interface
graphicPlay()
