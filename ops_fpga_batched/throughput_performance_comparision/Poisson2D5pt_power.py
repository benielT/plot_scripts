import matplotlib.pyplot as plt
import numpy as np
from matplotlib.ticker import FormatStrFormatter
import pandas as pd
from barplot_params import general_font_size, power_marker_size, throughput_marker_size, label_font_size, \
    legends_font_size, bar_width, iner_props, outer_props, energy_bar_gap, energy_bar_width, colors, bar_offset, \
    fig_size, x_ticks_font_size, y_ticks_font_size, size_multiplier
from math import log2

# Load data
batched_df = pd.read_csv("data/Poisson2D5pt_throughput_u280.csv")
batched_df_vck5000 = pd.read_csv("data/Poisson2D5pt_throughput_vck5000.csv")
df = pd.read_csv("../../ops_fpga/throughput_performance_comparision/data/Poisson2D5pt_throughput.csv")

# Extract data from CSV
xticks = batched_df["grid_size"][:-3].astype(str)
# hand_u280 = df["handcoded_u280"][:-3]
# hand_vck5000 = df["handcoded_vck5000"][:-3]
cgen_b1_u280_loopback = batched_df["cgen_LOOP_1B"][:-3]
cgen_b1_u280_datcopy = batched_df["cgen_DATCPY_1B"][:-3]
cgen_b10_u280_loopback = batched_df["cgen_LOOP_10B"][:-3]
cgen_b10_u280_datcopy = batched_df["cgen_DATCPY_10B"][:-3]
cgen_b20_u280_loopback = batched_df["cgen_LOOP_20B"][:-3]
cgen_b20_u280_datcopy = batched_df["cgen_DATCPY_20B"][:-3]
cgen_b50_u280_loopback = batched_df["cgen_LOOP_50B"][:-3]
cgen_b50_u280_datcopy = batched_df["cgen_DATCPY_50B"][:-3]
cgen_b100_u280_datcopy = batched_df["cgen_DATCPY_100B"][:-3]

cgen_b1_vck5000_loopback = batched_df_vck5000["cgen_LOOP_1B"][:-3]
cgen_b1_vck5000_datcopy = batched_df_vck5000["cgen_DATCPY_1B"][:-3]
cgen_b10_vck5000_loopback = batched_df_vck5000["cgen_LOOP_10B"][:-3]
cgen_b10_vck5000_datcopy = batched_df_vck5000["cgen_DATCPY_10B"][:-3]
cgen_b20_vck5000_loopback = batched_df_vck5000["cgen_LOOP_20B"][:-3]
cgen_b20_vck5000_datcopy = batched_df_vck5000["cgen_DATCPY_20B"][:-3]
cgen_b50_vck5000_loopback = batched_df_vck5000["cgen_LOOP_50B"][:-3]
cgen_b50_vck5000_datcopy = batched_df_vck5000["cgen_DATCPY_50B"][:-3]
cgen_b100_vck5000_datcopy = batched_df_vck5000["cgen_DATCPY_100B"][:-3]
# u280_imp = (df['codegen_u280'] - df["handcoded_u280"]) / df["handcoded_u280"] * 100
# vck5000_imp = (df['codegen_vck5000'] - df["handcoded_vck5000"]) / df["handcoded_vck5000"] * 100
# h100_1b = df["H100_1B"][:-3]
# h100_50b = df["H100_50B"][:-3]

cgen_batching_u280_lb_envelop = np.nanmax([cgen_b1_u280_loopback, cgen_b10_u280_loopback, cgen_b20_u280_loopback, cgen_b50_u280_loopback], axis=0)

# cgen_batching_u280_cp_envelop = np.nanmax([cgen_b1_u280_datcopy, cgen_b10_u280_datcopy, cgen_b20_u280_datcopy, cgen_b50_u280_datcopy, cgen_b100_u280_datcopy, cgen_b200_u280_datcopy], axis=0)

cgen_batching_vck5000_lb_envelop = np.nanmax([cgen_b1_vck5000_loopback, cgen_b10_vck5000_loopback, cgen_b20_vck5000_loopback, cgen_b50_vck5000_loopback], axis=0)

# cgen_batching_vck5000_cp_envelop = np.nanmax([cgen_b1_vck5000_datcopy, cgen_b10_vck5000_datcopy, cgen_b20_vck5000_datcopy, cgen_b50_vck5000_datcopy, cgen_b100_vck5000_datcopy, cgen_b200_vck5000_datcopy], axis=0)

u280_lb_envelop_source = np.nanargmax([cgen_b1_u280_loopback, cgen_b10_u280_loopback, cgen_b20_u280_loopback, cgen_b50_u280_loopback], axis=0)
u280_cp_envelop_source = np.nanargmax([cgen_b1_u280_datcopy, cgen_b10_u280_datcopy, cgen_b20_u280_datcopy, cgen_b50_u280_datcopy, cgen_b100_u280_datcopy], axis=0)
vck5000_lb_envelop_source = np.nanargmax([cgen_b1_vck5000_loopback, cgen_b10_vck5000_loopback, cgen_b20_vck5000_loopback, cgen_b50_vck5000_loopback], axis=0)
vck5000_cp_envelop_source = np.nanargmax([cgen_b1_vck5000_datcopy, cgen_b10_vck5000_datcopy, cgen_b20_vck5000_datcopy, cgen_b50_vck5000_datcopy, cgen_b100_vck5000_datcopy], axis=0)

