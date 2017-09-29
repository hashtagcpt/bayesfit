"""
 BAYESFIT (MAIN FILE) 
 Created by: Michael Slugocki
 Created on: September 28, 2017
 License: Apache 2.0
"""

# Import modules
import os as os 
import numpy as np
import warnings
from copy import deepcopy 
import scipy as sc 
import pystan as ps 
import pandas as pd

# Define wrapper function
def bayesfit(data, optin):

    # Check data structure inputted and convert to format required if possible
    # Format requested is a N x 3 data frame such that [x, y, N]
    if data.shape[1] != 3:
        raise Exception('Data provided does not contain the number of columns required! (i.e., [x, y, N])') 

    # Check user input for options
    if not('optin' in locals()): 
        options = dict()
    else:
        options = deepcopy(optin)
    if not('sigmoidType' in options.keys()):
        options['sigmoidType'] = 'weibull'
    if not('thresholdPC' in options.keys()):
        options['thresholdPC'] = .75
    if not('nAFC' in options.keys()):
        options['nAFC'] = 2
    if not('lapse' in options.keys()):
        options['lapse'] = True
    if not('fit' in options.keys()):
        options['fit'] = 'auto'
    # Check sigmoid type provided to convert to logspace where necessary 
#    if options['sigmoidType'] in ['Weibull','weibull']:
#        options['logspace'] = 1
#        assert min(data[:,0]) > 0, 'The sigmoid you specified is not defined for negative data points!'
#    else:
#        options['logspace'] = 0

    # File that performs main computation
    output = bayesfit_build(data,options)
        
    return fit


# Define core fitting 
def bayesfit_build(data,options):
    
    # Convert from average to numerical 1 and 0 sequence
    df = pd.DataFrame([],columns=['x','y']) 
    for i in range(len(data.x)):
        approx_numsequence = np.round(data.y[i]*data.N[i])   
        response_y = np.zeros(data.N[i])
        response_y[:int(approx_numsequence)] = 1
        response_x = np.repeat(data.x[i],data.N[i])
        tmp_df = pd.DataFrame(np.column_stack((response_x,response_y)), columns=['x','y'])
        df = df.append(tmp_df)
    
    model_definition = dict()
    if options['fit'] == 'auto':
        model_definition['data'] = '''
            data {
            int<lower=1> N;
            vector[N] x;
            int<lower=0,upper=1> y[N];
            }'''    
        if options['lapse'] == True:
            model_definition['parameters'] = '''
                parameters {
                real<lower=0> alpha;
                real<lower=0> beta;
                real<lower=0> lambda;
                }'''
        else:     
            model_definition['parameters'] = '''
                parameters {
                real<lower=0> alpha;
                real<lower=0> beta;
                }'''
        # Get initial estimate of alpha via linear regression
        def alpha_est(data,options):
            y = [data.y[0], data.y[data.y.shape[0]-1]]
            x = [data.x[0], data.x[data.x.shape[0]-1]] 
            init_alpha = np.polyfit(x, y, 1)
            alpha_estimate = [(0.70 - init_alpha[1]) / init_alpha[0]]
            return alpha_estimate[0]
        # Use function to obtain estimate of alpha     
        alpha_guess = alpha_est(data, options)

        # Set up likelihoods 
        model_definition['likelihood_start'] = '''        
            model {'''
        model_definition['likelihood_alpha'] = ('''alpha ~ normal(%f,3);''' %(alpha_guess))
        model_definition['likelihood_beta'] = '''   
            beta ~ normal(3,5);'''
        # This section is repeated for interpretability     
        if options['lapse'] == True:
            model_definition['likelihood_lambda'] = '''   
                lambda ~ beta(2,20);'''    
        else: 
            model_definition['likelihood_lambda'] = '''  '''  

        # Define Bernoulli distro
        # Define gamma
        gamma = 1/options['nAFC']
        
        model_definition['likelihood_model_start'] = '''
            for (i in 1:N){'''
        model_definition['likelihood_model_middle'] = (''' y[i] ~ bernoulli(%f + (1-lambda-%f)*weibull_cdf(x[i],beta, alpha));} ''' %(gamma, gamma))
        model_definition['likelihood_model_end'] = ''' } '''

        # Combine full model together
        model_definition['full_model'] = model_definition['data'] + model_definition['parameters'] + model_definition['likelihood_start'] + model_definition['likelihood_alpha'] + model_definition['likelihood_beta'] + model_definition['likelihood_lambda'] + model_definition['likelihood_model_start'] +model_definition['likelihood_model_middle'] + model_definition['likelihood_model_end'] 

    # Convert data frame above to list 
    x = [int(i) for i in pd.Series.tolist(df.x)]
    y = [int(i) for i in pd.Series.tolist(df.y)]
    data_model= {'N': len(df.x),'x': x,'y': y}
    model = ps.StanModel(model_code = model_definition['full_model']) 
    fit = model.sampling(data=data_model, iter=1000, chains=1)

    


    
    
  