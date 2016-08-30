# -*- coding: utf-8 -*-
"""
Created on Tue Aug 30 05:57:39 2016

@author: prateeksha
"""

import pandas as pd
import numpy as np
import plotly.plotly as py
import plotly.tools as tls
tls.set_credentials_file(username='PrateekshaKeshari', api_key='jtyjj31t0y')


import plotly.graph_objs as go
#train_data1 = pd.read_csv('train_data.csv', header=0)
#df=train_data1.ix[0:500,]
df=pd.read_csv('train_data.csv', header=0)
trace1 = go.Scatter(
                    x=df[' weekday_is_monday'], y=df[' shares'], # Data
                 #   mode='lines', name='shares' # Additional options
                   )
trace2 = go.Scatter(
                    x=df[' is_weekend'], y=df[' shares'], # Data
                 #   mode='lines', name='shares' # Additional options
                   )
                   
layout = go.Layout(title='Analysis on days Vs shares', plot_bgcolor='rgb(230, 230,230)')

fig = go.Figure(data=[trace1, trace2], layout=layout)

# Plot data in the notebook
py.image.save_as(fig, 'my_plot2.png')