Bayesian Psychometric Curve Fitting tool using STAN
====================================

.. image:: https://github.com/SlugocM/bayesfit/blob/master/logo.png
    :alt: BayesFit Logo
    :scale: 50 %

|pypi|

**BayesFit** provides a simple and easy to use interface to fit and plot psychometric functions by making use of pystan and Stan, which perform Bayesian inference using the No-U-Turn sampler.  

Important links
---------------
- Use documentation: https://slugocm.ca/BayesFit
- Source code repository: https://github.com/slugocm/bayesfit
- Issue tracker: https://github.com/slugocm/bayesfit/issues

- pystan documentation: https://pystan.readthedocs.org
- Stan: http://mc-stan.org/
- Stan User's Guide and Reference Manual (pdf) available at http://mc-stan.org


Basic Installation [Linux/ Windows/ macOS]
------------------

Packages required: 
- `PyStan <http://mc-stan.org/users/interfaces/pystan>`_
- `Scipy <https://www.scipy.org/>`_
- `Pandas <http://pandas.pydata.org/>`_
- `seaborn <https://seaborn.pydata.org/>`_


**RECOMMENDED:** BayesFit and required packages may be installed from the `Python Package Index
<https://pypi.python.org/pypi>`_ using ``pip``.

::

   pip install bayesfit

NOT RECOMMENDED BUT POSSIBLE: Alternatively, if required packages are already installed on your system, BayesFit can be installed via:

::

   git clone --recursive https://github.com/slugocm/bayesfit.git
   cd bayesfit
   python setup.py install


Example of use [Windows]
------------------
.. code-block:: python
    :linenos:
data = pd.read_csv('data.csv')




.. |pypi| image:: https://badge.fury.io/py/bayesfit.png
    :target: https://badge.fury.io/py/bayesfit
    :alt: pypi version
    
.. |travis| image:: https://travis-ci.org/slugocm/bayesfit.png?branch=master
    :target: https://travis-ci.org/slugocm/bayesfit
    :alt: travis-ci build status
