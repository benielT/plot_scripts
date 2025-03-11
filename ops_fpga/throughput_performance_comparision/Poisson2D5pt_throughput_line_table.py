import matplotlib.pyplot as plt
import numpy as np
from matplotlib.ticker import FormatStrFormatter
import pandas as pd

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

# Configure plot settings
plt.rcParams["figure.figsize"] = (10, 5.5)
plt.rcParams.update({'font.size': 10})

fig, ax = plt.subplots()

# Plot throughput data
ax.plot(xticks, cgen_u280, linestyle='-', marker='o', markersize=12, label='c_u280', color=colors[1])
ax.plot(xticks, hand_u280, linestyle='--', marker='o', markersize=12, markerfacecolor='white', label='h_u280', color=colors[0])
ax.plot(xticks, cgen_vck5000, linestyle='-', marker='d', markersize=12, label='c_vck5000', color=colors[3])
ax.plot(xticks, hand_vck5000, linestyle='--', marker='d', markersize=12, markerfacecolor='white', label='h_vck5000', color=colors[2])
ax.plot(xticks, h100_1b, linestyle='--', marker='^', markersize=12, label='h100_1b', color=colors[4])
ax.plot(xticks, h100_100b, linestyle='--', marker='^', markersize=12, label='h100_100b', color=colors[5])

# Format the axes
ax.yaxis.set_major_formatter(FormatStrFormatter('%.0f'))
ax.grid(which='both', axis='y', linewidth=1, alpha=0.5)
ax.set_xlabel('Mesh Size')
ax.set_ylabel('Throughput (GFLOP/s)')
ax.set_xticks(xticks)
ax.set_xticklabels(xticks, rotation=0)

# Combine legends
handles1, labels1 = ax.get_legend_handles_labels()
ax.legend(handles1, labels1, loc=2, ncol=2, facecolor='w', framealpha=1, edgecolor='black', prop={'size': 12})

# Set axis limits
ax.set_ylim([0, 1000])

# Add a table below the plot
cell_text = [
    [f"{cgen_u280_power[i]:.2f}", f"{h100_power[i]:.2f}"] for i in range(len(xticks))
]
column_labels = ["U280", "H100"]

# Place the table next to the plot
table = plt.table(
    cellText=cell_text,
    rowLabels=[f"{xtick}" for xtick in xticks],
    colLabels=column_labels,
    cellLoc='center',
    loc='right',
    bbox=[1.1, 0.1, 0.2, 0.7]  # [x, y, width, height]
)


# Save the figure
fig.tight_layout(rect=[0, 0, 1.2, 1])  # Make room for the table
plt.savefig("output/poisson2d5pt_throughput_lineplot_with_table.pdf", bbox_inches='tight')
# plt.show()