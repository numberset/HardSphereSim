"""
Module defining the Event class which is used to manage collissions and check their validity
"""

from itertools import combinations
from copy import copy
from particle import Particle

class EventParticle(object):
    
    def __init__(self, particle1, particle2):
        self.particle1 = particle1
        self.particle2 = particle2
        
        
        self.id = (self.particle1.getCollisionCountAsCopy(), self.particle2.getCollisionCountAsCopy())
        self.timeUntilCollision = self.particle1.collideParticle(self.particle2)
        
    def isValid(self):
        return self.id == (self.particle1.getCollisionCountAsCopy(), self.particle2.getCollisionCountAsCopy())

    def reevaluateCollisionTime(self):
        self.id = (self.particle1.getCollisionCountAsCopy(), self.particle2.getCollisionCountAsCopy())
        self.timeUntilCollision = self.particle1.collideParticle(self.particle2)
    
    def doCollision(self):
        self.particle1.bounceParticle(self.particle2)
    

    
class EventWallX(object):
    
    def __init__(self, particle):
        self.particle = particle
        self.id = self.particle.getCollisionCountAsCopy()
        self.timeUntilCollision = self.particle.collidesWallX()
    
    
    def isValid(self):
        return self.id == self.particle.getCollisionCountAsCopy()

    def reevaluateCollisionTime(self):
        self.id = self.particle.getCollisionCountAsCopy()
        self.timeUntilCollision = self.particle.collidesWallX()
    
    def doCollision(self):
        self.particle.bounceX()
    
class EventWallY(object):
    
    def __init__(self, particle):
        self.particle = particle
        self.id = self.particle.getCollisionCountAsCopy()
        self.timeUntilCollision = self.particle.collidesWallY()
        
    def isValid(self):
        return self.id == self.particle.getCollisionCountAsCopy()

    def reevaluateCollisionTime(self):
        self.id = self.particle.getCollisionCountAsCopy()
        self.timeUntilCollision = self.particle.collidesWallY()
    
    def doCollision(self):
        self.particle.bounceY()

        

class EventManager(object):
    
    def __init__(self, ListOfParticles):
        
        self.ListOfParticles = ListOfParticles
        self.ListOfEvents = []
        
        for (particle1, particle2) in combinations(self.ListOfParticles, 2):
            self.ListOfEvents.append(EventParticle(particle1, particle2))
            
        for particle in self.ListOfParticles:
            self.ListOfEvents.append(EventWallX(particle))
            self.ListOfEvents.append(EventWallY(particle))
        
        self.sortEventList()
        
        
            
    def sortEventList(self):
        
        def sorting_closure(event):
            if event.timeUntilCollision is None or event.timeUntilCollision < 0.0:
                return 1.0e7
            else:
                return event.timeUntilCollision
        
        self.ListOfEvents = sorted(self.ListOfEvents, key=sorting_closure)
        
    def step(self):
        
        for event in self.ListOfEvents:
            if not event.isValid():
                event.reevaluateCollisionTime()
        
        self.sortEventList()
        
        collTime = copy(self.ListOfEvents[0].timeUntilCollision)
        
        for particle in self.ListOfParticles:
            particle.advance(collTime)
            
        self.ListOfEvents[0].doCollision()
        
        for event in self.ListOfEvents:
            if event.timeUntilCollision is not None:
                event.timeUntilCollision -= collTime
            
if __name__ == '__main__':
    import numpy as np
    import pylab as plt
    
    a = Particle(np.array([0.1, 0.5]), np.array([0.01, 0.1]), 0.05, 2.0)
    b = Particle(np.array([0.4, 0.5]), np.array([-0.1, 0.01]), 0.05, 2.0)
    
    manager = EventManager([a,b])
    
    for i in range(20):
        plt.title(a.t)
        plt.scatter([a._x[0], b._x[0]], [a._x[1], b._x[1]])
        print a._x
        print b._x
        plt.xlim([0,1])
        plt.ylim([0,1])
        plt.show()
        
        manager.step()
        
        
        
            
        
        