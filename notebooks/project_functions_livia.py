## Method Chaining
import pandas

def load_and_process_df1(url):
    
    df1 = pd.read_csv(url, sep=',')
    
    indexEnt = df1_cleaned.loc[lambda row : row['Entity']=='World'].index
    
    df1_1 = {
        df1
        .dropna(axis=0)

    }
    df1_2 = {
        df1_1
        .copy().drop(['Code'], axis=1)

    }
    df1_3 = {
        df1_2
        .copy().drop(indexEnt, inplace=True)
        .rename(columns={'Entity': 'Country', 'Capture fisheries production (metric tons)': 'Capture fisheries production'})

    }
    df1_4 = {
        df1_3
        .sort_values(by=['Capture fisheries production'], ascending = False)

    }
    return df1_4

def load_and_process_df2(url):
    
    df2 = pd.read_csv(url, sep=',')
    
    indexEnt = df2_cleaned.loc[lambda row : row['Entity']=='World'].index
    
    df2_1 = {
        df2
        .dropna(axis=0)

    }
    df2_2 = {
        df2_1
        .copy().drop(['Code'], axis=1)

    }
    df2_3 = {
        df2_2
        .copy().drop(indexEnt, inplace=True)
        .rename(columns={'Entity': 'Country', 'Fish, Seafood- Food supply quantity (kg/capita/yr) (FAO, 2020)': 'Seafood supply'})
        
    }
    df2_4 = {
        df2_3
        .sort_values(by=['Seafood supply'], ascending = False)

    }
    return df1_4
