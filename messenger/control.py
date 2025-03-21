########################################################################
# COMPONENT:
#    CONTROL
# Author:
#    Br. Helfrich, Kyle Mueller, <your name here if you made a change>
# Summary: 
#    This class stores the notion of Bell-LaPadula
########################################################################

from enum import IntEnum
class Control(IntEnum):
    PUBLIC = 1
    CONFIDENTIAL = 2
    PRIVILEGED = 3
    SECRET = 4