cgen_b1_u280_loopback_pow = batched_df["cgen_LOOP_1B_1000B_pow"][:-3]
cgen_b1_u280_datcopy_pow = batched_df["cgen_DATCPY_1B_1000B_pow"][:-3]
cgen_b10_u280_loopback_pow = batched_df["cgen_LOOP_10B_1000B_pow"][:-3]
cgen_b10_u280_datcopy_pow = batched_df["cgen_DATCPY_10B_1000B_pow"][:-3]
cgen_b20_u280_loopback_pow = batched_df["cgen_LOOP_20B_1000B_pow"][:-3]
cgen_b20_u280_datcopy_pow = batched_df["cgen_DATCPY_20B_1000B_pow"][:-3]
cgen_b50_u280_loopback_pow = batched_df["cgen_LOOP_50B_1000B_pow"][:-3]
cgen_b50_u280_datcopy_pow = batched_df["cgen_DATCPY_50B_1000B_pow"][:-3]
cgen_b100_u280_datcopy_pow = batched_df["cgen_DATCPY_100B_1000B_pow"][:-3]

all_u280_batching_loop_pow = np.array([cgen_b1_u280_loopback_pow, cgen_b10_u280_loopback_pow, cgen_b20_u280_loopback_pow, cgen_b50_u280_loopback_pow])

cgen_b1_vck5000_loopback_pow = batched_df_vck5000["cgen_LOOP_1B_1000B_pow"][:-3]
cgen_b1_vck5000_datcopy_pow = batched_df_vck5000["cgen_DATCPY_1B_1000B_pow"][:-3]
cgen_b10_vck5000_loopback_pow = batched_df_vck5000["cgen_LOOP_10B_1000B_pow"][:-3]
cgen_b10_vck5000_datcopy_pow = batched_df_vck5000["cgen_DATCPY_10B_1000B_pow"][:-3]
cgen_b20_vck5000_loopback_pow = batched_df_vck5000["cgen_LOOP_20B_1000B_pow"][:-3]
cgen_b20_vck5000_datcopy_pow = batched_df_vck5000["cgen_DATCPY_20B_1000B_pow"][:-3]
cgen_b50_vck5000_loopback_pow = batched_df_vck5000["cgen_LOOP_50B_1000B_pow"][:-3]
cgen_b50_vck5000_datcopy_pow = batched_df_vck5000["cgen_DATCPY_50B_1000B_pow"][:-3]
cgen_b100_vck5000_datcopy_pow = batched_df_vck5000["cgen_DATCPY_100B_1000B_pow"][:-3]
all_vkc5000_batching_loop_pow = np.array([cgen_b1_vck5000_loopback_pow, cgen_b10_vck5000_loopback_pow, cgen_b20_vck5000_loopback_pow, cgen_b50_vck5000_loopback_pow])

cgen_batching_u280_lb_envelop_pow = all_u280_batching_loop_pow[
    u280_lb_envelop_source, np.arange(len(xticks))
]
cgen_batching_vck5000_lb_envelop_pow = all_vkc5000_batching_loop_pow[
    vck5000_lb_envelop_source, np.arange(len(xticks))
]

u280_lb_throughput = np.array([
    cgen_b1_u280_loopback, cgen_b10_u280_loopback,
    cgen_b20_u280_loopback, cgen_b50_u280_loopback
])
u280_lb_power_valid = np.isfinite(all_u280_batching_loop_pow)
u280_lb_power_source = np.argmax(
    np.where(u280_lb_power_valid, u280_lb_throughput, -np.inf), axis=0
)
cgen_batching_u280_lb_envelop_pow = all_u280_batching_loop_pow[
    u280_lb_power_source, np.arange(len(xticks))
]

def geometric_mean(values):
    return np.exp(np.nanmean(np.log(values)))

geometric_means = {
    'U280 without batching energy': geometric_mean(cgen_b1_u280_loopback_pow),
    'U280 loopback envelope energy': geometric_mean(cgen_batching_u280_lb_envelop_pow),
    'U280 datacopy 100B energy': geometric_mean(cgen_b100_u280_datcopy_pow),
    'VCK5000 without batching energy': geometric_mean(cgen_b1_vck5000_loopback_pow),
    'VCK5000 loopback envelope energy': geometric_mean(cgen_batching_vck5000_lb_envelop_pow),
    'VCK5000 datacopy 100B energy': geometric_mean(cgen_b100_vck5000_datcopy_pow),
}

for name, value in geometric_means.items():
    print(f'{name} geometric mean: {value:.6f}')

