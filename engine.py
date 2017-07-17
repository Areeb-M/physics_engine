from entity import Entity
from setup import *

class Engine (object):
    def __init__ (self, width, height, entities = []):
        self.width = width
        self.height = height
        self.entities = entities

    def addEnt (self, color, x, y, width, height, vx, vy, mass):
        self.entities.append (Entity (color, x, y, width, height, vx, vy, mass))

    def areColliding (self, a, b):
        if a.x > b.x + b.width:
            return False
        if a.x + a.width < b.x:
            return False
        if a.y > b.y + b.height:
            return False
        if a.y + a.height < b.y:
            return False
        return True

    def handleEntCollisions (self, fps):
        for a in self.entities:
            for b in self.entities:
                if self.areColliding (a, b):
                    print ("                        Entity Collision")
                    a.collide (b)
                    a.update (fps)
                    b.update (fps)
                else:
                    print ("no collision")

    def handleBorderCollision (self, ent, fps):
        ent.timeInAir += 1 / (fps * GRAV_FORCE)
        if ent.x < 0:
            #print ("                        Border Collision")
            ent.x = 1
            ent.vx = -ent.vx
        if ent.x + ent.width > self.width:
            #print ("                        Border Collision")
            ent.x = self.width - ent.width
            ent.vx = -ent.vx
        if ent.y < 0:
            #print ("                        Border Collision")
            ent.y = 0
            ent.timeInAir = 0
            ent.vy = -ent.vy
        if ent.y + ent.height > self.height:
            #print ("                        Border Collision")
            ent.y = self.height - ent.height
            ent.vy = -ent.vy

    def handleBorderCollisions (self, fps):
        for ent in self.entities:
            self.handleBorderCollision (ent, fps)

    def updateEnts (self, fps):
        for ent in self.entities:
            ent.update (fps)

    def drawEnts (self, screen):
        for ent in self.entities:
            ent.draw (screen)

    def update (self, fps):
        self.updateEnts (fps)
        self.handleEntCollisions (fps)
        self.handleBorderCollisions (fps)
        """
        for i in range (len (self.entities)):
            print (str (self.entities[i].x) + ", " + str (self.entities[i].y) + "    " +
                   str (self.entities[i].vx) + ", " + str (self.entities[i].vy))

        print ("------------------------------------------------------------------------------------")
        """



