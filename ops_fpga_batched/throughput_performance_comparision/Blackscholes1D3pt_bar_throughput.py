import matplotlib.pyplot as plt
import numpy as np
from matplotlib.ticker import FormatStrFormatter
import pandas as pd
from barplot_params import general_font_size, power_marker_size, throughput_marker_size, label_font_size, \
    legends_font_size, bar_width, iner_props, outer_props, energy_bar_gap, energy_bar_width, colors, bar_offset, \
    fig_size, x_ticks_font_size, y_ticks_font_size, size_multiplier
from math import log2

# Load data
batched_df = pd.read_csv("data/Blackscholes1D3pt_throughput.csv")
batched_df_vck5000 = pd.read_csv("data/Blackscholes1D3pt_throughput_vck5000.csv")
df = pd.read_csv("../../ops_fpga/throughput_performance_comparision/data/Blackscholes1D3pt_throughput.csv")

# Extract data from CSV
xticks = df["grid_size"][:-1].astype(str)
hand_u280 = df["handcoded_u280"][:-1]
hand_vck5000 = df["handcoded_vck5000"][:-1]
cgen_wo_batching_u280 = df["codegen_u280_281MHz"][:-1]
cgen_wo_batching_vck5000 = df["codegen_vck5000"][:-1]
cgen_b1_u280_loopback = batched_df["codegen_2048SLR_10HLS_LOOP_1B"][:-1]
cgen_b1_u280_datcopy = batched_df["codegen_2048SLR_32HLS_DATCPY_1B"][:-1]
cgen_b10_u280_loopback = batched_df["codegen_2048SLR_10HLS_LOOP_10B"][:-1]
cgen_b10_u280_datcopy = batched_df["codegen_2048SLR_32HLS_DATCPY_10B"][:-1]
cgen_b20_u280_loopback = batched_df["codegen_2048SLR_10HLS_LOOP_20B"][:-1]
cgen_b20_u280_datcopy = batched_df["codegen_2048SLR_32HLS_DATCPY_20B"][:-1]
cgen_b50_u280_loopback = batched_df["codegen_2048SLR_10HLS_LOOP_50B"][:-1]
cgen_b50_u280_datcopy = batched_df["codegen_2048SLR_32HLS_DATCPY_50B"][:-1]
cgen_b100_u280_loopback = batched_df["codegen_2048SLR_10HLS_LOOP_100B"][:-1]
cgen_b100_u280_datcopy = batched_df["codegen_2048SLR_32HLS_DATCPY_100B"][:-1]
cgen_b200_u280_loopback = batched_df["codegen_2048SLR_10HLS_LOOP_200B"][:-1]
cgen_b200_u280_datcopy = batched_df["codegen_2048SLR_32HLS_DATCPY_200B"][:-1]

cgen_b1_vck5000_loopback = batched_df_vck5000["codegen_16384SLR_10HLS_LOOP_1B"][:-1]
cgen_b1_vck5000_datcopy = batched_df_vck5000["codegen_16384SLR_10HLS_DATCPY_1B"][:-1]
cgen_b10_vck5000_loopback = batched_df_vck5000["codegen_16384SLR_10HLS_LOOP_10B"][:-1]
cgen_b10_vck5000_datcopy = batched_df_vck5000["codegen_16384SLR_10HLS_DATCPY_10B"][:-1]
cgen_b20_vck5000_loopback = batched_df_vck5000["codegen_16384SLR_10HLS_LOOP_20B"][:-1]
cgen_b20_vck5000_datcopy = batched_df_vck5000["codegen_16384SLR_10HLS_DATCPY_20B"][:-1]
cgen_b50_vck5000_loopback = batched_df_vck5000["codegen_16384SLR_10HLS_LOOP_50B"][:-1]
cgen_b50_vck5000_datcopy = batched_df_vck5000["codegen_16384SLR_10HLS_DATCPY_50B"][:-1]
cgen_b100_vck5000_loopback = batched_df_vck5000["codegen_16384SLR_10HLS_LOOP_100B"][:-1]
cgen_b100_vck5000_datcopy = batched_df_vck5000["codegen_16384SLR_10HLS_DATCPY_100B"][:-1]
cgen_b200_vck5000_loopback = batched_df_vck5000["codegen_16384SLR_10HLS_LOOP_200B"][:-1]
cgen_b200_vck5000_datcopy = batched_df_vck5000["codegen_16384SLR_10HLS_DATCPY_200B"][:-1]
# u280_imp = (df['codegen_u280'] - df["handcoded_u280"]) / df["handcoded_u280"] * 100
# vck5000_imp = (df['codegen_vck5000'] - df["handcoded_vck5000"]) / df["handcoded_vck5000"] * 100
h100_1b = df["H100_1B"][:-1]
h100_50b = df["H100_50B"][:-1]

