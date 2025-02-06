import plotly.graph_objects as go
import pandas as pd
import plotly.io as pio

# Disable MathJax globally
pio.kaleido.scope.mathjax = None

# Color Palette
colors = ['#003f5c', '#58508d', '#bc5090', '#ff6361', '#ffa600', '#34a853']

# Load data
df = pd.read_csv("data/Poisson2D5pt_throughput.csv")

# Extract data from CSV
xticks = df["grid_size"]
hand_u280 = df["handcoded_u280"]
cgen_u280 = df["codegen_u280"]
hand_vck5000 = df["handcoded_vck5000"]
cgen_vck5000 = df["codegen_vck5000"]
h100_1b = df["H100_1B"]
h100_100b = df["H100_100B"]
cgen_u280_power = df["pow_C_U280_1000B"]
h100_power = df["pow_H100_1000B"]

# Create the figure
fig = go.Figure()

# Add traces for throughput data
fig.add_trace(go.Scatter(x=xticks, y=cgen_u280, mode='lines+markers', name='c_u280', line=dict(color=colors[1], width=2), marker=dict(size=14)))
fig.add_trace(go.Scatter(x=xticks, y=hand_u280, mode='lines+markers', name='h_u280', line=dict(color=colors[0], width=2, dash='dash'), marker=dict(size=14, color='white', line=dict(color=colors[0], width=2))))
fig.add_trace(go.Scatter(x=xticks, y=cgen_vck5000, mode='lines+markers', name='c_vck5000', line=dict(color=colors[3], width=2), marker=dict(size=14, symbol='diamond')))
fig.add_trace(go.Scatter(x=xticks, y=hand_vck5000, mode='lines+markers', name='h_vck5000', line=dict(color=colors[2], width=2, dash='dash'), marker=dict(size=14, symbol='diamond', color='white', line=dict(color=colors[2], width=2))))
fig.add_trace(go.Scatter(x=xticks, y=h100_1b, mode='lines+markers', name='h100_1b', line=dict(color=colors[4], width=2, dash='dash'), marker=dict(size=16, symbol='triangle-up')))
fig.add_trace(go.Scatter(x=xticks, y=h100_100b, mode='lines+markers', name='h100_100b', line=dict(color=colors[5], width=2, dash='dash'), marker=dict(size=16, symbol='triangle-up')))

# Update layout for the figure
fig.update_layout(
    xaxis_title="Mesh Size",
    template="simple_white",
    yaxis_title="Throughput (GFLOP/s)",
    xaxis_title_font=dict(size=18),
    yaxis_title_font=dict(size=18),
    xaxis=dict(
        tickmode='array',
        tickvals=xticks,
        ticktext=xticks,
        tickfont=dict(size=16),
        domain=[0, 0.785]  # Shrink the x-axis to make space for the table
    ),
    yaxis=dict(
        tickformat='.0f',
        showgrid=True,
        gridwidth=1,
        gridcolor='rgba(128, 128, 128, 0.5)',
        range=[0,950],
        tickfont=dict(size=16)
    ),
    legend=dict(
        x=0.02,
        y=0.98,
        bgcolor='white',
        bordercolor='black',
        borderwidth=1,
        font=dict(size=14)
    ),
    margin=dict(l=50, r=50, t=50, b=50),  # Adjust margin to make room for the table
    width=900,  # Adjust width to accommodate the table
    height=500   # Adjust height as needed
)

# Add a table next to the plot
table_data = [
    [f"{xticks[i]}", f"{cgen_u280_power[i]:.2f}", f"{h100_power[i]:.2f}"] for i in range(len(xticks))
]
column_labels = ["", "U280", "H100"]
row_labels = [f"{xtick}" for xtick in xticks]

fig.add_trace(go.Table(
    columnwidth=[1.6, 1, 1],
    header=dict(
        values=column_labels,
        align='center',
        line=dict(width=1, color='black'),
        fill=dict(color='lightgray'),
        height = 32,
        font=dict(size=16)
    ),
    cells=dict(
        values=list(map(list, zip(*table_data))),
        align='center',
        line=dict(width=1, color='black'),
        height = 32,
        font=dict(size=16),
        fill = dict(color='white')
    ),
    domain=dict(x=[0.79, 1], y=[0, 0.8])  # Position the table to the right of the plot
))

fig.update_layout(
    annotations=[
        dict(
            text="Power-1000B (KJ)",  # Title text
            x=0.99,  # Center the title horizontally
            y=0.95,  # Position the title above the table
            xref="paper",  # Use relative coordinates
            yref="paper",
            showarrow=False,  # Hide the arrow
            font=dict(size=18, color="black")  # Customize font
        )
    ]
)

# Save the figure as a PDF
fig.write_image("output/poisson2d5pt_throughput_lineplot_with_table_plotly.pdf")