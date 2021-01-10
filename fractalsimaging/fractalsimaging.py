'''
Import the libarires to get access to mathematical functions and imaging
'''
import numpy
from numba import jit
import matplotlib.pyplot as plt

''' 
The Mandelbrot Set:
For us define this as the set of complex numbers c such that when c are equated into the formula fc = z^2 + c, the formula was not 
diverge pass a distance of 2 from the origin of the complex plane. z0 = 0. The complex number with the formula a + bi, where
a is the real part which is represented on the x axis of the complex plane. And b is the imaginary part which is represented on the
y axis of the complex plain. If the complex number c when using the formula does not diverge is it colored black otherwise it is colored
based on the speed in which it grows. 
'''

'''
We defined our function which takes in the max number of iterations until we stop, the real part and imaginary part of the complex number
'''
@jit
def mandelbrot (maxIterations, realPart, imagPart):
    '''We set our c in the formula as the arguments taken from the function when called'''
    c = complex(realPart, imagPart)
    '''Set z as our 0'''
    z = 0.0j

    ''' We iterate to the max number of iterations we want'''
    for i in range(maxIterations):
        ''' We do the arithmetic for the formula '''
        z = z * z + c
        ''' 
        We check if the magnitude(modulus) of our current point is greater than a distance of 2 from the original point
        If so we break out of the loop and function
        '''
        if(z.real * z.real + z.imag * z.imag) >= 2:
            return 1

    return maxIterations

'''
We define our size and we create an array of zeros using numpy.zeros
'''

rowSize = 2000
columnSize = 2000

result = numpy.zeros([rowSize, columnSize])
'''
Row is our real axis and column is our imaginary axis of the complex place, here we enumerate the spacing of the graph,
Then we call in the mandelbrot function  
'''
for row_index, realPart in enumerate(numpy.linspace(-2, 1, num = rowSize)):
    for column_index, imagPart in enumerate(numpy.linspace(-2,1, num = columnSize)):
        result[row_index, column_index] = mandelbrot(300, realPart, imagPart)

'''
Set parameters and labels of the graphical representation 
'''
plt.figure(dpi = 100)
plt.imshow(result.T, cmap = 'hot', interpolation = 'nearest', extent = [-2,1,-1,1])
plt.xlabel("Real Axis")
plt.ylabel("Imaginary Axis")
plt.show()


'''
Additional features that could be implemented are the Julia set, Newton Fractal, Sierpinski, Koch and various other fractals than the
standard Mandelbrot set. Another point of interest may be to try and expand by using different methods and libraries (Specifically
Turtle) to generate a Mandelbrot set. Potential for expanding on this mini side project in the future.
'''