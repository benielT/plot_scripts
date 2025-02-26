import matplotlib.pyplot as plt
import numpy as np
from matplotlib.ticker import FormatStrFormatter
import pandas as pd
from lineplot_params import general_font_size, power_marker_size, throughput_marker_size, label_font_size, legends_font_size


#Color Palette
colors = ['#003f5c', '#58508d', '#bc5090', '#ff6361', '#ffa600', '#34a853', '#ce87e6']
# Load data
df = pd.read_csv("data/data.csv")

# Extract data from CSV
xticks = df["grid_size"]
hand_u55c = df["mpt_handcoded_u55c"]
cgen_u55c = df["mpt_codegen_u55c"]
hand_vck5000 = df["mpt_handcoded_vck5000"]
cgen_vck5000 = df["mpt_codegen_vck5000"]
# u280_imp = (df['codegen_u280'] - df["handcoded_u280"]) / df["handcoded_u280"] * 100
# vck5000_imp = (df['codegen_vck5000'] - df["handcoded_vck5000"]) / df["handcoded_vck5000"] * 100
h100_1b = df["mpt_H100_1B"]
# h100_10b = df["H100_10B"]

cgen_u55c_power = df["pow_C_u55c_100B"]
h100_power = df["pow_H100_100B"]

# Configure plot settings
plt.rcParams["figure.figsize"] = (9, 5.5)
plt.rcParams.update({'font.size': general_font_size})

fig, ax = plt.subplots()

# Plot throughput data
ax.plot(xticks, hand_u55c, linestyle='--', marker='o', markersize=throughput_marker_size, markerfacecolor='white', label='c_U55c', color=colors[0])
ax.plot(xticks, cgen_u55c, linestyle='-', marker='o', markersize=throughput_marker_size, label='c_U55c', color=colors[1])
ax.plot(xticks, cgen_vck5000, linestyle='-', marker='d',markersize=throughput_marker_size, label='c_VCK', color=colors[3])
ax.plot(xticks, hand_vck5000, linestyle='--', marker='d',markersize=throughput_marker_size, markerfacecolor='white', label='h_VCK', color=colors[2])
ax.plot(xticks, h100_1b, linestyle='-', marker='^',markersize=throughput_marker_size, label='H100', color=colors[5])
# ax.plot(xticks, h100_100b, linestyle='-', marker='^',markersize=throughput_marker_size, label='H100_100B', color=colors[5])

# Add secondary y-axis for power usage
ax2 = ax.twinx()
ax2.plot(xticks, cgen_u55c_power, linestyle='dashdot', marker='s', markersize=power_marker_size, label="U55c energy", color='#6d65a3', markeredgecolor='#000000')#'#a59fd1')#'#f7b16a')
# ax2.plot(xticks, h100_power, linestyle='dashdot', marker='s', markersize=power_marker_size, label="H100 power", color='#d9b3e6', markeredgecolor='#000000')#'#a59fd1')#'#f7b16a')
ax2.plot(xticks, h100_power, linestyle='dashdot', marker='s', markersize=power_marker_size, label="H100 energy", color='#4dc46d', markeredgecolor='#000000')#'#92f0ab')#'#f5dc84')

# Format the axes
ax.yaxis.set_major_formatter(FormatStrFormatter('%.0f'))
ax2.yaxis.set_major_formatter(FormatStrFormatter('%.0f'))

# Add grid, labels, and legends
ax.grid(which='both', axis='y', linewidth=1, alpha=0.5)
ax.set_xlabel('Mesh Size', fontsize=label_font_size)
ax.set_ylabel('Throughput (MPts/s)', fontsize=label_font_size)
ax2.set_ylabel('Energy: 100 Batches (kJ)', fontsize=label_font_size)
ax.set_xticks(xticks)
ax.set_xticklabels(xticks, rotation=0)

# Combine legends from both axes
handles1, labels1 = ax.get_legend_handles_labels()
handles2, labels2 = ax2.get_legend_handles_labels()
handles = handles1 + handles2
labels = labels1 + labels2
ax.legend(handles, labels, loc=2, ncol=2, facecolor='w', framealpha=1, edgecolor='black', prop={'size': 13})

# Set axis limits
ax.set_ylim([0, 1500])
ax2.set_ylim([0, 600])

# Save the figure
fig.tight_layout()
plt.savefig("output/RTM_line.pdf", bbox_inches='tight')
# plt.show()
