import pyglet
from game import load
# TODO fill in import statements here

# Set up a window
# TODO fill in code here

# Set up the two top labels
# TODO fill in code here


@game_window.event
def on_draw():
    # TODO fill in code here
    pass

from game import resources

# TODO fill in code to create player_ship here

# TODO fill in code to create asteroids here

if __name__ == "__main__":    
    # Tell pyglet to do its thing
    pyglet.app.run()
