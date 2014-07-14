"""
Module defining the Event class which is used to manage collissions and check their validity
"""

class EventParticle(object):
    
    def __init__(self, particle1, particle2):
        self.particle1 = particle1
        self.particle2 = particle2
        
        
        self.id = (self.particle1.getCollisionCountAsCopy(), self.particle2.getCollisionCountAsCopy())
        self.timeUntilCollision = self.particle1.collideParticle(self.particle2)
    
class EventWallX(object):
    
    def __init__(self, particle):
        self.particle = particle
        self.id = self.particle.getCollisionCountAsCopy()
        self.timeUntilCollision = self.particle.collideWallX()
    
class EventWallY(object):
    
    def __init__(self, particle):
        self.particle = particle
        self.id = self.particle.getCollisionCountAsCopy()
        self.timeUntilCollision = self.particle.collideWallY()