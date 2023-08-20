# -*- coding: utf-8 -*-
"""
Created on Sun Aug 20 20:04:59 2023

@author: Raam
"""
import pickle
from re import match
import pandas as pd
from datetime import date
import time
class folder:
    def __init__(self,folder_name):
        self.father=None
        self.files=[]
        self.files_names=[]
        self.folder_name=folder_name
        self.route="root/"