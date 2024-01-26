from scrapper import football_matches_scrapping as fms
from analyzing_functions import check_odd, best_odds

import pandas as pd
    
#Getting the user odds input
while(True):
    try:
        odd_from = float(input("Enter the odds you want to show - from: "))
        odd_to = float(input("To: "))
        break
    except ValueError:
        print("Please enter a valid number!")


final_df = fms.dataframe_create()

average_odds = final_df.melt().value.mean()

interesting_odds = final_df.map(lambda x: check_odd(x, odd_from, odd_to))

best_odds = best_odds(final_df)


#Printing the desired odds
for match in interesting_odds.index:
    for col in interesting_odds.columns:
        if pd.notna(interesting_odds.loc[match, col]):
            print(f"{match} - {col}: {interesting_odds.loc[match, col]}")
print("")

#Printing the average odds
print(f"Average odds of all matches: {round(average_odds, 2)}")
print("")

#Printing the best odds
print("Best odds:")
for match in best_odds.index:
    for col in best_odds.columns:
        if pd.notna(best_odds.loc[match, col]):
            print(f"{match} - {col}: {best_odds.loc[match, col]}")