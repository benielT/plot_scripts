import matplotlib.pyplot as plt
import numpy as np
from matplotlib.ticker import FormatStrFormatter
import pandas as pd
from barplot_params import general_font_size, power_marker_size, throughput_marker_size, label_font_size, \
    legends_font_size, bar_width, iner_props, outer_props, energy_bar_gap, energy_bar_width, colors, bar_offset

# Color Palette
# colors = ['#003f5c', '#58508d', '#bc5090', '#ff6361', '#ffa600', '#34a853', '#ce87e6']
# colors = ['#4e79a7', '#f28e2b', '#e15759', '#76b7b2', '#59a14f', '#edc949', '#af7aa1' ]
# colors = ['#A6CEE3', '#1F78B4', '#B2DF8A', '#33A02C', '#FB9A99', '#E31A1C', '#FDBF6F']

# Load data
df = pd.read_csv("data/Poisson2D5pt_throughput.csv")

# Extract data
xticks = df["grid_size"]
hand_u280 = df["handcoded_u280"]
cgen_u280 = df["codegen_u280"]
hand_vck5000 = df["handcoded_vck5000"]
cgen_vck5000 = df["codegen_vck5000"]
cgen_u280_power = df["pow_C_U280_1000B"]
cgen_vck5000_power = df["pow_C_VCK5000_1000B"]
h100_power = df["pow_H100_1000B"]
# u280_imp = (df['codegen_u280'] - df["handcoded_u280"]) / df["handcoded_u280"] * 100
# vck5000_imp = (df['codegen_vck5000'] - df["handcoded_vck5000"]) / df["handcoded_vck5000"] * 100
h100_1b = df["H100_1B"]
h100_100b = df["H100_100B"]

# Configure plot settings
plt.rcParams["figure.figsize"] = (9, 4.5)
plt.rcParams.update({'font.size': general_font_size})
plt.rcParams['hatch.linewidth'] = 2
plt.rcParams['hatch.color'] = colors[1]

fig, ax = plt.subplots()
bar_offset = 0.0
x_indexes = np.arange(len(xticks))


# Plot throughput as bars
plt.rcParams['hatch.color'] = colors[5]
bar2 = ax.bar(x_indexes - bar_width + bar_offset, cgen_u280, width=bar_width, label='c_U280', color=colors[5])
bar2 = ax.bar(x_indexes - bar_width + bar_offset, cgen_u280, width=bar_width, color='none', edgecolor='black', **iner_props)

plt.rcParams['hatch.color'] = colors[5]
bar1 = ax.bar(x_indexes - bar_width + bar_offset, hand_u280, width=bar_width, label='h_U280', color='white', hatch='xxx')
bar1 = ax.bar(x_indexes - bar_width + bar_offset, hand_u280, width=bar_width, color='none', edgecolor='black', **iner_props)


bar5 = ax.bar(x_indexes + bar_offset, cgen_vck5000, width=bar_width, label='c_VCK', color=colors[0])
bar5 = ax.bar(x_indexes + bar_offset, cgen_vck5000, width=bar_width, color='none', edgecolor='black', **iner_props)

plt.rcParams['hatch.color'] = colors[0]
bar4 = ax.bar(x_indexes + bar_offset, hand_vck5000, width=bar_width, label='h_VCK', color='white', hatch='///')
bar4 = ax.bar(x_indexes + bar_offset, hand_vck5000, width=bar_width, color='none', edgecolor='black', **iner_props)

bar6 = ax.bar(x_indexes + bar_width + bar_offset, h100_100b, width=bar_width, label='H100_100B', color=colors[9])
bar6 = ax.bar(x_indexes + bar_width + bar_offset, h100_100b, width=bar_width, color='none', edgecolor='black', **iner_props)

plt.rcParams['hatch.color'] = colors[9]
bar7 = ax.bar(x_indexes + bar_width + bar_offset, h100_1b, width=bar_width, label='H100_1B', color='white', hatch='---')
bar7 = ax.bar(x_indexes + bar_width + bar_offset, h100_1b, width=bar_width, color='none', edgecolor='black', **iner_props)


# plt.rcParams['hatch.color'] = colors[4]
# bar1 = ax.bar(x_indexes - bar_width, hand_u280, width=bar_width, hatch='//', label='h_U280', color='white')
# bar1 = ax.bar(x_indexes - bar_width, hand_u280, width=bar_width, color='none', edgecolor='white', **props)

