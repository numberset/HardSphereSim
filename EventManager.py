"""
Module defining the Event class which is used to manage collissions and check their validity
"""

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
        self.reevaluateCollisionTime()
    

    
class EventWallX(object):
    
    def __init__(self, particle):
        self.particle = particle
        self.id = self.particle.getCollisionCountAsCopy()
        self.timeUntilCollision = self.particle.collideWallX()
    
    
    def isValid(self):
        return self.id == self.particle.getCollisionCountAsCopy()

    def reevaluateCollisionTime(self):
        self.id = self.particle1.getCollisionCountAsCopy()
        self.timeUntilCollision = self.particle.collideWallX()
    
    def doCollision(self):
        self.particle1.bounceX()
        self.reevaluateCollisionTime()
    
class EventWallY(object):
    
    def __init__(self, particle):
        self.particle = particle
        self.id = self.particle.getCollisionCountAsCopy()
        self.timeUntilCollision = self.particle.collideWallY()
        
    def isValid(self):
        return self.id == self.particle.getCollisionCountAsCopy()

    def reevaluateCollisionTime(self):
        self.id = self.particle1.getCollisionCountAsCopy()
        self.timeUntilCollision = self.particle.collideWallY()
    
    def doCollision(self):
        self.particle1.bounceY()
        self.reevaluateCollisionTime()