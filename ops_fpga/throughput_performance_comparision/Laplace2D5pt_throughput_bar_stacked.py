import matplotlib.pyplot as plt
import numpy as np
from matplotlib.ticker import FormatStrFormatter
import pandas as pd
from lineplot_params import general_font_size, power_marker_size, throughput_marker_size, label_font_size, legends_font_size

# Color Palette
# colors = ['#003f5c', '#58508d', '#bc5090', '#ff6361', '#ffa600', '#34a853', '#ce87e6']
# colors = ['#4e79a7', '#f28e2b', '#e15759', '#76b7b2', '#59a14f', '#edc949', '#af7aa1' ]
# colors = ['#A6CEE3', '#1F78B4', '#B2DF8A', '#33A02C', '#FB9A99', '#E31A1C', '#FDBF6F']
colors = ['#f05039', '#E57a77', '#eebab4', '#1f449c', '#3d65a5', '#7ca1cc', '#a8b6cc', '#8a5e00', '#ffc626', '#e6cf8e', '#5a626e', '#5c9e73']
# Load data
df = pd.read_csv("data/Laplace2D5pt_throughput.csv")

# Extract data
xticks = df["grid_size"]
# hand_u280 = df["handcoded_u280"]
cgen_u280 = df["codegen_u280"]
# hand_vck5000 = df["handcoded_vck5000"]
cgen_vck5000 = df["codegen_vck5000"]
# u280_imp = (df['codegen_u280'] - df["handcoded_u280"]) / df["handcoded_u280"] * 100
# vck5000_imp = (df['codegen_vck5000'] - df["handcoded_vck5000"]) / df["handcoded_vck5000"] * 100
h100_1b = df["H100_1B"]
h100_100b = df["H100_100B"]
cgen_u280_power = df["pow_C_U280_1000B"]
h100_power = df["pow_H100_1000B"]


# Configure plot settings
plt.rcParams["figure.figsize"] = (9, 5.5)
plt.rcParams.update({'font.size': general_font_size})
plt.rcParams['hatch.linewidth'] = 2
plt.rcParams['hatch.color'] = colors[1]

fig, ax = plt.subplots()

bar_width = 0.15  # Adjust as needed
energy_bar_width = 0.10
energy_bar_gap = 0.12
x_indexes = np.arange(len(xticks))

iner_props = {'linestyle':'-', 'linewidth':'1.0'}
outer_props = {'linestyle':'-', 'linewidth':'1.0'}
# Plot throughput as bars
plt.rcParams['hatch.color'] = colors[5]
bar2 = ax.bar(x_indexes - 2*bar_width, cgen_u280, width=bar_width, label='c_U280', color=colors[5])
bar2 = ax.bar(x_indexes - 2*bar_width, cgen_u280, width=bar_width, color='none', edgecolor='black', **iner_props)

# plt.rcParams['hatch.color'] = colors[5]
# bar1 = ax.bar(x_indexes - 2*bar_width, hand_u280, width=bar_width, label='h_U280', color='white', hatch='xxx')
# bar1 = ax.bar(x_indexes - 2*bar_width, hand_u280, width=bar_width, color='none', edgecolor='black', **iner_props)


bar5 = ax.bar(x_indexes - bar_width, cgen_vck5000, width=bar_width, label='c_VCK', color=colors[0])
bar5 = ax.bar(x_indexes - bar_width, cgen_vck5000, width=bar_width, color='none', edgecolor='black', **iner_props)

# plt.rcParams['hatch.color'] = colors[0]
# bar4 = ax.bar(x_indexes - bar_width, hand_vck5000, width=bar_width, label='h_VCK', color='white', hatch='///')
# bar4 = ax.bar(x_indexes - bar_width, hand_vck5000, width=bar_width, color='none', edgecolor='black', **iner_props)

bar6 = ax.bar(x_indexes, h100_100b, width=bar_width, label='H100_100B', color=colors[9])
bar6 = ax.bar(x_indexes, h100_100b, width=bar_width, color='none', edgecolor='black', **iner_props)

plt.rcParams['hatch.color'] = colors[9]
bar7 = ax.bar(x_indexes, h100_1b, width=bar_width, label='H100_1B', color='white', hatch='---')
bar7 = ax.bar(x_indexes, h100_1b, width=bar_width, color='none', edgecolor='black', **iner_props)


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
# ax2.plot(x_indexes, cgen_4096_u280_power, linestyle='dashdot', marker='^', markersize=power_marker_size, label="U280_4096 energy", color='#6d65a3', markeredgecolor='#000000')
# ax2.plot(x_indexes, cgen_8192_u280_power, linestyle='dashdot', marker='^', markersize=power_marker_size, label="U280_8192 energy", color='#d9b3e6', markeredgecolor='#000000')
# ax2.plot(x_indexes, h100_power, linestyle='dashdot', marker='^', markersize=power_marker_size, label="H100 energy", color='#4dc46d', markeredgecolor='#000000')

# plt.rcParams['hatch.color'] = colors[7]
bar9 = ax2.bar(x_indexes + bar_width + energy_bar_gap, h100_power, width=energy_bar_width, label='H100 energy', color=colors[10])
bar9 = ax2.bar(x_indexes + bar_width + energy_bar_gap, h100_power, width=energy_bar_width, color='none', edgecolor='black', **outer_props)


plt.rcParams['hatch.color'] = colors[10]
bar8 = ax2.bar(x_indexes + bar_width + energy_bar_gap, cgen_u280_power, width=energy_bar_width, hatch="\\\\\\", label='U280 energy', color='white')
bar8 = ax2.bar(x_indexes + bar_width + energy_bar_gap, cgen_u280_power, width=energy_bar_width, color='none', edgecolor='black', **outer_props)

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
ax.legend(handles, labels, loc=2, ncol=2, facecolor='w', framealpha=1, edgecolor='black', prop={'size': 13})

# Set axis limits
ax.set_ylim([0, 1380])
ax2.set_ylim([0, 50])

# Save the figure
fig.tight_layout()
plt.savefig("output/laplace2d5pt_throughput_barplot.pdf", bbox_inches='tight')
