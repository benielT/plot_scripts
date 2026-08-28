import matplotlib.pyplot as plt
import numpy as np
from matplotlib.ticker import FormatStrFormatter
import pandas as pd
from barplot_params import general_font_size, power_marker_size, throughput_marker_size, label_font_size, \
    legends_font_size, bar_width, iner_props, outer_props, energy_bar_gap, energy_bar_width, colors, bar_offset, \
    fig_size, x_ticks_font_size, y_ticks_font_size, size_multiplier
from math import log2


df = pd.read_csv("data/Poisson2D5pt_throughput_u280.csv")

bar_width = 1/5

xticks = df["grid_size"].astype(str)
tile_1024 = df["tile1024_row"]
tile_2048 = df["tile2048_row"]
tile_4096 = df["tile4096_row"]
tile_8192 = df["tile8192_row"]

plt.rcParams["figure.figsize"] = fig_size
plt.rcParams.update({'font.size': general_font_size})
plt.rcParams['hatch.linewidth'] = 3  # Hatch line width
plt.rcParams['hatch.color'] = colors[1]

fig, (ax, ax2) = plt.subplots(
    2, 1, sharex=True,
    gridspec_kw={'height_ratios': [3, 1], 'hspace': 0.05}
)
bar_offset = bar_width/6

x_indexes = np.arange(len(xticks))

tile_1024_bar = ax.bar(x_indexes - bar_width * 2 + bar_offset, tile_1024, width=bar_width, label='T_1024', color=colors[5])
ax.bar(x_indexes - bar_width * 2 + bar_offset, tile_1024, width=bar_width, color='none', edgecolor='black', **iner_props)

tile_2048_bar = ax.bar(x_indexes - bar_width + bar_offset, tile_2048, width=bar_width, label='T_2048', color=colors[1])
ax.bar(x_indexes - bar_width + bar_offset, tile_2048, width=bar_width, color='none', edgecolor='black', **iner_props)

tile_4096_bar = ax.bar(x_indexes + bar_offset, tile_4096, width=bar_width, label='T_4096', color=colors[9])
ax.bar(x_indexes + bar_offset, tile_4096, width=bar_width, color='none', edgecolor='black', **iner_props)

plt.rcParams['hatch.color'] = colors[1]
tile_8192_bar = ax.bar(x_indexes + bar_width + bar_offset, tile_8192, width=bar_width, label='T_8192', color='white', hatch='xx')
ax.bar(x_indexes + bar_width + bar_offset, tile_8192, width=bar_width, color='none', edgecolor='black', **iner_props)

for axis in (ax2,):
    axis.bar(x_indexes - bar_width * 2 + bar_offset, tile_1024, width=bar_width, color=colors[5])
    axis.bar(x_indexes - bar_width * 2 + bar_offset, tile_1024, width=bar_width, color='none', edgecolor='black', **iner_props)
    axis.bar(x_indexes - bar_width + bar_offset, tile_2048, width=bar_width, color=colors[1])
    axis.bar(x_indexes - bar_width + bar_offset, tile_2048, width=bar_width, color='none', edgecolor='black', **iner_props)
    axis.bar(x_indexes + bar_offset, tile_4096, width=bar_width, color=colors[9])
    axis.bar(x_indexes + bar_offset, tile_4096, width=bar_width, color='none', edgecolor='black', **iner_props)
    axis.bar(x_indexes + bar_width + bar_offset, tile_8192, width=bar_width, color='white', hatch='xx')
    axis.bar(x_indexes + bar_width + bar_offset, tile_8192, width=bar_width, color='none', edgecolor='black', **iner_props)

# Format the axes
ax.yaxis.set_major_formatter(FormatStrFormatter('%.0f'))
ax2.yaxis.set_major_formatter(FormatStrFormatter('%.0f'))

# Add grid, labels, and legends
ax.grid(which='both', axis='y', linewidth=1 * size_multiplier, alpha=0.5)
ax2.grid(which='both', axis='y', linewidth=1 * size_multiplier, alpha=0.5)
ax2.set_xlabel('Mesh Size', fontsize=label_font_size)
fig.supylabel('Throughput (GFLOP/s)', x=0.02, y=0.5, fontsize=label_font_size,
              va='center')
# ax2.set_ylabel('Energy: 1k Batches (kJ)', fontsize=label_font_size)
ax2.set_xticks(x_indexes)
ax2.set_xticklabels(xticks, rotation=0)

# Combine legends from both axes
handles1, labels1 = ax.get_legend_handles_labels()
# handles2, labels2 = ax2.get_legend_handles_labels()
handles = handles1 #+ handles2
labels = labels1 #+ labels2
ax.legend(handles, labels, loc=2, ncol=4, facecolor='w', framealpha=1, edgecolor='black', prop={'size': legends_font_size})
ax2.spines['top'].set_visible(False)
ax.spines['bottom'].set_visible(False)
ax.tick_params(labeltop=False, bottom=False)
ax2.tick_params(top=False)

# Set axis limits
ax.set_ylim([600, 730])
ax2.set_ylim([0, 600])

d = 0.5
kwargs = dict(marker=[(-1, -d), (1, d)], markersize=12,
              linestyle='none', color='k', mec='k', mew=1, clip_on=False)
ax.plot([0, 1], [0, 0], transform=ax.transAxes, **kwargs)
ax2.plot([0, 1], [1, 1], transform=ax2.transAxes, **kwargs)

# Save the figure
fig.tight_layout(rect=(0.06, 0, 1, 1))
plt.savefig("output/poisson2d_tiling_row_throughput_barplot.pdf", bbox_inches='tight')
# plt.show()