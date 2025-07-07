import matplotlib.pyplot as plt
import numpy as np
from matplotlib.ticker import FormatStrFormatter
import pandas as pd
from lineplot_params import general_font_size, power_marker_size, throughput_marker_size, label_font_size, legends_font_size, \
    colors

# Load data
batched_df = pd.read_csv("data/Jac2D9pt_throughput.csv")
df = pd.read_csv("../../ops_fpga/throughput_performance_comparision/data/Jac2D9pt_throughput.csv")

# Extract data from CSV
xticks = batched_df["grid_size"]
hand_u280 = df["handcoded_u280"]
cgen_wo_batching_u280 = df["codegen_L_4096_H_360_u280"]
cgen_b1_u280_loopback = batched_df["codegen_4096SLR_360HLS_LOOP_1B"]
cgen_b1_u280_datcopy = batched_df["codegen_128SLR_10HLS_DATCPY_1B"]
cgen_b10_u280_loopback = batched_df["codegen_4096SLR_360HLS_LOOP_10B"]
cgen_b10_u280_datcopy = batched_df["codegen_128SLR_10HLS_DATCPY_10B"]
cgen_b20_u280_loopback = batched_df["codegen_4096SLR_360HLS_LOOP_20B"]
cgen_b20_u280_datcopy = batched_df["codegen_128SLR_10HLS_DATCPY_20B"]
cgen_b50_u280_loopback = batched_df["codegen_4096SLR_360HLS_LOOP_50B"]
cgen_b50_u280_datcopy = batched_df["codegen_128SLR_10HLS_DATCPY_50B"]
cgen_b100_u280_datcopy = batched_df["codegen_128SLR_10HLS_DATCPY_100B"]
# u280_imp = (df['codegen_u280'] - df["handcoded_u280"]) / df["handcoded_u280"] * 100
# vck5000_imp = (df['codegen_vck5000'] - df["handcoded_vck5000"]) / df["handcoded_vck5000"] * 100
h100_1b = df["H100_1B"]
h100_100b = df["H100_100B"]

# h100_power = df["pow_H100_1000B"]

# Configure plot settings
plt.rcParams["figure.figsize"] = (12, 7.5)
plt.rcParams.update({'font.size': general_font_size})

fig, ax = plt.subplots()

# Plot throughput data
ax.plot(xticks, cgen_b1_u280_loopback, linestyle='-', marker='o', markersize=throughput_marker_size, label='c_1B_LB', color=colors[2])
ax.plot(xticks, cgen_b10_u280_loopback, linestyle='-', marker='o', markersize=throughput_marker_size, label='c_10B_LB', color=colors[3])
ax.plot(xticks, cgen_b20_u280_loopback, linestyle='-', marker='o', markersize=throughput_marker_size, label='c_20B_LB', color=colors[4])
ax.plot(xticks, cgen_b50_u280_loopback, linestyle='-', marker='o', markersize=throughput_marker_size, label='c_50B_LB', color=colors[5])
ax.plot(xticks, cgen_b1_u280_datcopy, linestyle='-', marker='d', markersize=throughput_marker_size, label='c_1B_CP', color=colors[6])
ax.plot(xticks, cgen_b10_u280_datcopy, linestyle='-', marker='d', markersize=throughput_marker_size, label='c_10B_CP', color=colors[7])
ax.plot(xticks, cgen_b20_u280_datcopy, linestyle='-', marker='d', markersize=throughput_marker_size, label='c_20B_CP', color=colors[8])
ax.plot(xticks, cgen_b50_u280_datcopy, linestyle='-', marker='d', markersize=throughput_marker_size, label='c_50B_CP', color=colors[9])
ax.plot(xticks, cgen_b100_u280_datcopy, linestyle='-', marker='d', markersize=throughput_marker_size, label='c_100B_CP', color=colors[10])
ax.plot(xticks[2:], hand_u280, linestyle='--', marker='o', markersize=throughput_marker_size, markerfacecolor='white', label='h_U280', color=colors[0])
ax.plot(xticks[2:], cgen_wo_batching_u280, linestyle='-', marker='o', markersize=throughput_marker_size, label='c_WOB_LB', color=colors[1])
ax.plot(xticks[2:], h100_1b, linestyle='-', marker='^',markersize=throughput_marker_size, label='H100_1B', color=colors[11])
ax.plot(xticks[2:], h100_100b, linestyle='-', marker='^',markersize=throughput_marker_size, label='H100_100B', color=colors[12])

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
ax.set_ylim([0, 1700])
# ax2.set_ylim([0, 50])

# Save the figure
fig.tight_layout()
plt.savefig("output/jac2d9p_batched_throughput_lineplot.pdf", bbox_inches='tight')
# plt.show()
