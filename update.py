import os
import platform
from subprocess import call
Os=platform.system()
if Os == "Windows":
    pass
else:
    call(['wget','https://github.com/brozorb/CalcGame/archive/main.zip'])
    call(['unzip','main.zip','-u'])
