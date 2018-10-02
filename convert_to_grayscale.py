# -*- coding: utf-8 -*-
"""
Created on Tue Oct  2 12:25:56 2018

@author: hasee
"""
import numpy as np
from PIL import Image

img = Image.open('cr.png').convert('LA')


img.save('graycr.png')