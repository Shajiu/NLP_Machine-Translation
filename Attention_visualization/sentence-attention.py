#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2019/12/1 23:09
# @USER:     ShaJiu
# @Author  : shajiu
# @FileName: sentence-attention.py
# @Software: PyCharm
# @DATE:     2019/12/1 
import seaborn as sns
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

region = ['Albania', 'Algeria', 'Angola', 'Argentina', 'Armenia', 'Azerbaijan',
       'Bahamas', 'Bangladesh', 'Belize', 'Bhutan', 'Bolivia',
       'Bosnia and Herzegovina', 'Brazil', 'Burkina Faso', 'Burundi',
       'Cambodia', 'Cameroon', 'Cape Verde', 'Chile', 'China', 'Colombia',
       'Costa Rica', 'Cote d Ivoire', 'Cuba', 'Cyprus',
       "Democratic People's Republic of Korea",
       'Democratic Republic of the Congo', 'Dominican Republic', 'Ecuador',
       'Egypt', 'El Salvador', 'Equatorial Guinea', 'Ethiopia', 'Fiji',
       'Gambia', 'Georgia', 'Ghana', 'Guatemala', 'Guyana', 'Honduras']

kind = ['Afforestation & reforestation', 'Biofuels', 'Biogas',
        'Biomass', 'Cement', 'Energy efficiency', 'Fuel switch',
       'HFC reduction/avoidance', 'Hydro power',
        'Leak reduction', 'Material use', 'Methane avoidance',
       'N2O decomposition', 'Other renewable energies',
       'PFC reduction and substitution','PV',
       'SF6 replacement', 'Transportation', 'Waste gas/heat utilization',
      'Wind power']

print(len(region))
print(len(kind))
np.random.seed(100)
arr_region = np.random.choice(region, size=(10000,))
list_region = list(arr_region)
arr_kind = np.random.choice(kind, size=(10000,))
list_kind = list(arr_kind)
values = np.random.randint(50, 1000, 10000)
list_values = list(values)
df = pd.DataFrame({'region':list_region,
                  'kind': list_kind,
                  'values':list_values})
df.head()
pt = df.pivot_table(index='kind', columns='region', values='values', aggfunc=np.sum)
pt.head()
f, ax = plt.subplots(figsize = (10, 4))
cmap = sns.cubehelix_palette(start = 1, rot = 3, gamma=0.8, as_cmap = True)
sns.heatmap(pt, cmap = cmap, linewidths = 0.05, ax = ax)
ax.set_title('Amounts per kind and region')
ax.set_xlabel('region')
ax.set_ylabel('kind')
f.savefig('sns_heatmap_normal.jpg', bbox_inches='tight')
plt.show()