'''Calculate here the area and circumference of shape'''

from mypackage.interest_calculation import simple_interest
from mypackage.shape_calculation import area_of_circle, area_of_square


print(f'area of simple interest:  {simple_interest(1000,2,2.5)[0]}'
      f' Amount:{simple_interest(1000,2,2.5)[1]}')

print(f'Area of circle:{area_of_circle(2)} '
      f'Area of square:{area_of_square(5)} ')
