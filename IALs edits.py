
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import langs_defs

############################################
# Users that edit in IAL and top languages # 
############################################

all_edits = []

'''
For every language create an entry to a dataframe containing its name and
every non-null user's editcount.
'''

for l in langs_defs.IALs:
    df = pd.read_csv('users coeditions/' + l + ' coeditions.csv')
    df = df['Contributions_in_' + l]
    df = df[~np.isnan(df)]
    all_edits.append((l, df.values.tolist()))
        
for tl in langs_defs.top_langs:
    df2 = pd.read_csv('users edits in top langs/' + tl + ' edits.csv')
    df2 = df2['Edits']
    all_edits.append((tl, df2.values.tolist()))

'''
Let us sort the boxplots by the following percentile.
'''

percentile = 75

all_edits.sort(key = lambda x: np.percentile(x[1], percentile))

'''
Plotting.
'''

plt.figure(figsize = (20, 10))

plt.boxplot( [ all_edits[i][1] for i in range(len(all_edits)) ], 
             showfliers = False, 
             labels = [ all_edits[i][0] for i in range(len(all_edits)) ] )

plt.title('Editors ordered by the ' + str(percentile) + '% percentile.')
plt.xlabel('Language')
plt.ylabel('Number of edits')
plt.show()
