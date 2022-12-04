
# Method Chaining

import pandas as pd

def load_and_process(rawFile):
    
    df = pd.read_csv(rawFile, sep=',')
    
    df_cleaned = (
                df.copy().dropna()
                  .drop(['Code','Recreational','Subsistence'], axis=1)
                . rename(columns = {'Aquaculture production (metric tons)':'Aquaculture production', 'Capture fisheries production (metric tons)': 'Capture fisheries production'})
                  .rename(columns={'Fish, Seafood- Food supply quantity (kg/capita/yr) (FAO, 2020)': 'Sea food supply', 'Share of fish stocks within biologically sustainable levels (FAO, 2020)': 'Sustainable fish stock share'})
                  .rename(columns={'Share of fish stocks that are overexploited': 'Overexploited fish stock share', 'Artisanal (small-scale commercial)': 'Artisanal fisheries'})
                  .rename(columns={'Discards': 'Discards portion', 'Commodity Balances - Livestock and Fish Primary Equivalent - Pelagic Fish - 2763 - Production - 5510 - tonnes': 'Pelagic Fish production'})
                  .rename(columns={'Commodity Balances - Livestock and Fish Primary Equivalent - Crustaceans - 2765 - Production - 5510 - tonnes': 'Crustaceans production', 'Commodity Balances - Livestock and Fish Primary Equivalent - Cephalopods - 2766 - Production - 5510 - tonnes': 'Cephalopods production'})
                  .rename(columns={'Commodity Balances - Livestock and Fish Primary Equivalent - Demersal Fish - 2762 - Production - 5510 - tonnes': 'Demersal Fish production', 'Commodity Balances - Livestock and Fish Primary Equivalent - Freshwater Fish - 2761 - Production - 5510 - tonnes': 'Freshwater Fish production'})
                  .rename(columns={'Commodity Balances - Livestock and Fish Primary Equivalent - Molluscs, Other - 2767 - Production - 5510 - tonnes': 'Molluscs and other production', 'Commodity Balances - Livestock and Fish Primary Equivalent - Marine Fish, Other - 2764 - Production - 5510 - tonnes': 'Marine Fish and other production'})
                  .rename(columns={'Industrial (large-scale commercial)':'Industrial fisheries'}))
    
    df_cleaned['Pelagic Fish production'] = df_cleaned['Pelagic Fish production']+ df_cleaned['Crustaceans production']+ df_cleaned['Cephalopods production'] + df_cleaned['Demersal Fish production']+ df_cleaned['Molluscs and other production'] + df_cleaned['Marine Fish and other production'] 
    df_cleaned = df_cleaned.drop(['Crustaceans production', 'Cephalopods production','Demersal Fish production', 'Molluscs and other production', 'Marine Fish and other production'], axis=1)
    
    return df_cleaned