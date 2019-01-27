
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
    
    f, (ax1, ax2) = plt.subplots(2, 1)
    
    ax1.set_title('PDF of edit distribution of ' + l)
    
    ax1.set_ylabel('P(X = x)')
    
    fit = powerlaw.Fit(data, discrete=True)
    
    fit.power_law.plot_pdf(ax = ax1)
    
    plt.xlabel('Edits of distinct users')
    
    '''
    Alpha refers to the theoretical slope of the function and sigma to the std
    of the data.
    '''
    
    alpha = round(fit.power_law.alpha, 3)
    sigma = round(fit.power_law.sigma, 3)
    
    ax2.set_title( 'CDF, similarly (α = ' + str(alpha) 
                   + ', σ = ' + str(sigma) + ')' )
    
    powerlaw.plot_cdf(data)
    
    plt.xlabel('Edits of distinct users')
    
    plt.subplots_adjust(hspace = 0.8)
    
    plt.savefig( '../graphs/edits distributions/' +
                 'PDF and CDF of edit distribution of ' + l + '.png', 
                 dpi = 500)
    
    plt.show()


for l in langs_defs.IALs:
    df = pd.read_csv('../datasets/users coeditions/' + l + ' coeditions.csv')
    df = df['Contributions_in_' + l]
    df = df[~np.isnan(df)]
    data = np.array(df.values.tolist())
    
    fit = powerlaw.Fit(data, discrete=True)
    
    fit.power_law.plot_pdf()
    
plt.xlabel('Edits of distinct users')

plt.title('PDF of edit distribution of IALs users')

plt.legend(langs_defs.IALs)

plt.savefig( '../graphs/edits distributions/CDF of all.png', dpi = 500)
    
plt.show()

for l in langs_defs.IALs:
    df = pd.read_csv('../datasets/users coeditions/' + l + ' coeditions.csv')
    df = df['Contributions_in_' + l]
    df = df[~np.isnan(df)]
    data = np.array(df.values.tolist())
    
    powerlaw.plot_cdf(data)
    
plt.xlabel('Edits of distinct users')

plt.title('CDF of edit distribution of IALs users')

plt.legend(langs_defs.IALs)

plt.savefig( '../graphs/edits distributions/CDF of all.png', dpi = 500)
    
plt.show()
