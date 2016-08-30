# -*- coding: utf-8 -*-
"""
Created on Tue Aug 30 21:18:47 2016

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
df =pd.read_csv('train_data.csv', header=0)
t =np.log(df[' n_tokens_title'])
trace1 = go.Scattergl(
                    x=t, y=df[' shares'], # Data
                    mode='markers', name='title words vs shares' # Additional options
                   )
#trace2 = go.Scattergl(
#                    x=df[' n_tokens_content'], y=df[' shares'], # Data
#                    mode='markers', name='content words vs shares' # Additional options
#                   )
##trace3 = go.Scatter(
#                    x=df[' n_unique_tokens'], y=df[' shares'], # Data
#                    mode='markers', name='rate of unique words vs shares' # Additional options
#                   )
##trace4 = go.Scatter(
#                    x=df[' n_non_stop_words'], y=df[' shares'], # Data
#                    mode='markers', name='rate of non stop words vs shares' # Additional options
#                   )
                   
                   
layout = go.Layout(title='log Title words vs shares', plot_bgcolor='rgb(230,230,230)')

fig = go.Figure(data=[trace1], layout=layout)

# Plot data in the notebook
py.image.save_as(fig, 'logfirstlineargl.png')