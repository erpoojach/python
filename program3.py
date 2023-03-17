import sys
import os
sys.path.insert(0, os.getcwd())
import Modules.AreaInside as AreaInside

area = AreaInside.AreaofSquare(2)
print('area',area)
for path in sys.path:
    print(path)

import pyfiglet
Help(pyfiglet)
print(pyfiglet.figlet_format("welcome"))