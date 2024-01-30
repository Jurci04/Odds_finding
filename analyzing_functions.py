import pandas as pd

## @brief Function that checks if the odds are in the desired range
#  @param val the value to be checked
#  @param odd_from the lower bound of the range
#  @param odd_to the upper bound of the range
#  @return val if it is in the range, None otherwise
def check_odd(val, odd_from, odd_to):
    if odd_from <= val <= odd_to:
        return val
    else:
        return None

## @brief Function that finds the best odds
# 
#  The function takes the check_odd function and applies the values 1.66 and 1.81
#
#  @param dataframe the dataframe to be checked
#  @return concatenated dataframe of the best odds
def best_odds(dataframe):
    best_odds_1 = dataframe["1"].map(lambda val: check_odd(val, 1.66, 1.73))
    best_odds_1X = dataframe["1X"].map(lambda val: check_odd(val, 1.66, 1.78))
    return pd.concat([best_odds_1, best_odds_1X], axis=1)