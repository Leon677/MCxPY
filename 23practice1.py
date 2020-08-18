# -*- coding: utf-8 -*-
"""
Created on Tue Aug 18 11:57:45 2020

@author: user
"""

  
from mcpi.minecraft import Minecraft
import time
import random
mc=Minecraft.create()
color=random.randrange(0,9)
while True:
    x,y,z=mc.player.getPos()
    mc.setBlock(x,y,z,38,color)
    time.sleep(0.5)
    color=random.randrange(0,9)