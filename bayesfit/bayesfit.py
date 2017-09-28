# -*- coding: utf-8 -*-
"""
Created on Thu Sep 28 15:11:46 2017

@author: Mike
"""

import os as os 
import numpy as np
import warnings
from copy import deepcopy as _deepcopy
import scipy as sc 


def bayesfit(data, optionsIn):
    if not('optionsIn' in locals()): 
        options = dict()
    else:
        options = _deepcopy(optionsIn)
    if not('sigmoidName' in options.keys()):
        options['sigmoidName'] = 'norm'
    if not('threshPC' in options.keys()):
        options['threshPC'] = .75
        
    # Check sigmoid type provided 
    if options['sigmoidName'] in ['Weibull','weibull']:
        options['logspace'] = 1
        assert min(data[:,0]) > 0, 'The sigmoid you specified is not defined for negative data points!'
    else:
        options['logspace'] = 0
        
  