# h100_power = df["pow_H100_1000B"]
print(cgen_batching_u280_lb_envelop_pow)

# Configure plot settings
plt.rcParams["figure.figsize"] = fig_size
plt.rcParams.update({'font.size': general_font_size})
plt.rcParams['hatch.linewidth'] = 4  # Hatch line width
plt.rcParams['hatch.color'] = colors[1]

fig, ax = plt.subplots()
bar_offset = 0.0

x_indexes = np.arange(len(xticks))

batch_sizes = np.array(['1B', '10B', '20B', '50B', '100B', '200B'])
# print("U280 loopback envelope source batch size:", batch_sizes[u280_lb_envelop_source])
# print("U280 datacopy envelope source batch size:", batch_sizes[u280_cp_envelop_source])
# print("VCK5000 loopback envelope source batch size:", batch_sizes[vck5000_lb_envelop_source])
# print("VCK5000 datacopy envelope source batch size:", batch_sizes[vck5000_cp_envelop_source])
ax.plot(x_indexes, cgen_b1_u280_loopback_pow, linestyle='--', marker='o', markersize=(power_marker_size), label="U280 WOB", color=colors[0], markerfacecolor='white', markeredgewidth=2 * size_multiplier, markeredgecolor=colors[0])
ax.plot(x_indexes, cgen_batching_u280_lb_envelop_pow, linestyle='dashdot', marker='^', markersize=(power_marker_size), label="LB U280 ENV", color=colors[7], markerfacecolor='white', markeredgewidth=2 * size_multiplier, markeredgecolor=colors[7])
ax.plot(x_indexes, cgen_b100_u280_datcopy_pow, linestyle='-', marker='d', markersize=(power_marker_size), label="CP U280 100B", color=colors[8], markerfacecolor='white', markeredgewidth=2 * size_multiplier, markeredgecolor=colors[8])

ax.plot(x_indexes, cgen_b1_vck5000_loopback_pow, linestyle='--', marker='o', markersize=(power_marker_size), label="VCK5 WOB", color=colors[10], markerfacecolor='white', markeredgewidth=2 * size_multiplier, markeredgecolor=colors[10])

ax.plot(x_indexes, cgen_batching_vck5000_lb_envelop_pow, linestyle='dashdot', marker='^', markersize=(power_marker_size), label="LB VCK5 ENV", color=colors[3], markerfacecolor='white', markeredgewidth=2 * size_multiplier, markeredgecolor=colors[3])
ax.plot(x_indexes, cgen_b100_vck5000_datcopy_pow, linestyle='-', marker='o', markersize=(power_marker_size), label="CP VCK5 100B", color=colors[11], markerfacecolor='white', markeredgewidth=2 * size_multiplier, markeredgecolor=colors[11])



# for x_index, power, batch_index in zip(
#         x_indexes, cgen_batching_u280_lb_envelop_pow, u280_lb_envelop_source):
#     ax.annotate(batch_sizes[batch_index], (x_index, power), xytext=(0, 5),
#                 textcoords='offset points', ha='center', va='bottom',
#                 fontsize=x_ticks_font_size - 1)

# for x_index, power, batch_index in zip(
#         x_indexes, cgen_batching_vck5000_lb_envelop_pow, vck5000_lb_envelop_source):
#     ax.annotate(batch_sizes[batch_index], (x_index, power), xytext=(0, -8),
#                 textcoords='offset points', ha='center', va='top',
#                 fontsize=x_ticks_font_size - 1)


# Add secondary y-axis for power usage
# ax2 = ax.twinx()
# ax2.plot(xticks, cgen_4096_u280_power, linestyle='dashdot', marker='s', markersize=power_marker_size, label="U280_4096 energy", color='#6d65a3', markeredgecolor='#000000')#'#a59fd1')#'#f7b16a')
# ax2.plot(xticks, cgen_8192_u280_power, linestyle='dashdot', marker='s', markersize=power_marker_size, label="U280_8192 energy", color='#d9b3e6', markeredgecolor='#000000')#'#a59fd1')#'#f7b16a')
# ax2.plot(xticks, h100_power, linestyle='dashdot', marker='s', markersize=power_marker_size, label="H100 energy", color='#4dc46d', markeredgecolor='#000000')#'#92f0ab')#'#f5dc84')

# Format the axes
ax.yaxis.set_major_formatter(FormatStrFormatter('%.1f'))
# ax2.yaxis.set_major_formatter(FormatStrFormatter('%.0f'))

# Add grid, labels, and legends
ax.grid(which='both', axis='y', linewidth=1 * size_multiplier, alpha=0.5)
ax.set_xlabel('Mesh Size', fontsize=label_font_size)
ax.set_ylabel('Energy: 1k Batches (kJ)', fontsize=label_font_size)
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
ax.set_ylim([0, 1.3])
# ax2.set_ylim([0, 50])

# Save the figure
fig.tight_layout()
plt.savefig("output/poisson2d5pt_batched_power.pdf", bbox_inches='tight')
# plt.show()
