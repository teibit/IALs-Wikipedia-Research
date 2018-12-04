
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
    df = pd.read_csv('../datasets/users coeditions/' + l + ' coeditions.csv')
    df = df['Contributions_in_' + l]
    df = df[~np.isnan(df)]
    data = np.array(df.values.tolist())
    
    plt.subplot(211)
    
    plt.title('PDF of edit distribution of ' + l)
    
    powerlaw.plot_pdf(data)
    
    plt.xlabel('Edits of distinct users')
    
    plt.ylabel('P(X = x)')
    
    plt.subplot(212)
    
    '''
    Alpha refers to the theoretical slope of the function and sigma to the std
    of the data.
    '''
    
    alpha = round(powerlaw.Fit(data, discrete = True).power_law.alpha, 3)
    sigma = round(powerlaw.Fit(data, discrete = True).power_law.sigma, 3)
    
    plt.title( 'CDF, similarly (α = ' + str(alpha) 
               + ', σ = ' + str(sigma) + ')' )
    
    powerlaw.plot_cdf(data)
    
    plt.xlabel('Edits of distinct users')
    
    plt.ylabel('P(X = x)')
    
    plt.subplots_adjust(hspace = 0.8)
    
    plt.savefig( '../graphs/edits distributions/' +
                 'PDF of edit distribution of ' + l + '.png', 
                 dpi = 500)
    
    plt.show()
