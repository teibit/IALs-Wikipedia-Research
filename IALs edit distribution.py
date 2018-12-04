
import pandas as pd
import numpy as np
import powerlaw
import matplotlib.pyplot as plt
import langs_defs

###################################################
# Edits distribution per user on various projects # 
###################################################¡

'''
For every IAL plot the edit distribution considering every non-null user
editcount using powerlaw.Fit().
'''

for l in langs_defs.IALs:
    df = pd.read_csv('users coeditions/' + l + ' coeditions.csv')
    df = df['Contributions_in_' + l]
    df = df[~np.isnan(df)]
    data = np.array(df.values.tolist())
    
    plt.title('PDF of edit distribution of ' + l + ' with alpha = ' 
              + str(round(powerlaw.Fit(data, discrete = True).power_law.alpha, 
                          2)))
    
    powerlaw.plot_pdf(data)
    
    plt.xlabel('Edits of distinct users')
    
    plt.ylabel('P(X = x)')
    
    plt.show()
