"""
Problem Statement:
------------------
You are given four points in a 3-dimensional Cartesian coordinate system. 
You are required to print the angle (in degrees, not radians) between 
the two planes formed by these points.

Mathematically:
---------------
Let the angle be θ.

θ = arccos( (x . y) / (|x| * |y|) )

Where:
- "x . y" is the dot product of vectors x and y.
- "|" denotes the magnitude (length) of a vector.
- "x × y" is the cross product of vectors x and y.

Here:
- x = (B - A) × (C - B)
- y = (C - B) × (D - C)

Input Format:
-------------
One line of input containing the space separated floating number 
values of the x, y, z coordinates of 4 points.

That is, 4 lines follow, each containing 3 floating-point numbers.

Output Format:
--------------
Output the angle correct up to two decimal places.

Constraints:
------------
- Coordinates are floating point numbers.
- Points are distinct.
- 3D Cartesian coordinate geometry rules apply.

Sample Input:
-------------
0 4 5
1 7 6
0 5 9
1 7 2

Sample Output:
--------------
8.19
"""

# ============================================================
# SOLUTION 1: Using Python built-ins (NumPy for vector math)
# ============================================================

import math                     # Import math module for trigonometric functions
import numpy as np              # Import numpy for vector/matrix operations

# Step 1: Read input points
points = []                     # Empty list to store the 4 points
for i in range(4):              # Loop to read 4 lines
    a = list(map(float, input().split()))  # Convert each line into a list of floats
    points.append(a)            # Append to the points list

# Step 2: Convert points to numpy arrays
A, B, C, D = map(np.array, points)   # Convert list of lists into numpy arrays

# Step 3: Define vectors for cross products
AB = B - A                        # Vector from A to B
BC = C - B                        # Vector from B to C
CD = D - C                        # Vector from C to D

# Step 4: Compute normals of planes using cross product
x = np.cross(AB, BC)              # Normal to plane ABC
y = np.cross(BC, CD)              # Normal to plane BCD

# Step 5: Compute dot product and magnitudes
dot = np.dot(x, y)                # Dot product of normals
mag_x = np.linalg.norm(x)         # Magnitude of normal x
mag_y = np.linalg.norm(y)         # Magnitude of normal y

# Step 6: Calculate angle
angle_rad = math.acos(dot / (mag_x * mag_y))  # Angle in radians
angle_deg = math.degrees(angle_rad)           # Convert to degrees

# Step 7: Print result rounded to 2 decimal places
print("%.2f" % angle_deg)


# ------------------------------------------------------------------------
# Time Complexity (Solution 1):
# - Reading input: O(1) (fixed 4 points)
# - Cross product: O(1) (3D vectors, constant time)
# - Dot product: O(1)
# - Norm (magnitude): O(1)
# Overall: O(1)
#
# Space Complexity (Solution 1):
# - Storing 4 points: O(1)
# - Storing temporary vectors: O(1)
# Overall: O(1)
# ------------------------------------------------------------------------


# ============================================================
# SOLUTION 2: Manual implementation (No numpy)
# ============================================================

class Points(object):
    def __init__(self, x, y, z):
        # Store coordinates of the point/vector
        self.x = x
        self.y = y
        self.z = z

    def __sub__(self, no):
        # Subtract two vectors (self - no)
        return Points(self.x - no.x, self.y - no.y, self.z - no.z)

    def dot(self, no):
        # Dot product of two vectors
        return self.x * no.x + self.y * no.y + self.z * no.z

    def cross(self, no):
        # Cross product of two vectors
        return Points(
            self.y * no.z - self.z * no.y,
            self.z * no.x - self.x * no.z,
            self.x * no.y - self.y * no.x
        )

    def absolute(self):
        # Magnitude of a vector
        return math.sqrt(self.x ** 2 + self.y ** 2 + self.z ** 2)


# Step 1: Read input again (for manual solution)
points = []
for i in range(4):                        # Read 4 lines again
    a = list(map(float, input().split())) # Convert to list of floats
    points.append(a)

# Step 2: Create Points objects
a, b, c, d = Points(*points[0]), Points(*points[1]), Points(*points[2]), Points(*points[3])

# Step 3: Compute cross products for normals
x = (b - a).cross(c - b)                  # Normal to plane ABC
y = (c - b).cross(d - c)                  # Normal to plane BCD

# Step 4: Compute angle using dot product and magnitudes
angle = math.acos(x.dot(y) / (x.absolute() * y.absolute()))

# Step 5: Print result in degrees
print("%.2f" % math.degrees(angle))


# ------------------------------------------------------------------------
# Time Complexity (Solution 2):
# - Reading input: O(1) (fixed 4 points)
# - Subtraction: O(1) (3 operations)
# - Cross product: O(1) (9 multiplications, 6 subtractions)
# - Dot product: O(1) (3 multiplications, 2 additions)
# - Magnitude: O(1) (3 multiplications, 2 additions, 1 sqrt)
# Overall: O(1)
#
# Space Complexity (Solution 2):
# - Storing 4 points: O(1)
# - Creating vectors for cross/dot: O(1)
# Overall: O(1)
# ------------------------------------------------------------------------

