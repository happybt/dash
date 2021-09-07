import plotly.plotly as pylt
import plotly.graph_objs as go

x = ['A', 'B', 'C', 'D', 'E']
y = ['W', 'X', 'Y', 'Z']

#       x0    x1    x2    x3    x4
z = [[0.00, 0.00, 0.75, 0.75, 0.00],  # y0
     [0.00, 0.00, 0.75, 0.75, 0.00],  # y1
     [0.75, 0.75, 0.75, 0.75, 0.75],  # y2
     [0.00, 0.00, 0.00, 0.75, 0.00]]  # y3

annotations = go.Annotations()
for n, row in enumerate(z):
    for m, val in enumerate(row):
        annotations.append(go.Annotation(text=str(z[n][m]), x=x[m], y=y[n],
                                         xref='x1', yref='y1', showarrow=False))

colorscale = [[0, '#3D9970'], [1, '#001f3f']]  # custom colorscale
trace = go.Heatmap(x=x, y=y, z=z, colorscale=colorscale, showscale=False)

fig = go.Figure(data=go.Data([trace]))
fig['layout'].update(
    title="Annotated Heatmap",
    annotations=annotations,
    xaxis=go.XAxis(ticks='', side='top'),
    yaxis=go.YAxis(ticks='', ticksuffix='  '),  # ticksuffix is a workaround to add a bit of padding
    width=700,
    height=700,
    autosize=False
)
print(pylt.plot(fig, filename='Stack Overflow 31756636', auto_open=False))
