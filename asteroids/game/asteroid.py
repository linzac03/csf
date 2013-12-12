import random
import pyglet 
import physicalobject, resources

game_window = pyglet.window.Window(800, 600)

if __name__ == '__main__':
    pyglet.app.run()
pyglet.resource.path = ['../resources']
pyglet.resource.reindex()

class Asteroid(physicalobject.PhysicalObject):
    """An asteroid that divides a little before it dies"""
    # TODO fill in code here
    new_asteroid = physicalobject.PhysicalObject()
    new_asteroid.rotation = random.randint(0, 360)
    new_asteroid.velocity_x = random.random()*40
    new_asteroid.velocity_y = random.random()*40
    pass