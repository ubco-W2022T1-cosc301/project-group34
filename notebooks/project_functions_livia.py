## Method Chaining
import pandas

def load_and_process(url):
    
    df = pandas.read_csv(url)
    
    df1 = {
        df.copy().drop(['Code'], axis=1)
    }
    
    df2 = {
        df1
        .rename(columns={'Share of fish stocks within biologically sustainable levels (FAO, 2020)': 'Biologically sustainable fish stocks', 'Share of fish stocks that are overexploited': 'Overexploited fish stocks'})
        .rename(columns={'Capture fisheries production (metric tons)': 'Capture fisheries production'})
        .rename(columns={'Fish, Seafood- Food supply quantity (kg/capita/yr) (FAO, 2020)' : 'Fish, Seafood- Food supply quantity'})
        .rename(columns={'Commodity Balances - Livestock and Fish Primary Equivalent - Freshwater Fish - 2761 - Production - 5510 - tonnes' : 'Livestock and Fish Primary Equivalent - Freshwater Fish'})
    }
    
    return df1

