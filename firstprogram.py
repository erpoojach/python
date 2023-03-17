print("Hello")

#math usage
import math
valsquare = 25
square = math.sqrt(valsquare)
print(square)
#print("square of "+valsquare+" is " + square)


power = math.pow(2,3)
print(power)

dir(math) #for more details : google Python 3 math module
math.pi
floor = math.floor(4.3) 
print(floor)

ceil = math.ceil(4.3) 
print(ceil)

#Calender usage
import calendar
calmonth = calendar.month(2018,8)
calleap = calendar.isleap(2018)
caldir = dir(calendar)
print(calmonth)
print(calleap)
print(caldir)

#import custom module

import Area
areaoftriangle = Area.AreaofTraiangle(10,20)
print('areaoftriangle ',areaoftriangle)

AreaOfSquare = Area.AreaOfSquare(5)
print('AreaOfSquare ',AreaOfSquare)


