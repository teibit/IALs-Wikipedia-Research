
import numpy as np
import pandas as pd
import langs_defs

#################################
# How many IAL users are there? # 
#################################

'''
Dataframe to be filled up with the amount of editors of each IAL.
'''

IAL_editors = pd.DataFrame()

'''
For each IAL, read every non-null user entry and count all of them,
effectively yielding the amount of editors there is.
'''

for l, i in zip(langs_defs.IALs, range(1, len(langs_defs.IALs) + 1)):
    df = pd.read_csv('../datasets/users coeditions/' + l + ' coeditions.csv')
    df = df['Contributions_in_' + l]
    df = df[~np.isnan(df)]
    IAL_editors = pd.concat( [ IAL_editors, 
                               pd.DataFrame( { 'IAL' : l, 
                                               'Editors' : df.shape[0] }, 
                                             index = [i] ) ] )

'''
Plotting. Saving the image assumes there exists a folder called graphs and
that this code file is in a different folder, both inside the same folder.
'''

IAL_editors = IAL_editors.sort_values(['Editors'])

graph = IAL_editors.plot( x = 'IAL', 
                          y = 'Editors', 
                          kind = 'barh', 
                          title = 'Editors in IALs.',
                          figsize = (40,20),
                          fontsize = 28,
                          xticks = [837, 2963, 16262, 67852], 
                          grid = True)

fig = graph.get_figure()
fig.savefig('../graphs/IAL_users.png')
