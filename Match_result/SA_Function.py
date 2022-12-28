
from unittest import result
import numpy as np
import random
import pandas as pd
import scipy.stats as ss

def SA_Index(dataframe, version):
    df = pd.DataFrame(dataframe.replace(np.nan, 0))
    C_AT = df["2P"]*0.87 + df["FT"]*0.84 + df['REB_OR']*0.93
    C_Def= df["REB_DF"]*0.87 + df["BS"]*0.84 + df["GD"]*0.76 + df["ST"]*0.60
    C_PER= df["2P%"]*0.87 + df["3P%"]*0.60 + df["FT%"]*0.84
    F_AT = df["2P"]*0.86 + df["3P"]*0.88 + df["FT"]*0.84 + df['REB_OR']*0.74
    F_Def= df["REB_DF"]*0.69 + df["BS"]*0.64 + df["GD"]*0.73 + df["ST"]*0.67
    F_PER= df["2P%"]*0.86 + df["3P%"]*0.88 + df["FT%"]*0.84
    G_AT = df["2P"]*0.79 + df["3P"]*0.84 + df["AS"]*0.98 + df["FT"]*0.98 - df['TO']*0.87
    G_Def= df["REB_DF"]*0.59 + df["BS"]*0.47 + df["GD"]*0.72 + df["ST"]*0.89
    G_PER= df["2P%"]*0.79 + df["3P%"]*0.84 + df["FT%"]*0.84
    
    result = pd.concat([C_AT, C_Def, C_PER, F_AT, F_Def, F_PER, G_AT, G_Def, G_PER], axis=1)
    result.columns = ["C_AT", "C_Def", "C_PER", "F_AT", "F_Def", "F_PER", "G_AT", "G_Def", "G_PER"]
    
    if version == 1:
        result_z = ss.zscore(result, nan_policy='omit').copy() * 10 + 50
    elif version == 2:
        result_z = ss.zscore(result, nan_policy='omit').copy()
    else:
        print("version 확인. 1: t-score,  2: z-score")                                    
    return result_z


def SA_Weight(dataframe, weight=[5,3,2]):
    df = pd.DataFrame(np.nan_to_num(dataframe), columns=dataframe.columns)
    var_list = ["C", "F", "G"]
    
    for i in var_list:
        df[i+"_"+str(weight)]=df[i+"_AT"] * (weight[0] * 0.1)+\
            df[i+"_Def"] * (weight[1] * 0.1) +\
                df[i+"_PER"] * weight[2] * 0.1
    return df


def park_sample(df, n):
    sample = random.sample(range(df.shape[0]), n)
    
    return df.iloc[sample,:]