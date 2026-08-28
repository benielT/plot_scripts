import matplotlib.pyplot as plt
import numpy as np
from matplotlib.ticker import FormatStrFormatter
import pandas as pd
from lineplot_params import general_font_size, power_marker_size, throughput_marker_size, label_font_size, legends_font_size, \
    colors

# Load data
batched_df = pd.read_csv("data/jac2d9t_throughput.csv")

# Extract data from CSV
xticks = batched_df["grid_size"]
cgen_b1_tapa_datcopy = batched_df["tapa_b1"]
cgen_b10_tapa_datcopy = batched_df["tapa_b10"]
cgen_b20_tapa_datcopy = batched_df["tapa_b20"]
cgen_b50_tapa_datcopy = batched_df["tapa_b50"]
cgen_b1_hls_datcopy = batched_df["hls_b1"]
cgen_b10_hls_datcopy = batched_df["hls_b10"]
cgen_b20_hls_datcopy = batched_df["hls_b20"]
cgen_b50_hls_datcopy = batched_df["hls_b50"]

# h100_power = df["pow_H100_1000B"]

# Configure plot settings
plt.rcParams["figure.figsize"] = (9, 5)
plt.rcParams.update({'font.size': general_font_size})

fig, ax = plt.subplots()

# Plot throughput data
# ax.plot(xticks, cgen_b1_u280_loopback, linestyle='-', marker='o', markersize=throughput_marker_size, label='c_1B_LB', color=colors[2])
# ax.plot(xticks, cgen_b10_u280_loopback, linestyle='-', marker='o', markersize=throughput_marker_size, label='c_10B_LB', color=colors[3])
# ax.plot(xticks, cgen_b20_u280_loopback, linestyle='-', marker='o', markersize=throughput_marker_size, label='c_20B_LB', color=colors[4])
# ax.plot(xticks, cgen_b50_u280_loopback, linestyle='-', marker='o', markersize=throughput_marker_size, label='c_50B_LB', color=colors[5])
ax.plot(xticks, cgen_b1_hls_datcopy, linestyle='--', marker='d', markersize=throughput_marker_size, label='HLS_1B', color=colors[6])
ax.plot(xticks, cgen_b10_hls_datcopy, linestyle='--', marker='d', markersize=throughput_marker_size, label='HLS_10B', color=colors[7])
ax.plot(xticks, cgen_b20_hls_datcopy, linestyle='--', marker='d', markersize=throughput_marker_size, label='HLS_20B', color=colors[8])
ax.plot(xticks, cgen_b50_hls_datcopy, linestyle='--', marker='d', markersize=throughput_marker_size, label='HLS_50B', color=colors[9])
ax.plot(xticks, cgen_b1_tapa_datcopy, linestyle='--', marker='o', markersize=throughput_marker_size, label='TAPA_1B', color=colors[10])
ax.plot(xticks, cgen_b10_tapa_datcopy, linestyle='--', marker='o', markersize=throughput_marker_size, label='TAPA_10B', color=colors[1])
ax.plot(xticks, cgen_b20_tapa_datcopy, linestyle='--', marker='o', markersize=throughput_marker_size, label='TAPA_20B', color=colors[2])
ax.plot(xticks, cgen_b50_tapa_datcopy, linestyle='--', marker='o', markersize=throughput_marker_size, label='TAPA_50B', color=colors[3])



# Add secondary y-axis for power usage
# ax2 = ax.twinx()
# ax2.plot(xticks, cgen_4096_u280_power, linestyle='dashdot', marker='s', markersize=power_marker_size, label="U280_4096 energy", color='#6d65a3', markeredgecolor='#000000')#'#a59fd1')#'#f7b16a')
# ax2.plot(xticks, cgen_8192_u280_power, linestyle='dashdot', marker='s', markersize=power_marker_size, label="U280_8192 energy", color='#d9b3e6', markeredgecolor='#000000')#'#a59fd1')#'#f7b16a')
# ax2.plot(xticks, h100_power, linestyle='dashdot', marker='s', markersize=power_marker_size, label="H100 energy", color='#4dc46d', markeredgecolor='#000000')#'#92f0ab')#'#f5dc84')

# Format the axes
ax.yaxis.set_major_formatter(FormatStrFormatter('%.0f'))
# ax2.yaxis.set_major_formatter(FormatStrFormatter('%.0f'))

# Add grid, labels, and legends
ax.grid(which='both', axis='y', linewidth=1, alpha=0.5)
ax.set_xlabel('Mesh Size', fontsize=label_font_size)
ax.set_ylabel('Throughput (GFLOP/s)', fontsize=label_font_size)
# ax2.set_ylabel('Energy: 1k Batches (kJ)', fontsize=label_font_size)
ax.set_xticks(xticks)
ax.set_xticklabels(xticks, rotation=0)

# Combine legends from both axes
handles1, labels1 = ax.get_legend_handles_labels()
# handles2, labels2 = ax2.get_legend_handles_labels()
handles = handles1 #+ handles2
labels = labels1 #+ labels2
ax.legend(handles, labels, loc=2, ncol=4, facecolor='w', framealpha=1, edgecolor='black', prop={'size': 13})

# Set axis limits
ax.set_ylim([0, 700])
# ax2.set_ylim([0, 50])

# Save the figure
fig.tight_layout()
plt.savefig("output/jac2d5pt_tapa_batched_throughput_lineplot.pdf", bbox_inches='tight')
# plt.show()