# bar4 = ax.bar(x_indexes + bar_width, hand_vck5000, width=bar_width, hatch='//', label='h_U280', color='white')
# bar4 = ax.bar(x_indexes + bar_width, hand_vck5000, width=bar_width, color='none', edgecolor='black', **props)
# bar5 = ax.bar(x_indexes + 2 * bar_width, cgen_vck5000, width=bar_width, label='c_VCK', color=colors[2])
# bar6 = ax.bar(x_indexes + 3 * bar_width, h100_1b, width=bar_width, label='H100_1B', color=colors[4])
# bar7 = ax.bar(x_indexes + 4 * bar_width, h100_100b, width=bar_width, label='H100_100B', color=colors[5])

# Add secondary y-axis for power usage
ax2 = ax.twinx()
ax2.plot(x_indexes - bar_width, cgen_u280_power, linestyle='dashdot', marker='^', markersize=power_marker_size + 2, label="U280 energy", color='none', markerfacecolor='white', markeredgewidth=3.5, markeredgecolor=colors[12])
ax2.plot(x_indexes, cgen_vck5000_power, linestyle='dashdot', marker='d', markersize=power_marker_size, label="VCK5000 energy", color='none', markerfacecolor='white', markeredgewidth=3, markeredgecolor=colors[13])
ax2.plot(x_indexes + bar_width, h100_power, linestyle='dashdot', marker='o', markersize=power_marker_size, label="H100 energy", color='none', markerfacecolor='white', markeredgewidth=3.5, markeredgecolor=colors[10])

# ax2.plot(x_indexes, cgen_4096_u280_power, linestyle='dashdot', marker='^', markersize=power_marker_size, label="U280_4096 energy", color='#6d65a3', markeredgecolor='#000000')
# ax2.plot(x_indexes, cgen_8192_u280_power, linestyle='dashdot', marker='^', markersize=power_marker_size, label="U280_8192 energy", color='#d9b3e6', markeredgecolor='#000000')
# ax2.plot(x_indexes, h100_power, linestyle='dashdot', marker='^', markersize=power_marker_size, label="H100 energy", color='#4dc46d', markeredgecolor='#000000')

# plt.rcParams['hatch.color'] = colors[7]
# bar9 = ax2.bar(x_indexes + bar_width + energy_bar_gap, h100_power, width=energy_bar_width, label='H100 energy', color=colors[10])
# bar9 = ax2.bar(x_indexes + bar_width + energy_bar_gap, h100_power, width=energy_bar_width, color='none', edgecolor='black', **outer_props)


# plt.rcParams['hatch.color'] = colors[10]
# bar8 = ax2.bar(x_indexes + bar_width + energy_bar_gap, cgen_u280_power, width=energy_bar_width, hatch="\\\\\\", label='U280 energy', color='white')
# bar8 = ax2.bar(x_indexes + bar_width + energy_bar_gap, cgen_u280_power, width=energy_bar_width, color='none', edgecolor='black', **outer_props)

# Format the axes
ax.yaxis.set_major_formatter(FormatStrFormatter('%.0f'))
ax2.yaxis.set_major_formatter(FormatStrFormatter('%.0f'))

# Labels, grid, and legend
ax.grid(which='both', axis='y', linewidth=1, alpha=0.5)
ax.set_xlabel('Mesh Size', fontsize=label_font_size)
ax.set_ylabel('Throughput (GFLOP/s)', fontsize=label_font_size)
ax2.set_ylabel('Energy: 1k Batches (kJ)', fontsize=label_font_size)
ax.set_xticks(x_indexes)
ax.set_xticklabels(xticks, rotation=0)

# Combine legends from both axes
handles1, labels1 = ax.get_legend_handles_labels()
handles2, labels2 = ax2.get_legend_handles_labels()
handles = handles1 + handles2
labels = labels1 + labels2
ax.legend(handles, labels, loc=2, ncol=3, facecolor='w', framealpha=1, edgecolor='black', prop={'size': 13})

# Set axis limits
ax.set_ylim([0, 1300])
ax2.set_ylim([0, 45])

# Save the figure
fig.tight_layout()
plt.savefig("output/poisson2d5pt_throughput_barplot.pdf", bbox_inches='tight')
