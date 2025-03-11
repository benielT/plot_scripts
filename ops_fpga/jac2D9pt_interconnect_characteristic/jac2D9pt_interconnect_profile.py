import matplotlib.pyplot as plt
import numpy as np
from matplotlib.ticker import FormatStrFormatter, MaxNLocator
import pandas as pd

df = pd.read_csv("jac2D9pt_interconnect_buffer_characteristic.csv")
df = df.sort_values("num_elements")

xticks = df["num_elements"]
u280_2024_x = df["u280_buff_size_2024_throughput"]
u280_8192_x = df["u280_buff_size_8192_throughput"]
vck5000_8192_x = df["vck5000_buff_size_8192_throughput"]
vck5000_16384_x = df["vck5000_buff_size_16384_throughput"]


# print(xticks)
# print(u280_2024_x)
# print(u280_8192_x)
# print(vck5000_8192_x)
# print(vck5000_16384_x)

plt.rcParams["figure.figsize"] = (9,5.5)
plt.rcParams.update({'font.size': 14})
plt.rcParams['hatch.linewidth'] = 3
plt.rcParams['hatch.color'] = '#6589cd'

fig, ax = plt.subplots()

# props = {'linestyle':'--', 'linewidth':'1.0'}
# x = np.arange(xticks.size)
# kwargs={'alpha': 1.0}
# bar1=ax.bar(x+0.00, hand_u280, color='white', width=0.2, hatch='//', label='hand_u280')
# bar1=ax.bar(x+0.00, hand_u280, color='none', width=0.2, edgecolor='black', **props)
# bar2=ax.bar(x+0.2, cgen_u280, color='#6589cd', width=0.2, label='cgen_u280', edgecolor='black')
# bar4=ax.bar(x+0.6, cgen_vck5000, color='#90c46e', width=0.2, label='cgen_vck5000', edgecolor='black')
# bar3=ax.bar(x+0.4, hand_vck5000, color='white', width=0.2, hatch='//', label='hand_vck5000', edgecolor='#90c46e')
# bar3=ax.bar(x+0.4, hand_vck5000, color='none', width=0.2, edgecolor='black', **props)
# ax2 = ax.twinx()
x = np.arange(xticks.size)
line1 = ax.plot(x, u280_2024_x, '-o', label="u280/2024")
line2 = ax.plot(x, u280_8192_x, '-o', label="u280/8192")
line3 = ax.plot(x, vck5000_8192_x, '-o', label="vck5000/8192")
line4 = ax.plot(x, vck5000_16384_x, '-o', label="vck5000/16384")
# line2 = ax2.plot(x+0.25, vck5000_imp, color='#70915a', label="vck5000 Imp%")

ax.yaxis.set_major_formatter(FormatStrFormatter('%.0f'))
ax.xaxis.set_major_locator(MaxNLocator(integer=True))
# ax.xaxis.set_major_formatter(FormatStrFormatter('%.0f'))
# ax2.yaxis.set_major_formatter(FormatStrFormatter('%.0f'))
# plt.tight_layout()
plt.xticks(x+0.250, xticks)
ax.set_xticklabels(xticks, rotation=45)


# for ind, val in enumerate(u280_p54_300_y[1:].to_list()):
#        ax.text(u280_300_x[1:].to_list()[ind], val + (2 if ind%2 == 0 else -6), "{:.1f}".format(val), ha='center', size=10) 
#     #    ax.text(u280_300_x[1:].to_list()[ind] + 2000, val + 2 , f"(y={u280_300_grid[1:].to_list()[ind][4:]})", ha='center', size=10, rotation=90)

# for ind, val in enumerate(u280_p60_300_y[1:].to_list()):
#         ax.text(u280_300_x[1:].to_list()[ind], val + (2 if ind%2 == 0 else -6), "{:.1f}".format(val), ha='center', size=10) 

# for ind, val in enumerate(u280_p54_400_y.to_list()):
#         ax.text(u280_400_x.to_list()[ind], val + 2, "{:.1f}".format(val), ha='center', size=10) 

# for ind, val in enumerate(u280_p60_400_y.to_list()):
#         ax.text(u280_400_x.to_list()[ind], val + 2, "{:.1f}".format(val), ha='center', size=10) 


# ax.set_yscale('log')
ax.set_axisbelow(True)
ax.grid(which='both', axis='y', linewidth=1, alpha=0.5)
handles, labels = ax.get_legend_handles_labels()



ax.legend(handles, labels, loc=2, ncol=3, facecolor='w', framealpha=1, edgecolor='black', prop={'size': 12})
ax.set_xlabel('number of elements')
ax.set_ylabel('Throughput (GOps/s)')


ax.set_ylim([80, 700])
# ax2.set_ylim([-20,60])

# fig.tight_layout()
plt.savefig("jac2d9pt_interconnect_characteristic.pdf", bbox_inches='tight')

# # plt.show()