"""
This file contains the particle class for the molecular simulation of hard spheres
"""
import numpy as np
from copy import copy

class Particle(object):
    
    def __init__(self, location, velocity, radius, mass):
        
        self._x  = location
        self._v = velocity
        self._r = radius
        self._m = mass
        
        #Collision number
        self.NumberOfCollisions = 0
        
    
    def collidesWallX(self):
        if self._v[0]==0:
            return None
        
        if self.v[1] > 0.0:
            return (1.0 - self._r - self.x_x[0])/self._v[0]
        else:
            return (self._r - self.x_x[0])/self._v[0]
        
    def collidesWallY(self):
        if self._v[0]==0:
            return None
        
        if self.v[1] > 0.0:
            return (1.0 - self._r - self.x_x[0])/self._v[0]
        else:
            return (self._r - self.x_x[0])/self._v[0]
    
    def collideParticle(self, particle):
        
        deltax = self._x - particle._x
        deltav = self._v - particle._v
        R = self._r + particle._r
        
        d = np.dot(deltav, deltax)**2 - np.dot(deltav, deltav)*(np.dot(deltax, deltax) - R**2)
        
        if np.dot(deltav, deltax) >= 0:
            return None
        
        if d < 0:
            return None
        
        return -(np.dot(deltav, deltax)+np.sqrt(d))/(np.dot(deltav, deltav))
    
    
    def bounceX(self):
        pass
    
    def bounceY(self):
        pass
    
    def bounceParticle(self, particle):
        pass
    
    def getCollisionCountAsCopy(self):
        return copy(self.NumberOfCollisions)
        
    
    
            