cgen_batching_u280_lb_envelop = np.nanmax([cgen_b1_u280_loopback, cgen_b10_u280_loopback, cgen_b20_u280_loopback, cgen_b50_u280_loopback, cgen_b100_u280_loopback, cgen_b200_u280_loopback], axis=0)

cgen_batching_u280_cp_envelop = np.nanmax([cgen_b1_u280_datcopy, cgen_b10_u280_datcopy, cgen_b20_u280_datcopy, cgen_b50_u280_datcopy, cgen_b100_u280_datcopy, cgen_b200_u280_datcopy], axis=0)

cgen_batching_vck5000_lb_envelop = np.nanmax([cgen_b1_vck5000_loopback, cgen_b10_vck5000_loopback, cgen_b20_vck5000_loopback, cgen_b50_vck5000_loopback, cgen_b100_vck5000_loopback, cgen_b200_vck5000_loopback], axis=0)

cgen_batching_vck5000_cp_envelop = np.nanmax([cgen_b1_vck5000_datcopy, cgen_b10_vck5000_datcopy, cgen_b20_vck5000_datcopy, cgen_b50_vck5000_datcopy, cgen_b100_vck5000_datcopy, cgen_b200_vck5000_datcopy], axis=0)

u280_lb_envelop_source = np.nanargmax([cgen_b1_u280_loopback, cgen_b10_u280_loopback, cgen_b20_u280_loopback, cgen_b50_u280_loopback, cgen_b100_u280_loopback, cgen_b200_u280_loopback], axis=0)
u280_cp_envelop_source = np.nanargmax([cgen_b1_u280_datcopy, cgen_b10_u280_datcopy, cgen_b20_u280_datcopy, cgen_b50_u280_datcopy, cgen_b100_u280_datcopy, cgen_b200_u280_datcopy], axis=0)
vck5000_lb_envelop_source = np.nanargmax([cgen_b1_vck5000_loopback, cgen_b10_vck5000_loopback, cgen_b20_vck5000_loopback, cgen_b50_vck5000_loopback, cgen_b100_vck5000_loopback, cgen_b200_vck5000_loopback], axis=0)
vck5000_cp_envelop_source = np.nanargmax([cgen_b1_vck5000_datcopy, cgen_b10_vck5000_datcopy, cgen_b20_vck5000_datcopy, cgen_b50_vck5000_datcopy, cgen_b100_vck5000_datcopy, cgen_b200_vck5000_datcopy], axis=0)

def geometric_mean(values):
    return np.exp(np.nanmean(np.log(values)))

geometric_means = {
    'U280 loopback envelope': geometric_mean(cgen_batching_u280_lb_envelop),
    'U280 datacopy envelope': geometric_mean(cgen_batching_u280_cp_envelop),
    'VCK5000 loopback envelope': geometric_mean(cgen_batching_vck5000_lb_envelop),
    'VCK5000 datacopy envelope': geometric_mean(cgen_batching_vck5000_cp_envelop),
    'U280 without batching': geometric_mean(cgen_wo_batching_u280),
    'VCK5000 without batching': geometric_mean(cgen_wo_batching_vck5000),
    'H100 50B': geometric_mean(h100_50b),
}

for name, value in geometric_means.items():
    print(f'{name} geometric mean: {value:.6f}')

# h100_power = df["pow_H100_1000B"]

# Configure plot settings
plt.rcParams["figure.figsize"] = fig_size
plt.rcParams.update({'font.size': general_font_size})
plt.rcParams['hatch.linewidth'] = 3  # Hatch line width
plt.rcParams['hatch.color'] = colors[1]

fig, ax = plt.subplots()
bar_offset = 0.0

x_indexes = np.arange(len(xticks))

batch_sizes = np.array(['1B', '10B', '20B', '50B', '100B', '200B'])
# print("U280 loopback envelope source batch size:", batch_sizes[u280_lb_envelop_source])
# print("U280 datacopy envelope source batch size:", batch_sizes[u280_cp_envelop_source])
# print("VCK5000 loopback envelope source batch size:", batch_sizes[vck5000_lb_envelop_source])
# print("VCK5000 datacopy envelope source batch size:", batch_sizes[vck5000_cp_envelop_source])


# U280
u280_lb_bars = ax.bar(x_indexes - bar_width + bar_offset, cgen_batching_u280_lb_envelop, width=bar_width, label='LB_ENV_U280', color=colors[4])
ax.bar(x_indexes - bar_width + bar_offset, cgen_batching_u280_lb_envelop, width=bar_width, color='none', edgecolor='black', **iner_props)

