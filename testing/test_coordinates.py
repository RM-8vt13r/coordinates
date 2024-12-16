import sys
sys.path.append('src')
import numpy as np
from math import pi

import coordinates as c

def test_coordinates():
    cartesian = np.array([[1, 0], [-1, 0], [0, 2], [0, -np.sqrt(2)], [2, 2]])
    polar = np.array([[1, 0], [1, pi], [2, pi/2], [np.sqrt(2), -pi/2], [np.sqrt(8), pi/4]])
    calculated_polar = c.cartesian2polar(cartesian)
    calculated_cartesian = c.polar2cartesian(polar)
    
    assert np.all(np.isclose(polar[:,0], calculated_polar[:,0]) & np.isclose(polar[:,1]%(2*pi), calculated_polar[:,1]%(2*pi))), f"cartesian2polar yields {calculated_polar}, but should be {polar}"
    assert np.all(np.isclose(cartesian, calculated_cartesian)), f"polar2cartesian yields {calculated_cartesian}, but should be {cartesian}"
