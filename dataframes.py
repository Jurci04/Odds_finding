from scrapper import football_matches_scrapping as fms

import pandas as pd

def create_dataframe():
    #Getting the data
    data_premier_league = fms.english_premier_league()
    data_la_liga = fms.spanish_la_liga()
    data_bundesliga = fms.german_bundesliga()
    data_serie_a = fms.italian_serie_a()
    data_ligue_1 = fms.french_ligue_1()

    #Creating individual dataframes
    df_premier_league = pd.DataFrame(data_premier_league)
    df_la_liga = pd.DataFrame(data_la_liga)
    df_bundesliga = pd.DataFrame(data_bundesliga)
    df_serie_a = pd.DataFrame(data_serie_a)
    df_ligue_1 = pd.DataFrame(data_ligue_1)

    #Creating the final dataframe
    final_df = pd.concat([df_premier_league, df_la_liga, df_bundesliga, df_serie_a, df_ligue_1], axis=1)
    final_df = final_df.T

    final_df.columns = ["1", "1X", "X", "X2", "2"]
    final_df.index.name = "Match"
    return final_df