import matplotlib.pyplot as plt
import numpy as np
from matplotlib.ticker import FormatStrFormatter
import pandas as pd
from pandas.plotting import table


#Color Palette
colors = ['#003f5c', '#58508d', '#bc5090', '#ff6361', '#ffa600', '#34a853'] #['#4e79a7', '#f28e2b', '#e15759', '#76b7b2', '#59a14f', '#edc948'] 
# Load data
df = pd.read_csv("data/Poisson2D5pt_throughput.csv")

# Extract data from CSV
xticks = df["grid_size"]
hand_u280 = df["handcoded_u280"]
cgen_u280 = df["codegen_u280"]
hand_vck5000 = df["handcoded_vck5000"]
cgen_vck5000 = df["codegen_vck5000"]
cgen_u280_power = df["pow_C_U280_1000B"]
h100_power = df["pow_H100_1000B"]
# u280_imp = (df['codegen_u280'] - df["handcoded_u280"]) / df["handcoded_u280"] * 100
# vck5000_imp = (df['codegen_vck5000'] - df["handcoded_vck5000"]) / df["handcoded_vck5000"] * 100
h100_1b = df["H100_1B"]
h100_100b = df["H100_100B"]

# Configure plot settings
plt.rcParams["figure.figsize"] = (9, 5.5)
plt.rcParams.update({'font.size': 12})

fig, ax = plt.subplots()

# Add secondary y-axis for power usage
ax2 = ax.twinx()
ax2.plot(xticks, cgen_u280_power, linestyle='dashdot', marker='s', markersize=10, label="u280 power", color='#6d65a3', markeredgecolor='#000000')#'#a59fd1')#'#f7b16a')
ax2.plot(xticks, h100_power, linestyle='dashdot', marker='s', markersize=10, label="H100 power", color='#4dc46d', markeredgecolor='#000000')#'#92f0ab')#'#f5dc84')


# Plot throughput data
ax.plot(xticks, cgen_u280, linestyle='-', marker='o',markersize=12, label='c_u280', color=colors[1])
ax.plot(xticks, hand_u280, linestyle='--', marker='o', markersize=12, markerfacecolor='white', label='h_u280', color=colors[0])
ax.plot(xticks, cgen_vck5000, linestyle='-', marker='d',markersize=12, label='c_vck5000', color=colors[3])
ax.plot(xticks, hand_vck5000, linestyle='--', marker='d',markersize=12, markerfacecolor='white', label='h_vck5000', color=colors[2])
ax.plot(xticks, h100_1b, linestyle='-', marker='^',markersize=12, label='h100_1b', color=colors[4])
ax.plot(xticks, h100_100b, linestyle='-', marker='^',markersize=12, label='h100_100b', color=colors[5])


#anotate power numbers
# for ind, val in enumerate(cgen_u280.to_list()):
#     if not cgen_u280_power.isnull()[ind] and ind >= (cgen_u280.size - 4):
#         ax.text(xticks[ind], val + 30, "{:.1f} KJ".format(cgen_u280_power[ind]), ha='center', size=10) #, color=colors[1]) 

# for ind, val in enumerate(h100_100b.to_list()):
#     if not h100_power.isnull()[ind] and ind >= (h100_100b.size - 4):
#         ax.text(xticks[ind], val + 30, "{:.1f} KJ".format(h100_power[ind]), ha='center', size=10) #, color=colors[5]) 

# Format the axes
ax.yaxis.set_major_formatter(FormatStrFormatter('%.0f'))
ax2.yaxis.set_major_formatter(FormatStrFormatter('%.0f'))

# Add grid, labels, and legends
ax.grid(which='both', axis='y', linewidth=1, alpha=0.5)
ax.set_xlabel('Mesh Size')
ax.set_ylabel('Throughput (GFLOP/s)')
ax2.set_ylabel('Power Usage (KJ)')
ax.set_xticks(xticks)
ax.set_xticklabels(xticks, rotation=0)

# Combine legends from both axes
handles1, labels1 = ax.get_legend_handles_labels()
handles2, labels2 = ax2.get_legend_handles_labels()
handles = handles1 + handles2
labels = labels1 + labels2
ax.legend(handles, labels, loc=2, ncol=2, facecolor='w', framealpha=1, edgecolor='black', prop={'size': 12})

# Set axis limits
ax.set_ylim([0, 1000])
ax2.set_ylim([0, 45])

# Save the figure
fig.tight_layout()
plt.savefig("output/poisson2d5pt_throughput_lineplot.pdf", bbox_inches='tight')
# plt.show()
