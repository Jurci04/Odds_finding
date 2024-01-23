from dataframes import create_dataframe

import pandas as pd
import matplotlib.pyplot as plt

#Function that checks if the odds from the dataframe are in the users range
def check_odd(val, odd_from, odd_to):
    if odd_from <= val <= odd_to:
        return val
    else:
        return None
    
#Getting the user odds input
while(True):
    try:
        odd_from = float(input("Enter the odds you want to show - from: "))
        odd_to = float(input("To: "))
        break
    except ValueError:
        print("Please enter a valid number!")

#Creating the final dataframe
final_df = create_dataframe()

#Finding the average odds
average_odds = final_df.melt().value.mean()

#Finding the desired odds
interesting_odds = final_df.map(lambda x: check_odd(x, odd_from, odd_to))

#Printing the desired odds
for match in interesting_odds.index:
    for col in interesting_odds.columns:
        if pd.notna(interesting_odds.loc[match, col]):
            print(f"{match} - {col}: {interesting_odds.loc[match, col]}")
print("")

#Printing the average odds
print(f"Average odds of all matches: {round(average_odds, 2)}")

#Flattening the dataframe
flattened_ods = final_df.melt().value

# Plotting the histogram
flattened_ods.hist(bins=60, color="blue", edgecolor="black", linewidth=1.2)

plt.title("Histogram of odds")
plt.xlabel("Odds")
plt.ylabel("Frequency")
plt.axvline(average_odds, color="red", linestyle="dashed", linewidth=1.2, label="Average odds")
plt.show()