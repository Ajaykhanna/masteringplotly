import chart_studio.plotly as plotly
import plotly.graph_objs as go

## Offline Mode
from plotly.offline import download_plotlyjs, init_notebook_mode, plot, iplot
init_notebook_mode(connected=True)

trace1 = go.Scatter(x=[1, 2, 3], y=[4, 3, 2],
                    name='Main Graph',)
trace2 = go.Scatter(x=[20, 30, 40], y=[30, 40, 50],
                    xaxis='x2', yaxis='y2',
                    name='Inset')

data = [trace1, trace2]

layout = go.Layout(
    title='Simple Inset Graph With Plotly',
    title_x=0.5,
    xaxis=dict(title='X-axis'),
    yaxis=dict(title='Y-axis'),
    xaxis2=dict(domain=[0.6, 1.0], anchor='y2'),
    yaxis2=dict(domain=[0.6, 1.0], anchor='x2'))

fig = go.Figure(data=data, layout=layout)
iplot(fig, filename='simple-inset')
