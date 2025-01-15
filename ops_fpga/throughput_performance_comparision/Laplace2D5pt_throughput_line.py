import matplotlib.pyplot as plt
import numpy as np
from matplotlib.ticker import FormatStrFormatter
import pandas as pd

#Color Palette
colors = ['#003f5c', '#58508d', '#bc5090', '#ff6361', '#ffa600', '#34a853']
# Load data
df = pd.read_csv("data/Laplace2D5pt_throughput.csv")

# Extract data from CSV
xticks = df["grid_size"]
# hand_u280 = df["handcoded_u280"]
cgen_u280 = df["codegen_u280"]
# hand_vck5000 = df["handcoded_vck5000"]
cgen_vck5000 = df["codegen_vck5000"]
# u280_imp = (df['codegen_u280'] - df["handcoded_u280"]) / df["handcoded_u280"] * 100
# vck5000_imp = (df['codegen_vck5000'] - df["handcoded_vck5000"]) / df["handcoded_vck5000"] * 100
h100_1b = df["H100_1B"]
h100_100b = df["H100_100B"]

# Configure plot settings
plt.rcParams["figure.figsize"] = (9, 5.5)
plt.rcParams.update({'font.size': 14})

fig, ax = plt.subplots()

# Plot throughput data
# ax.plot(xticks, hand_u280, linestyle='--', marker='o', label='h_u280', color=colors[0])
ax.plot(xticks, cgen_u280, linestyle='-', marker='o', label='c_u280', color=colors[1])
# ax.plot(xticks, hand_vck5000, linestyle='--', marker='s', label='h_vck5000', color=colors[2])
ax.plot(xticks, cgen_vck5000, linestyle='-', marker='s', label='c_vck5000', color=colors[3])
ax.plot(xticks, h100_1b, linestyle='--', marker='^', label='h100_1b', color=colors[4])
ax.plot(xticks, h100_100b, linestyle='--', marker='^', label='h100_100b', color=colors[5])

# Add secondary y-axis for improvement percentages
# ax2 = ax.twinx()
# ax2.plot(xticks, u280_imp, linestyle='-', marker='s', label="u280 Imp%", color='#4768a6')
# ax2.plot(xticks, vck5000_imp, linestyle='-', marker='s', label="vck5000 Imp%", color='#70915a')

# Format the axes
ax.yaxis.set_major_formatter(FormatStrFormatter('%.0f'))
# ax2.yaxis.set_major_formatter(FormatStrFormatter('%.0f'))

# Add grid, labels, and legends
ax.grid(which='both', axis='y', linewidth=1, alpha=0.5)
ax.set_xlabel('Mesh Size')
ax.set_ylabel('Throughput (GFLOP/s)')
# ax2.set_ylabel('% Improvement')
ax.set_xticks(xticks)
ax.set_xticklabels(xticks, rotation=45)

# Combine legends from both axes
handles1, labels1 = ax.get_legend_handles_labels()
# handles2, labels2 = ax2.get_legend_handles_labels()
handles = handles1 #+ handles2
labels = labels1 #+ labels2
ax.legend(handles, labels, loc=2, ncol=2, facecolor='w', framealpha=1, edgecolor='black', prop={'size': 12})

# Set axis limits
ax.set_ylim([0, 1250])
# ax2.set_ylim([-5, 100])

# Save the figure
fig.tight_layout()
plt.savefig("output/laplace2d9pt_throughput_lineplot.pdf", bbox_inches='tight')
# plt.show()
