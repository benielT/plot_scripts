import matplotlib.pyplot as plt
import numpy as np
from matplotlib.ticker import FormatStrFormatter
import pandas as pd
from barplot_params import general_font_size, power_marker_size, throughput_marker_size, label_font_size, \
    legends_font_size, bar_width, iner_props, outer_props, energy_bar_gap, energy_bar_width, colors, bar_offset, \
    fig_size, x_ticks_font_size, y_ticks_font_size, size_multiplier
from math import log2


df = pd.read_csv("data/Poisson2D5pt_throughput_u280.csv")

bar_width = 1/4

xticks = df["grid_size"].astype(str)
row_wise_tiling = df["tile8192_row"]
inter_u_tiling = df["tile8192_inter_u"]
inter_a_tiling = df["tile8192_inter_a"]

row_wise_tiling_pow = df["tile8192_row_pow"]
inter_u_tiling_pow = df["tile8192_inter_u_pow"]
inter_a_tiling_pow = df["tile8192_inter_a_pow"]

plt.rcParams["figure.figsize"] = fig_size
plt.rcParams.update({'font.size': general_font_size})
plt.rcParams['hatch.linewidth'] = 3  # Hatch line width
plt.rcParams['hatch.color'] = colors[1]

fig, ax = plt.subplots()
bar_offset = 0.0

x_indexes = np.arange(len(xticks))

tile_row_bar = ax.bar(x_indexes - bar_width + bar_offset, row_wise_tiling, width=bar_width, label='ROW', color=colors[5])
ax.bar(x_indexes - bar_width + bar_offset, row_wise_tiling, width=bar_width, color='none', edgecolor='black', **iner_props)

tile_inter_u_bar = ax.bar(x_indexes + bar_offset, inter_u_tiling, width=bar_width, label='ITR_U', color=colors[1])
ax.bar(x_indexes + bar_offset, inter_u_tiling, width=bar_width, color='none', edgecolor='black', **iner_props)

tile_inter_a_bar = ax.bar(x_indexes + bar_width + bar_offset, inter_a_tiling, width=bar_width, label='ITR_A', color=colors[9])
ax.bar(x_indexes + bar_width + bar_offset, inter_a_tiling, width=bar_width, color='none', edgecolor='black', **iner_props)

# plt.rcParams['hatch.color'] = colors[1]
# tile_8192_bar = ax.bar(x_indexes + bar_width + bar_offset, tile_8192, width=bar_width, label='T_8192', color='white', hatch='xx')
# ax.bar(x_indexes + bar_width + bar_offset, tile_8192, width=bar_width, color='none', edgecolor='black', **iner_props)

# for axis in (ax2,):
#     axis.bar(x_indexes - bar_width + bar_offset, row_wise_tiling, width=bar_width, color=colors[5])
#     axis.bar(x_indexes - bar_width + bar_offset, row_wise_tiling, width=bar_width, color='none', edgecolor='black', **iner_props)
    
#     axis.bar(x_indexes + bar_offset, inter_u_tiling, width=bar_width, color=colors[1])
#     axis.bar(x_indexes + bar_offset, inter_u_tiling, width=bar_width, color='none', edgecolor='black', **iner_props)
#     axis.bar(x_indexes + bar_width + bar_offset, inter_a_tiling, width=bar_width, color=colors[9])
#     axis.bar(x_indexes + bar_width + bar_offset, inter_a_tiling, width=bar_width, color='none', edgecolor='black', **iner_props)

ax2 = ax.twinx()
ax2.plot(x_indexes - bar_width, row_wise_tiling_pow, linestyle='dashdot', marker='^', markersize=(power_marker_size + 2), label="ROW energy", color='none', markerfacecolor='white', markeredgewidth=3.5 * size_multiplier, markeredgecolor=colors[12])
ax2.plot(x_indexes, inter_u_tiling_pow, linestyle='dashdot', marker='d', markersize=power_marker_size, label="ITR_U energy", color='none', markerfacecolor='white', markeredgewidth=3 * size_multiplier, markeredgecolor=colors[13])
ax2.plot(x_indexes + bar_width, inter_a_tiling_pow, linestyle='dashdot', marker='o', markersize=power_marker_size, label="ITR_A energy", color='none', markerfacecolor='white', markeredgewidth=3.5 * size_multiplier, markeredgecolor=colors[10])

# Format the axes
ax.yaxis.set_major_formatter(FormatStrFormatter('%.0f'))
ax2.yaxis.set_major_formatter(FormatStrFormatter('%.0f'))

# Add grid, labels, and legends
ax.grid(which='both', axis='y', linewidth=1 * size_multiplier, alpha=0.5)
# ax2.grid(which='both', axis='y', linewidth=1 * size_multiplier, alpha=0.5)
ax.set_xlabel('Mesh Size', fontsize=label_font_size)
ax.set_ylabel('Throughput (GFLOP/s)', fontsize=label_font_size)
ax2.set_ylabel('Energy: 1k Batches (kJ)', fontsize=label_font_size)
# fig.supylabel('Throughput (GFLOP/s)', x=0.02, y=0.5, fontsize=label_font_size,
#               va='center')
# ax2.set_ylabel('Energy: 1k Batches (kJ)', fontsize=label_font_size)
ax.set_xticks(x_indexes)
ax.set_xticklabels(xticks, rotation=0)

# Combine legends from both axes
handles1, labels1 = ax.get_legend_handles_labels()
handles2, labels2 = ax2.get_legend_handles_labels()
handles = handles1 + handles2
labels = labels1 + labels2
ax.legend(handles, labels, loc=2, ncol=4, facecolor='w', framealpha=1, edgecolor='black', prop={'size': legends_font_size})
# ax2.spines['top'].set_visible(False)
# ax.spines['bottom'].set_visible(False)
# ax.tick_params(labeltop=False, bottom=False)
# ax2.tick_params(top=False)

# Set axis limits
ax.set_ylim([0, 900])
ax2.set_ylim([0, 1750])

# d = 0.5
# kwargs = dict(marker=[(-1, -d), (1, d)], markersize=12,
#               linestyle='none', color='k', mec='k', mew=1, clip_on=False)
# ax.plot([0, 1], [0, 0], transform=ax.transAxes, **kwargs)
# ax2.plot([0, 1], [1, 1], transform=ax2.transAxes, **kwargs)

# Save the figure
fig.tight_layout()
plt.savefig("output/poisson2d_tiling_throughput_and_power.pdf", bbox_inches='tight')
# plt.show()