## Method Chaining
import pandas

def load_and_process_df1(url):
    
    df1 = pandas.read_csv(url)
    df1_1 = {
        df1.copy()
        .dropna(axis=0)
        .rename(columns={"Artisanal" : "Normal Fishing", "Subsistence": "Fishing for Survival"})
        .sort_values("Year", ascending=False)
        .reset_index(drop=True)
    }
    df1_2 = {
        df1_1.copy()
        .drop(['Entity','Code'],axis=1)
        .drop_duplicates(inplace=True)

    }
    return df1_2

def load_and_process_df2(url):
    
    df2 = pandas.read_csv(url)
    df2_1 = {
        df2.copy()
        .dropna(axis=0)
        .rename(columns={"Entity" : "Location"})
        .sort_values("Year", ascending=False)
        .reset_index(drop=True)
    }
    df2_2 = {
        df2_1.copy()
        .drop(['Code'],axis=1)
        .drop_duplicates(inplace=True)

    }
    return df2_2

