# -*- coding: utf-8 -*-
"""
Created on Sun Aug 20 20:07:26 2023

@author: Raam
"""

import pickle
from re import match
import pandas as pd
from datetime import date
import time
class file:
    def __init__(self,file_name):
        self.file_name=file_name
        self.route="root/"
        self.text=""