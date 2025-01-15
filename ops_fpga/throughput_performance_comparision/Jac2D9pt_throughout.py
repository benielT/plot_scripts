import matplotlib.pyplot as plt
import numpy as np
from matplotlib.ticker import FormatStrFormatter
import pandas as pd

# headers=["grid size","handcoded_u280","codegen_u280","handcoded_vck5000","codegen_vck5000"]
df = pd.read_csv("Jac2D9pt_throughput.csv")

print(df.head())

# make data
xticks = df["grid_size"]
hand_u280 = df["handcoded_u280"]
cgen_u280 = df["codegen_u280"]
hand_vck5000 = df["handcoded_vck5000"] 
cgen_vck5000 = df["codegen_vck5000"] 
u280_imp = (df['codegen_u280'] - df["handcoded_u280"]) / df["handcoded_u280"] * 100
vck5000_imp = (df['codegen_vck5000'] - df["handcoded_vck5000"]) / df["handcoded_vck5000"] * 100

print(xticks)
print(u280_imp)
plt.rcParams["figure.figsize"] = (9,5.5)
plt.rcParams.update({'font.size': 14})
plt.rcParams['hatch.linewidth'] = 3
plt.rcParams['hatch.color'] = '#6589cd'

fig, ax = plt.subplots()

props = {'linestyle':'--', 'linewidth':'1.0'}
x = np.arange(xticks.size)
kwargs={'alpha': 1.0}
bar1=ax.bar(x+0.00, hand_u280, color='white', width=0.2, hatch='//', label='hand_u280')
bar1=ax.bar(x+0.00, hand_u280, color='none', width=0.2, edgecolor='black', **props)
bar2=ax.bar(x+0.2, cgen_u280, color='#6589cd', width=0.2, label='cgen_u280', edgecolor='black')
bar4=ax.bar(x+0.6, cgen_vck5000, color='#90c46e', width=0.2, label='cgen_vck5000', edgecolor='black')
bar3=ax.bar(x+0.4, hand_vck5000, color='white', width=0.2, hatch='//', label='hand_vck5000', edgecolor='#90c46e')
bar3=ax.bar(x+0.4, hand_vck5000, color='none', width=0.2, edgecolor='black', **props)
ax2 = ax.twinx()
line1 = ax2.plot(x+0.25, u280_imp, color='#4768a6', label="u280 Imp%")
line2 = ax2.plot(x+0.25, vck5000_imp, color='#70915a', label="vck5000 Imp%")

ax.yaxis.set_major_formatter(FormatStrFormatter('%.0f'))
ax2.yaxis.set_major_formatter(FormatStrFormatter('%.0f'))
plt.tight_layout()
plt.xticks(x+0.250, xticks)
ax.set_xticklabels(xticks, rotation=45)




# for ind, val in enumerate(hand_u280):
#        ax.text(x[ind], val + 4 , "{:.2f}".format(val), ha='center', size=10, rotation=90) 

# for ind, val in enumerate(cgen_u280):
#        ax.text(x[ind]+0.2, val + 4 , "{:.2f}".format(val), ha='center', size=10, rotation=90) 

# for ind, val in enumerate(hand_vck5000):
#        ax.text(x[ind]+0.4, val + 4 , "{:.2f}".format(val), ha='center', size=10, rotation=90) 

# for ind, val in enumerate(cgen_vck5000):
#        ax.text(x[ind]+0.6, val + 4 , "{:.2f}".format(val), ha='center', size=10, rotation=90) 
       
# ax.set_yscale('log')
ax.set_axisbelow(True)
ax.grid(which='both', axis='y', linewidth=1, alpha=0.5)
handles1, labels1 = ax.get_legend_handles_labels()
handles2, labels2 = ax2.get_legend_handles_labels()
handles = handles1 + handles2
labels = labels1 + labels2


ax.legend(handles, labels, loc=2, ncol=3, facecolor='w', framealpha=1, edgecolor='black', prop={'size': 12})
ax.set_xlabel('Mesh Size')
ax.set_ylabel('Throughput (Gflops/s)')
ax2.set_ylabel('% Improvement')

ax.set_ylim([0, 1150])
ax2.set_ylim([-5,100])

fig.tight_layout()
plt.savefig("jac2d9pt_throughput.pdf", bbox_inches='tight')

# plt.show()