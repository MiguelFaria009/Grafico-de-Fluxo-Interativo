import plotly.graph_objects as go
from plotly.subplots import make_subplots
import numpy as np

# Data generation
def generate_data(num_points, func_type='sin_cos'):
    x = np.linspace(0, 10, num_points)
    if func_type == 'sin_cos':
        y1 = np.sin(x)
        y2 = np.cos(x)
        return x, [y1, y2], ['Seno', 'Cosseno']
    elif func_type == 'sin_tan':
        y1 = np.sin(x)
        y2 = np.tan(x) / 2  # Scale tan to avoid extreme values
        return x, [y1, y2], ['Seno', 'Tangente']
    else:  # cos_tan
        y1 = np.cos(x)
        y2 = np.tan(x) / 2
        return x, [y1, y2], ['Cosseno', 'Tangente']

# Create interactive streamgraph
def create_streamgraph(baseline='wiggle', num_points=100, func_type='sin_cos'):
    x, ys, labels = generate_data(num_points, func_type)
    
    fig = go.Figure()
    
    # Add traces for each dataset
    for y, label in zip(ys, labels):
        fig.add_trace(go.Scatter(
            x=x, y=y,
            mode='lines',
            fill='tonexty' if baseline != 'zero' else 'tozeroy',
            stackgroup='one',
            name=label
        ))
    
    # Update layout for baseline and styling
    if baseline == 'wiggle':
        # Approximate wiggle by adjusting the mean of the stacked data
        total = np.sum(ys, axis=0)
        mean = total.mean()
        for trace in fig.data:
            trace.y = trace.y - mean / len(ys)
    
    fig.update_layout(
        title='Gráfico de Fluxo Interativo',
        xaxis_title='Eixo X',
        yaxis_title='Eixo Y',
        showlegend=True,
        hovermode='x unified',
        template='plotly_white',
        updatemenus=[
            dict(
                buttons=[
                    dict(label='Wiggle', method='update', args=[{'stackgroup': 'one', 'y': [y - np.sum(ys, axis=0).mean() / len(ys) for y in ys]}]),
                    dict(label='Zero', method='update', args=[{'stackgroup': 'one', 'fill': 'tozeroy'}]),
                    dict(label='Simétrico', method='update', args=[{'stackgroup': 'one', 'fill': 'tonexty'}])
                ],
                direction='down',
                showactive=True,
                x=0.1,
                xanchor='left',
                y=1.15,
                yanchor='top',
                active=0 if baseline == 'wiggle' else 1 if baseline == 'zero' else 2
            ),
            dict(
                buttons=[
                    dict(label='Seno e Cosseno', method='restyle', args=[{'y': generate_data(num_points, 'sin_cos')[1], 'name': ['Seno', 'Cosseno']}]),
                    dict(label='Seno e Tangente', method='restyle', args=[{'y': generate_data(num_points, 'sin_tan')[1], 'name': ['Seno', 'Tangente']}]),
                    dict(label='Cosseno e Tangente', method='restyle', args=[{'y': generate_data(num_points, 'cos_tan')[1], 'name': ['Cosseno', 'Tangente']}])
                ],
                direction='down',
                showactive=True,
                x=0.3,
                xanchor='left',
                y=1.15,
                yanchor='top'
            )
        ],
        sliders=[
            dict(
                steps=[
                    dict(method='update', args=[{'x': [np.linspace(0, 10, n)], 'y': generate_data(n, func_type)[1]}], label=str(n)) 
                    for n in [50, 100, 200, 500]
                ],
                active=1,
                x=0.1,
                len=0.9,
                y=0,
                yanchor='top',
                currentvalue={'prefix': 'Pontos: '}
            )
        ]
    )
    
    return fig

# Display the plot
fig = create_streamgraph(baseline='wiggle', num_points=100)
fig.show()
