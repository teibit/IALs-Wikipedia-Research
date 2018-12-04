
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.sankey import Sankey
import langs_defs

###############################################################################
# Coeditions.                                                                 #
#                                                                             #
# This subroutine will plot a histogram of the amount of users that edit in a #
# specific IAL AND all other languages we're considering.                     #
###############################################################################

def language_coeditions(lang):
    
    '''
    Read the dataset for the language.
    '''
    
    df = pd.read_csv('../datasets/users coeditions/' + lang + ' coeditions.csv')
    
    '''
    If we consider coeditions of an IAL then we won't show that IAL data and
    will exclude it from the main list.
    
    Create then the appropriate dataframe to hold the data.
    '''
    
    dfindex = [1,2,3,4,5,6] if lang in langs_defs.IALs else [1,2,3,4,5,6,7]
    
    new_df = pd.DataFrame( columns = ['IAL', 'Editors'], index = dfindex )
    
    IALs_others = langs_defs.IALs.copy()
    
    if lang in langs_defs.IALs:
        IALs_others.remove(lang)
    
    '''
    Fill this dataframe with the name of the IAL and the amount of non-null
    user entries there is, effectively yielding the amount of users that edit.
    '''
    
    for l, i in zip(IALs_others, range(1, len(IALs_others) + 1)):
        
        new_df.loc[i] = [l, df[df['Contributions_in_' + l].notnull()].shape[0]]
    
    '''
    Normalize the data in proportion to the editors of the language we're
    considering. This will show what is the percentage of users from the
    given language that coedit in other languages.
    '''
    
    lang_editors = df['Contributions_in_' + lang].notnull().shape[0]
    new_df['Editors'] = new_df['Editors'] / lang_editors
    
    '''
    Plotting. Don't pay much attention to this part, it's mostly settings
    that make the graphs look good and save them.
    '''
    
    sankey_flows = []
    sankey_labels = []
    
    for l, i in zip(IALs_others, range(1, len(IALs_others) + 1)):
        
        sankey_flows.append(round(new_df.loc[i, ['Editors']]['Editors'], 5))
        
        sankey_labels.append(l)
    
    ortts1, ortts2 = [1,-1,1,-1,1,-1], [1,-1,1,-1,1,-1,1]
    
    sorientations = ortts1 if lang in langs_defs.IALs else ortts2
    
    plt.figure(figsize = (13, 7))
                     
    Sankey( flows = sankey_flows,
            labels = sankey_labels, 
            orientations = sorientations,
            pathlengths = new_df['Editors'].tolist(),
            trunklength = 1.4,
            scale = 0.4,
            gap = 1,
            offset = 0.4,
            rotation = -180 ).finish()
    
    plt.title( "Flow of " + lang + " users that coedit in other IALs" )
    
    plt.savefig( '../graphs/flows/' + 
                 'Flow of ' + lang + ' users that coedit in other IALs.png', 
                 dpi = 400 )

######################################################
# How many users edit in a language AND in ALL IALs? # 
######################################################

for l in langs_defs.IALs + langs_defs.top_langs:
    language_coeditions(l)
    
