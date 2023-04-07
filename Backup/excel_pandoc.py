import pandas as pd
import os

dir_path = os.getcwd()


df = pd.DataFrame()
temp = pd.read_excel(dir_path + "/친선대회.xlsx", sheet_name=1)
temp = temp.iloc[temp["Unnamed: 0"].dropna().index,:]
temp.reset_index(drop=True, inplace=True)

Match = temp.iloc[1,1]
Game = temp.iloc[2,8]
Date = temp.iloc[4,1]
Year = Date.year

s = temp['Unnamed: 0'].str.endswith(pat="고등학교").tolist()
e = temp['Unnamed: 0'].str.endswith(pat="TOTAL").tolist()

School_1 = temp.iloc[temp[s].index[0], 0]
School_2 = temp.iloc[temp[s].index[1], 0]

School_which = temp[s].index
Total_which = temp[e].index

Team_A = temp.iloc[School_which[0]+1:Total_which[0],:]
Team_B = temp.iloc[School_which[1]+1:Total_which[1],:]
Team_A.insert(0, "Team", School_1)
Team_B.insert(0, "Team", School_2)
temp = pd.concat([Team_A, Team_B], ignore_index=True)
temp.columns = ["team", "name", "Starting", "Back_num", "SCOR_1Q", "SCOR_2Q","SCOR_3Q","SCOR_4Q", "SCOR_EX", "SCOR_TOT",
    "game_time", "kpi_2p", "kpi_2pA", "kpi_2pp%", "kpi_3p", "kpi_3pA", "kpi_3pp", "kpi_FGp", "kpi_FT", "kpi_FTA",
    "kpi_FTp", "kpi_REB_OR", "kpi_REB_DF", "kpi_REB_TOT", "kpi_AS", "kpi_ST", "kpi_GD", "kpi_BS", "kpi_PF_w", "kpi_PF_wo",
    "kpi_PF_TOT", "kpi_TO", "kpi_TF"]
temp.insert(0, "match", Match)
temp.insert(1, "year", Year)
temp.insert(2, "game", Game)
temp.insert(3, "date", Date)

df = pd.concat([df, temp], ignore_index=True)    
df = df.drop(df.iloc[:,6:13], axis=1)
print(df.columns)