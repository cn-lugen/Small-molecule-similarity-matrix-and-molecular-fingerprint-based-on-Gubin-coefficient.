import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)
df = pd.read_csv("./data.csv",index_col=0)
print(df)
f, ax = plt.subplots(figsize=(12, 12))
mask = np.triu(np.ones_like(df,dtype=None))
fig=sns.heatmap(df,annot=True,mask=mask,
            linewidths=.06,square=True,annot_kws={'size':9})
plt.subplots_adjust(left=.1, right=0.95, bottom=0.22, top=0.95)
plt.xticks(fontsize=12,fontweight='bold')
plt.yticks(fontsize=12,fontweight='bold')
boxplot = fig.get_figure()
boxplot.savefig("a.png", dpi=400)
plt.show()

