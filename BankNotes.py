# -*- coding: utf-8 -*-
"""
Created on Sun Oct 31 17:30:39 2021

@author: user
"""

from pydantic import BaseModel

# 2. Class which describes Bank Notes measurements
class BankNote(BaseModel):
    variance: float 
    skewness: float 
    curtosis: float 
    entropy: float