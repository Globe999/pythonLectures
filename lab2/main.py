# Imports everything from both model and graphics
from gamemodel import *
from gamegraphics import *
import sys

# Here is a nice little method you get for free
# It fires a shot for the current player and animates it until it stops
def graphicFire(game, angle, vel):
    #This is a gplayer
    player = game.getCurrentPlayer()
    # create a shot and track until it hits ground or leaves window
    gproj = player.fire(angle, vel)
    while gproj.isMoving():
        gproj.update(1/50)
        update(50)
    return gproj

def graphicPlay():
    # TODO: This is where you implement the game loop
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
    # The current player
    player = game.getCurrentPlayer()
    # The player opposing the current player
    other = game.getOtherPlayer()

    # Check if we won
    distance = other.projectileDistance(proj.proj) 
    if distance == 0.0:
        player.increaseScore()
        game.newRound()
    # Switch active player
    game.nextPlayer()
    
    # HINT: Creating a GraphicGame is a good start. 
    # HINT: You can look at the text interface for some inspiration
    # Note that this code should not directly work with any drawing or such, all that is done by the methods in the classes


# Run the game with graphical interface
graphicPlay()
