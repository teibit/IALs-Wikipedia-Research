
import matplotlib.pyplot as plt
import pandas as pd
import langs_defs

##############################
# Articles per editors ratio # 
##############################

x_axis = 'Editors'
y_axis = 'Articles'

df = pd.read_csv('../datasets/articles-editors.csv')

plt.figure(figsize=(8,6))

plt.title( "Ratio of articles per editor in IALs" + 
           "\nDots show the corresponding value." )

for i in range(0,7):
    
    plt.scatter(df[x_axis][i], df[y_axis][i])
    
    plt.text( df[x_axis][i], 
             
              df[y_axis][i], 
              
              # ratio of actual values, not logarithmically scaled
              # computing: articles/editors
              round(df[y_axis][i] / df[x_axis][i], 2),
              
              horizontalalignment = 'left' if i in (2,5) else 'right')

plt.legend(langs_defs.IALs)

plt.xscale('log')
plt.yscale('log')

plt.xlabel("Number of " + x_axis)
plt.ylabel("Number of " + y_axis)

plt.savefig('../graphs/articles-editors.png', dpi = 500)

plt.show()
