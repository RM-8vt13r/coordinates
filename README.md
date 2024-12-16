Module that is used to convert between cartesian and polar 2D coordinates in various other MPE repositories  
  
Files:
- coordinates.py: convert between cartesian and polar coordinates

Installation:
`pip install git+https://gitlab.tudelft.nl/medical-process-engineering/coordinates.git`

Usage:
```python
import numpy as np
from coordinates import cartesian2polar, polar2cartesian

# Generate coordinates
# Arbitrary dimensions supported, as long as the last dimension has length 2
# For cartesian coordinates, the last dimension contains x,y
# For polar coordinates, the last dimension contains magnitude,orientation (in radians)
cartesian_coordinates = np.random.randint(low=-10, high=11, size=(10, 11, 12, 2))

# Conversion
polar_coordinates     = cartesian2polar(cartesian_coordinates)
cartesian_coordinates = polar2cartesian(polar_coordinates)
```

Testing:
`pytest testing/`