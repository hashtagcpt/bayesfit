# -*- coding: utf-8 -*-
"""
Created on Tue Oct  3 14:03:30 2017

@author: Mike
"""

import pandas as pd
import bayesfit as bf




def _normal():
    # Generate test data 
    x = [1, 2, 3, 4, 5, 6, 7]
    y = [0.01, 0.08, 0.2, 0.45, 0.75, 0.89, 0.98]
    N = [20, 20, 20, 20, 20, 20, 20]
    data = pd.DataFrame({'x':x, 'y':y, 'N':N})
    # Initialize options variable as dictionary type
    options = dict()
    # Determines the value of gamma (guess rate) to which the function is fit (default = 2)
    options['nAFC'] = 0
    # Define function
    options['sigmoidType'] = 'cnorm'
    # Define lapse rate
    options['lapse'] = True
    # Define fit 
    options['fit'] = 'auto'
    # Build model 
    model = bf.bayesfit_build(data, options)
    # Determine success
    success = 1
    return success

def _logistic():
    # Generate test data 
    x = [1, 2, 3, 4, 5, 6, 7]
    y = [0.01, 0.08, 0.2, 0.45, 0.75, 0.89, 0.98]
    N = [20, 20, 20, 20, 20, 20, 20]
    data = pd.DataFrame({'x':x, 'y':y, 'N':N})
    # Initialize options variable as dictionary type
    options = dict()
    # Determines the value of gamma (guess rate) to which the function is fit (default = 2)
    options['nAFC'] = 0
    # Define function
    options['sigmoidType'] = 'logistic'
    # Define lapse rate
    options['lapse'] = True
    # Define fit 
    options['fit'] = 'auto'
    # Build model 
    model = bf.bayesfit_build(data, options)
    # Determine success
    success = 1
    return success

def _cauchy():
    # Generate test data 
    x = [1, 2, 3, 4, 5, 6, 7]
    y = [0.01, 0.08, 0.2, 0.45, 0.75, 0.89, 0.98]
    N = [20, 20, 20, 20, 20, 20, 20]
    data = pd.DataFrame({'x':x, 'y':y, 'N':N})
    # Initialize options variable as dictionary type
    options = dict()
    # Determines the value of gamma (guess rate) to which the function is fit (default = 2)
    options['nAFC'] = 0
    # Define function
    options['sigmoidType'] = 'cauchy'
    # Define lapse rate
    options['lapse'] = True
    # Define fit 
    options['fit'] = 'auto'
    # Build model 
    model = bf.bayesfit_build(data, options)
    # Determine success
    success = 1
    return success

def _weibull():
    # Generate test data 
    x = [1, 2, 3, 4, 5, 6, 7]
    y = [0.01, 0.08, 0.2, 0.45, 0.75, 0.89, 0.98]
    N = [20, 20, 20, 20, 20, 20, 20]
    data = pd.DataFrame({'x':x, 'y':y, 'N':N})
    # Initialize options variable as dictionary type
    options = dict()
    # Determines the value of gamma (guess rate) to which the function is fit (default = 2)
    options['nAFC'] = 0
    # Define function
    options['sigmoidType'] = 'weibull'
    # Define lapse rate
    options['lapse'] = True
    # Define fit 
    options['fit'] = 'auto'
    # Build model 
    model = bf.bayesfit_build(data, options)
    # Determine success
    success = 1
    return success



def test_normal():
    assert _normal() == 1

def test_logistic():
    assert _logistic() == 1
    
def test_cauchy():
    assert _cauchy() == 1
    
def test_weibull(ata):
    assert _weibull() == 1
