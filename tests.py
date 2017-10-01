# -*- coding: utf-8 -*-
"""
Created on Fri Sep 29 21:21:23 2017

@author: MetalHorse
"""

import bayesfit as bayesfit
import pandas as pd

# Import data as data frame into working environment using pandas
data = pd.read_csv('data.csv')

# Initialize options variable as dictionary type
options = dict()

# Determines the value of gamma (guess rate) to which the function is fit (default = 2)
# Note: 
options['nAFC'] = 0
# Determines the type of sigmoidal curve that is fit to the data (default = 'cnorm')
options['sigmoidType'] = 'weibull'

model = bayesfit_build(data, options)

fit = bayesfit(data,options,model)


params,threshold = bayesfit_extract(fit,options)


options['plot'] = 'cdf'
bayesfit_plot(data,fit,params,options)      
