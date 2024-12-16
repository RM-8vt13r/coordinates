import cupy as cp
import numpy as np

def polar2cartesian(coordinates):
    '''
    Convert polar coordinates to cartesian coordinates
    
    Inputs:
    - coordinates: [...,2] where the last dimension contains magnitude, orientation in radians
    
    Outputs:
    - coordinates where the last dimension contains x, y
    '''
    if isinstance(coordinates, cp.ndarray): np = cp
    x = (coordinates[...,-2]*np.cos(coordinates[...,-1]))[...,None]
    y = (coordinates[...,-2]*np.sin(coordinates[...,-1]))[...,None]
    cartesian_coordinates = np.concatenate([x, y], axis=-1)
    return cartesian_coordinates

def cartesian2polar(coordinates):
    '''
    Convert cartesian coordinates to polar coordinates
    
    Inputs:
    - coordinates: [...,2] where the last dimension contains x,y
    
    Outputs:
    - coordinates where the last dimension contains magnitude, orientation in radians
    '''
    if isinstance(coordinates, cp.ndarray): np = cp
    magnitudes = np.sqrt(np.sum(coordinates**2, axis=-1))[...,None]
    orientations = np.arctan2(coordinates[...,-1], coordinates[...,-2])[...,None]
    polar_coordinates = np.concatenate([magnitudes, orientations], axis=-1)
    return polar_coordinates
