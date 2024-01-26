from scrapper import football_matches_scrapping as fms

import pandas as pd

## @brief Function that creates the final dataframe
# 
#  The function takes the data from the scrapper, creates individual dataframes
#  for each league and then concatenates them into one final dataframe
#
#  @return final_df the final dataframe
def create_dataframe():
    data_premier_league = fms.english_premier_league()
    data_la_liga = fms.spanish_la_liga()
    data_bundesliga = fms.german_bundesliga()
    data_serie_a = fms.italian_serie_a()
    data_ligue_1 = fms.french_ligue_1()
    data_slovak_nike_liga = fms.slovak_nike_liga()
    data_czech_1st_league = fms.czech_1st_league()
    data_dutch_eridivisie = fms.dutch_eridivisie()
    data_turkish_super_lig = fms.turkish_super_lig()

    df_premier_league = pd.DataFrame(data_premier_league)
    df_la_liga = pd.DataFrame(data_la_liga)
    df_bundesliga = pd.DataFrame(data_bundesliga)
    df_serie_a = pd.DataFrame(data_serie_a)
    df_ligue_1 = pd.DataFrame(data_ligue_1)
    df_slovak_nike_liga = pd.DataFrame(data_slovak_nike_liga)
    df_czech_1st_league = pd.DataFrame(data_czech_1st_league)
    df_dutch_eridivisie = pd.DataFrame(data_dutch_eridivisie)
    df_turkish_super_lig = pd.DataFrame(data_turkish_super_lig)

    #Final dataframe
    final_df = pd.concat([df_premier_league, df_la_liga, df_bundesliga, df_serie_a, df_ligue_1, df_slovak_nike_liga, df_czech_1st_league, df_dutch_eridivisie, df_turkish_super_lig], axis=1)
    final_df = final_df.T

    final_df.columns = ["1", "1X", "X", "X2", "2"]
    final_df.index.name = "Match"
    return final_df