'''Area,Circumfenrence of SQ,RECT,CIRCLE'''
import math
from math import pi,sqrt

def area_of_square(side):
    ''' Return the area of Square'''
    return side*side

def area_of_circle(radius):
    ''' Return the area of Circle'''
    return pi*radius**2

def area_of_rectangle(length,bredth):
    ''' Return the area of Rectangle'''
    return length*bredth

def circumference_of_circle(radius):
    ''' Return the circumeference of Circle'''
    return 2*pi*radius
