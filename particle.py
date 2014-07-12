"""
This file contains the particle class for the molecular simulation of hard spheres
"""

class Particle(object):
    
    def __init__(self, location, velocity, radius):
        
        self._x  = location
        self._v = velocity
        self._r = radius
        
    
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
    
    
            