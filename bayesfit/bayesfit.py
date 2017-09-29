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
import statsmodels.api as sm

# Define wrapper function
def bayesfit(data, optin):

    # Check data structure inputted and convert to format required if possible
    # Format requested is a N x 3 matrix such that [x, y, N]
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
    if options['sigmoidType'] in ['Weibull','weibull']:
        options['logspace'] = 1
        assert min(data[:,0]) > 0, 'The sigmoid you specified is not defined for negative data points!'
    else:
        options['logspace'] = 0

    # File that performs main computation
    output = bayesfit_main(data,options)
        
    return output


# Define core fitting 
def bayesfit_main(data,options):
    
    gamma = 1/options['nAFC']

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
            if options['fit'] == 'auto':
            y = [data[0,1], data[len(data[:,1]),1]]
            x = [data[0,0], data[len(data[:,0]),0]] 
            init_alpha = np.polyfit(x, y, 1)
            alpha_estimate = [(0.70 - init_alpha[1]) / init_alpha[0]]
            return alpha_estimate  
        # Use function to obtain estimate of alpha     
        alpha_guess = alpha_est(data, options)

        # Set up likelihoods 
        model_definition['likelihood_start'] = '''        
            model {'''
        model_definition['likelihood_alpha'] = 
            ('''alpha ~ normal(%f,3);''' %(alpha))
        model_definition['likelihood_beta'] = '''   
            beta ~ normal(3,5);'''
        # This section is repeated for interpretability     
        if options['lapse'] == True:
            model_definition['likelihood_lambda'] = '''   
                lambda ~ beta(2,20);'''    
        else: 
            model_definition['likelihood_lambda'] = '''  '''  

        # Define Bernoulli distro
        model_definition['likelihood_start'] = '''
            for (i in 1:N){'''
        if options['lapse'] == True:
            model_definition['likelihood_middle'] =     
            (''' y[i] ~ bernoulli(%f + (1-lambda-%f)*weibull_cdf(x[i],beta, alpha));} ''' %(gamma, gamma))
        else:
        model_definition['likelihood_end'] = ''' } '''

        # Combine full model together
        model_definition['full_model'] = model_definition['data'] + 
            model_definition['parameters'] + 
            model_definition['likelihood_start'] + 
            model_definition['likelihood_alpha'] + 
            model_definition['likelihood_beta'] + 
            model_definition['likelihood_lambda'] + 
            model_definition['likelihood_start'] +
            model_definition['likelihood_middle'] +
            model_definition['likelihood_end'] +

    # Pool data types together 
    data_dict = {'N': data[1,2],'x': data[:,0],'y': data[:,1]}
    fit = ps.stan(model_code = model_definition['full_model'], data=data_dict, iter=1000, chains=1)  
    


x1 = np.array([1,2,3,4,5])        
x = np.repeat(x1,5)
y = np.array([1,0,0,0,0,0,1,0,0,0,1,1,1,1,0,0,1,1,1,1,1,1,1,1,1])
y1 = [0.2,0.2,0.8,0.8,1]


        

    
    


    
    
    
    
    
    
    
    
        
  