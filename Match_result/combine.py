def result_combine(file_PATH):
    import pandas as pd
    import numpy as np
    import os
    
    file_list = os.listdir(file_PATH)
    file_list_xlsx = [file for file in file_list if file.endswith('.xlsx')]
    df = pd.DataFrame()

    for i in file_list xlsx:
        temp = pd.read_excel(PATH + "result/" + i, sheet_name= 1)
    temp = temp.iloc[temp["Unnamed: 0"].dropna().index,:]
    temp.reset_index(drop=True, inplace=True)

    Match = temp.iloc[1,1]
    Game = temp.iloc[2,8]

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
    temp.columns = ["Team", "Name", "Starting", "Back_num", "SCOR_1Q", "SCOR_2Q","SCOR_3Q","SCOR_4Q", "SCOR_EX", "SCOR_TOT",
        "Min", "2P", "2PA", "2P%", "3P", "3PA", "3P%", "FG%", "FT", "FTA",
        "FT%", "REB_OR", "REB_DF", "REB_TOT", "AS", "ST", "GD", "BS", "PF_W", "PF_WO",
        "PF_TOT", "TO", "TF"]
    temp.insert(0, "Match", Match)
    temp.insert(1, "Game", Game)

    df = pd.concat([df, temp], ignore_index=True)
    return df

