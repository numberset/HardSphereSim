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
        self.t = 0.0
        
        #Collision number
        self.NumberOfCollisions = 0
        
    
    def collidesWallY(self):
        if self._v[0]==0:
            return None
        
        if self._v[0] > 0.0:
            return (1.0 - self._r - self._x[0])/self._v[0]
        else:
            return (self._r - self._x[0])/self._v[0]
        
    def collidesWallX(self):
        if self._v[1]==0:
            return None
        
        if self._v[1] > 0.0:
            return (1.0 - self._r - self._x[1])/self._v[1]
        else:
            return (self._r - self._x[1])/self._v[1]
    
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
        self._v[1] = -self._v[1]
        self.NumberOfCollisions += 1
    
    def bounceY(self):
        self._v[0] = -self._v[0]
        self.NumberOfCollisions += 1
    
    def bounceParticle(self, particle):
        deltax = self._x - particle._x
        deltav = self._v - particle._v
        R = self._r + particle._r
        J = 2.0*self._m * particle._m *np.dot(deltav, deltax)/(R*(self._m + particle._m))

        Jx = J*(self._x[0]-particle._x[0])/R
        Jy = J*(self._x[1]-particle._x[1])/R
        
        self._v -= np.array([Jx/self._m, Jy/self._m])
        particle._v += np.array([Jx/particle._m, Jy/particle._m])
        
        self.NumberOfCollisions += 1
        particle.NumberOfCollisions += 1

    def getCollisionCountAsCopy(self):
        return copy(self.NumberOfCollisions)
    
    def advance(self, time):
        self._x += time*self._v
        self.t += time
    
if __name__ == '__main__':
    
    a = Particle(np.array([0.1, 0.5]), np.array([0.0, 0.0]), 0.05, 2.0)
    b = Particle(np.array([0.4, 0.5]), np.array([-0.1, 0.0]), 0.05, 2.0)
            
    print a.collideParticle(b)
    
    print b.collidesWallX()
    print b.collidesWallY()
    
    print "impulse before:", a._m*a._v + b._m*b._v
    print "energy before:", 0.5*a._m*np.dot(a._v,a._v) + 0.5*b._m*np.dot(b._v,b._v)
    
    b.advance(a.collideParticle(b))
    a.bounceParticle(b)
    
    print "impulse after:", a._m*a._v + b._m*b._v
    print "energy after:", 0.5*a._m*np.dot(a._v,a._v) + 0.5*b._m*np.dot(b._v,b._v)
    
    