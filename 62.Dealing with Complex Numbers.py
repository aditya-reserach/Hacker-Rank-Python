"""
Problem Statement:
------------------
For this challenge, you are given two complex numbers, and you have to print the result of their 
addition, subtraction, multiplication, division and modulus operations.

The real and imaginary precision part should be correct up to two decimal places.

Input Format:
-------------
One line of input: The real and imaginary part of a number separated by a space.

Output Format:
--------------
For two complex numbers A and B, the output should be in the following sequence on separate lines:
1. A + B
2. A - B
3. A * B
4. A / B
5. mod(A)
6. mod(B)

Formatting Rules:
-----------------
- For complex numbers with non-zero real and complex part, the output should be in the format:
  a+bi  or  a-bi
- Replace the plus symbol with a minus when the imaginary part is negative.
- For complex numbers with a zero complex part, output should be:
  a.00+0.00i
- For complex numbers where the real part is zero and the imaginary part is non-zero, output should be:
  0.00+bi  or  0.00-bi

Sample Input:
-------------
2 1
5 6

Sample Output:
--------------
7.00+7.00i
-3.00-5.00i
4.00+17.00i
0.26-0.11i
2.24+0.00i
7.81+0.00i

Concept:
--------
Python is a fully object-oriented language like C++, Java, etc.
- Methods with a double underscore before and after their name are built-in methods.
- These allow operator overloading for custom classes.
  __add__   -> for + operator
  __sub__   -> for - operator
  __mul__   -> for * operator
  __truediv__ -> for / operator
  __str__   -> for string representation
"""

# ============================================================
# SOLUTION 1: Using Python’s built-in complex type (HackerRank style)
# ============================================================

# This solution leverages Python's built-in support for complex numbers.
# Python already has a `complex` type which directly supports addition,
# subtraction, multiplication, division, and modulus (abs).
# We only need to format the output properly.

# Step 1: Import the math library (to compute modulus manually if needed)
import math

# Step 2: Read input values for first complex number
c = map(float, input().split())  # Reads input, splits by space, converts to float
d = map(float, input().split())  # Reads second complex number

# Step 3: Create complex numbers using Python's built-in `complex` type
x = complex(*c)  # unpack real and imaginary parts into complex()
y = complex(*d)

# Step 4: Define a helper function to format complex numbers in the required style
def format_complex(z):
    # Extract real and imaginary parts
    real = z.real
    imag = z.imag
    
    # Case 1: purely real
    if imag == 0:
        return "%.2f+0.00i" % (real)
    # Case 2: purely imaginary
    elif real == 0:
        if imag >= 0:
            return "0.00+%.2fi" % (imag)
        else:
            return "0.00-%.2fi" % (abs(imag))
    # Case 3: both real and imaginary
    else:
        if imag > 0:
            return "%.2f+%.2fi" % (real, imag)
        else:
            return "%.2f-%.2fi" % (real, abs(imag))

# Step 5: Perform operations using Python built-in complex arithmetic
results = [
    x + y,       # addition
    x - y,       # subtraction
    x * y,       # multiplication
    x / y,       # division
    abs(x),      # modulus of x
    abs(y)       # modulus of y
]

# Step 6: Format modulus values to match required Complex class style
# Wrapping modulus in a fake complex number for consistency
formatted_results = []
for idx, res in enumerate(results):
    if idx < 4:  # first four are complex numbers
        formatted_results.append(format_complex(res))
    else:  # modulus results
        formatted_results.append(format_complex(complex(res, 0)))

# Step 7: Print results, each on a new line
print(*formatted_results, sep="\n")

# ------------------------------------------------------------
# Time Complexity Analysis (Solution 1):
# - Input reading: O(1) (two numbers only)
# - Each arithmetic operation on complex numbers: O(1)
# - Formatting: O(1)
# Total = O(1)
#
# Space Complexity Analysis (Solution 1):
# - We store two inputs, results list of 6 elements = O(1)
# Total = O(1)
# ------------------------------------------------------------


# ============================================================
# SOLUTION 2: Manual Implementation with Custom Complex Class
# ============================================================

# Step 1: Define Complex class
class Complex(object):
    def __init__(self, real, imaginary):
        # Store real and imaginary parts
        self.real = real
        self.imaginary = imaginary

    def __add__(self, no):
        # Add real with real, imaginary with imaginary
        return Complex(self.real + no.real, self.imaginary + no.imaginary)

    def __sub__(self, no):
        # Subtract real with real, imaginary with imaginary
        return Complex(self.real - no.real, self.imaginary - no.imaginary)

    def __mul__(self, no):
        # (a+bi)(c+di) = (ac - bd) + (ad + bc)i
        real_part = self.real * no.real - self.imaginary * no.imaginary
        imag_part = self.real * no.imaginary + self.imaginary * no.real
        return Complex(real_part, imag_part)

    def __truediv__(self, no):
        # (a+bi)/(c+di) = [(ac+bd) + (bc - ad)i] / (c^2 + d^2)
        denominator = no.real ** 2 + no.imaginary ** 2
        real_part = (self.real * no.real + self.imaginary * no.imaginary) / denominator
        imag_part = (self.imaginary * no.real - self.real * no.imaginary) / denominator
        return Complex(real_part, imag_part)

    def mod(self):
        # modulus = sqrt(a^2 + b^2)
        modulus = math.sqrt(self.real ** 2 + self.imaginary ** 2)
        return Complex(modulus, 0)

    def __str__(self):
        # Formatting rules as per problem statement
        if self.imaginary == 0:
            result = "%.2f+0.00i" % (self.real)
        elif self.real == 0:
            if self.imaginary >= 0:
                result = "0.00+%.2fi" % (self.imaginary)
            else:
                result = "0.00-%.2fi" % (abs(self.imaginary))
        elif self.imaginary > 0:
            result = "%.2f+%.2fi" % (self.real, self.imaginary)
        else:
            result = "%.2f-%.2fi" % (self.real, abs(self.imaginary))
        return result

# Step 2: Input reading again for second solution
c = map(float, input().split())
d = map(float, input().split())
x = Complex(*c)
y = Complex(*d)

# Step 3: Perform operations
# List of results in required order
results = [x+y, x-y, x*y, x/y, x.mod(), y.mod()]

# Step 4: Print each result using __str__ automatically
print(*map(str, results), sep="\n")

# ------------------------------------------------------------
# Time Complexity Analysis (Solution 2):
# - Each operation (add, sub, mul, div, mod): O(1)
# - Input reading: O(1)
# - Printing: O(1)
# Total = O(1)
#
# Space Complexity Analysis (Solution 2):
# - We store two input Complex objects, and 6 results = O(1)
# Total = O(1)
# ------------------------------------------------------------