u280_cp_bars = ax.bar(x_indexes - bar_width + bar_offset, cgen_batching_u280_cp_envelop, width=bar_width, label='CP_200B_U280', color=colors[5])
ax.bar(x_indexes - bar_width + bar_offset, cgen_batching_u280_cp_envelop, width=bar_width, color='none', edgecolor='black', **iner_props)

plt.rcParams['hatch.color'] = colors[5]
bar3 = ax.bar(x_indexes - bar_width + bar_offset, cgen_wo_batching_u280, width=bar_width, label='LB_WOB_U280', color='white', hatch='xx')
bar3 = ax.bar(x_indexes - bar_width + bar_offset, cgen_wo_batching_u280, width=bar_width, color='none', edgecolor='black', **iner_props)

#VCK5000
vck5000_lb_bars = ax.bar(x_indexes + bar_offset, cgen_batching_vck5000_lb_envelop, width=bar_width, label='LB_ENV_VCK5', color=colors[0])
ax.bar(x_indexes + bar_offset, cgen_batching_vck5000_lb_envelop, width=bar_width, color='none', edgecolor='black', **iner_props)

vck5000_cp_bars = ax.bar(x_indexes + bar_offset, cgen_batching_vck5000_cp_envelop, width=bar_width, label='CP_200B_VCK5', color=colors[1])
ax.bar(x_indexes + bar_offset, cgen_batching_vck5000_cp_envelop, width=bar_width, color='none', edgecolor='black', **iner_props)

plt.rcParams['hatch.color'] = colors[1]
bar6 = ax.bar(x_indexes + bar_offset, cgen_wo_batching_vck5000, width=bar_width, label='LB_WOB_VCK5', color='white', hatch='xx')
bar6 = ax.bar(x_indexes + bar_offset, cgen_wo_batching_vck5000, width=bar_width, color='none', edgecolor='black', **iner_props)

#H100
bar6 = ax.bar(x_indexes + bar_width + bar_offset, h100_50b, width=bar_width, label='H100_50B', color=colors[9])
bar6 = ax.bar(x_indexes + bar_width + bar_offset, h100_50b, width=bar_width, color='none', edgecolor='black', **iner_props)

plt.rcParams['hatch.color'] = colors[9]
bar7 = ax.bar(x_indexes + bar_width + bar_offset, h100_1b, width=bar_width, label='H100_1B', color='white', hatch='//')
bar7 = ax.bar(x_indexes + bar_width + bar_offset, h100_1b, width=bar_width, color='none', edgecolor='black', **iner_props)

for bars, source in ((u280_lb_bars, u280_lb_envelop_source),
                     (vck5000_lb_bars, vck5000_lb_envelop_source)):
    ax.bar_label(bars, labels=batch_sizes[source], padding=2, fontsize=x_ticks_font_size - 1)


# Add secondary y-axis for power usage
# ax2 = ax.twinx()
# ax2.plot(xticks, cgen_4096_u280_power, linestyle='dashdot', marker='s', markersize=power_marker_size, label="U280_4096 energy", color='#6d65a3', markeredgecolor='#000000')#'#a59fd1')#'#f7b16a')
# ax2.plot(xticks, cgen_8192_u280_power, linestyle='dashdot', marker='s', markersize=power_marker_size, label="U280_8192 energy", color='#d9b3e6', markeredgecolor='#000000')#'#a59fd1')#'#f7b16a')
# ax2.plot(xticks, h100_power, linestyle='dashdot', marker='s', markersize=power_marker_size, label="H100 energy", color='#4dc46d', markeredgecolor='#000000')#'#92f0ab')#'#f5dc84')

# Format the axes
ax.yaxis.set_major_formatter(FormatStrFormatter('%.0f'))
# ax2.yaxis.set_major_formatter(FormatStrFormatter('%.0f'))

# Add grid, labels, and legends
ax.grid(which='both', axis='y', linewidth=1 * size_multiplier, alpha=0.5)
ax.set_xlabel('Mesh Size', fontsize=label_font_size)
ax.set_ylabel('Throughput (GFLOP/s)', fontsize=label_font_size)
# ax2.set_ylabel('Energy: 1k Batches (kJ)', fontsize=label_font_size)
ax.set_xticks(x_indexes)
ax.set_xticklabels(xticks, rotation=0)

# Combine legends from both axes
handles1, labels1 = ax.get_legend_handles_labels()
# handles2, labels2 = ax2.get_legend_handles_labels()
handles = handles1 #+ handles2
labels = labels1 #+ labels2
ax.legend(handles, labels, loc=2, ncol=4, facecolor='w', framealpha=1, edgecolor='black', prop={'size': legends_font_size})

# Set axis limits
ax.set_ylim([0, 900])
# ax2.set_ylim([0, 50])

# Save the figure
fig.tight_layout()
plt.savefig("output/black1d3pt_batched_throughput_barplot.pdf", bbox_inches='tight')
# plt.show()
