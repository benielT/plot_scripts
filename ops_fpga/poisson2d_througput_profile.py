import matplotlib.pyplot as plt
import numpy as np
from matplotlib.ticker import FormatStrFormatter, MaxNLocator
import pandas as pd

# headers=["grid size","handcoded_u280","codegen_u280","handcoded_vck5000","codegen_vck5000"]
df = pd.read_csv("poisson2d_extended_codegen_u280.csv")
# print(df)

sorted_df= df.sort_values('num_elements')
# print("Sorted DF")
# print(sorted_df)

# print("query x=300")
query_300_df = sorted_df[sorted_df["grid_size"].str.contains("300x")]
min_300_num_elements = query_300_df["num_elements"][1:].min()
max_300_num_elements = query_300_df["num_elements"][1:].max()
# print(query_300_df)

# print("query x=400")
query_400_df = sorted_df[sorted_df["grid_size"].str.contains("400x")]
min_400_num_elements = query_400_df["num_elements"].min()
max_400_num_elements = query_400_df["num_elements"].max()
# print(query_400_df)

# make data
time_divisor = 1000
xticks = np.arange((min(min_300_num_elements, min_400_num_elements)/10000 - 1) * 10000, (max(max_300_num_elements, max_400_num_elements)/10000 + 2) * 10000, 10000)
print(xticks)
u280_300_x = query_300_df["num_elements"]
u280_300_grid = query_300_df["grid_size"]
u280_p54_300_y = query_300_df["codegen_u280_p54_throughput"]
u280_p60_300_y = query_300_df["codegen_u280_p60_throughput"]
u280_400_x = query_400_df["num_elements"]
u280_p54_400_y = query_400_df["codegen_u280_p54_throughput"]
u280_p60_400_y = query_400_df["codegen_u280_p60_throughput"]
# cgen_u280 = df["codegen_u280"] / time_divisor
# hand_vck5000 = df["handcoded_vck5000"] / time_divisor
# cgen_vck5000 = df["codegen_vck5000"] / time_divisor
# u280_imp = (df["handcoded_u280"] - df['codegen_u280']) / df["handcoded_u280"] * 100
# vck5000_imp = (df["handcoded_vck5000"] - df['codegen_vck5000']) / df["handcoded_vck5000"] * 100

# print(xticks)
# print(u280_imp)
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
line1 = ax.plot(u280_300_x[1:], u280_p54_300_y[1:], '-o', label="54PE x=300")
line2 = ax.plot(u280_300_x[1:], u280_p60_300_y[1:], '-o', label="60PE x=300")
line3 = ax.plot(u280_400_x, u280_p54_400_y, '-o', label="54PE x=400")
line4 = ax.plot(u280_400_x, u280_p60_400_y, '-o', label="60PE x=400")
# line2 = ax2.plot(x+0.25, vck5000_imp, color='#70915a', label="vck5000 Imp%")

ax.yaxis.set_major_formatter(FormatStrFormatter('%.0f'))
ax.xaxis.set_major_locator(MaxNLocator(integer=True))
# ax.xaxis.set_major_formatter(FormatStrFormatter('%.0f'))
# ax2.yaxis.set_major_formatter(FormatStrFormatter('%.0f'))
# plt.tight_layout()
adjusted_xticks = xticks[0:-1:2]/1000
plt.xticks(xticks[0:-1:2], xticks[0:-1:2])
ax.set_xticklabels([int(elem) for elem in adjusted_xticks], rotation=45)
plt.xticks(xticks)



for ind, val in enumerate(u280_p54_300_y[1:].to_list()):
       ax.text(u280_300_x[1:].to_list()[ind], val + (2 if ind%2 == 0 else -6), "{:.1f}".format(val), ha='center', size=10) 
    #    ax.text(u280_300_x[1:].to_list()[ind] + 2000, val + 2 , f"(y={u280_300_grid[1:].to_list()[ind][4:]})", ha='center', size=10, rotation=90)

for ind, val in enumerate(u280_p60_300_y[1:].to_list()):
        ax.text(u280_300_x[1:].to_list()[ind], val + (2 if ind%2 == 0 else -6), "{:.1f}".format(val), ha='center', size=10) 

for ind, val in enumerate(u280_p54_400_y.to_list()):
        ax.text(u280_400_x.to_list()[ind], val + 2, "{:.1f}".format(val), ha='center', size=10) 

for ind, val in enumerate(u280_p60_400_y.to_list()):
        ax.text(u280_400_x.to_list()[ind], val + 2, "{:.1f}".format(val), ha='center', size=10) 


# ax.set_yscale('log')
ax.set_axisbelow(True)
ax.grid(which='both', axis='y', linewidth=1, alpha=0.5)
handles, labels = ax.get_legend_handles_labels()



ax.legend(handles, labels, loc=2, ncol=3, facecolor='w', framealpha=1, edgecolor='black', prop={'size': 12})
ax.set_xlabel('Number of Elements (Thousands)')
ax.set_ylabel('Throughput (GOps/s)')


ax.set_ylim([625, 825])
# ax2.set_ylim([-20,60])

# fig.tight_layout()
plt.savefig("poisson2d_throughput_characteristic.pdf", bbox_inches='tight')

# # plt.show()