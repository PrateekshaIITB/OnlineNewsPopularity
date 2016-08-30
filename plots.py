


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
                    x=df[' weekday_is_tuesday'], y=df[' shares'], # Data
                 #   mode='lines', name='shares' # Additional options
                   )
trace3 = go.Scatter(
                    x=df[' weekday_is_wednesday'], y=df[' shares'], # Data
                 #   mode='lines', name='shares' # Additional options
                   )
trace4 = go.Scatter(
                    x=df[' weekday_is_thursday'], y=df[' shares'], # Data
                 #   mode='lines', name='shares' # Additional options
                   )
trace5 = go.Scatter(
                    x=df[' weekday_is_friday'], y=df[' shares'], # Data
                 #   mode='lines', name='shares' # Additional options
                   )
trace6 = go.Scatter(
                    x=df[' is_weekend'], y=df[' shares'], # Data
                #    mode='lines', name='shares' # Additional options
                   )

                 
layout = go.Layout(title='Analysis on days vs shares',
                   plot_bgcolor='rgb(230, 230,230)')

fig = go.Figure(data=[trace1, trace2, trace3, trace4, trace5, trace6], layout=layout)

# Plot data in the notebook
py.image.save_as(fig, 'my_plot.png')