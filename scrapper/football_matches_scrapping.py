from selenium import webdriver
from selenium.webdriver.chrome.service import Service

from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

import pandas as pd

#URLS for different sites:
url_tipsport = "https://www.tipsport.cz/kurzy/fotbal/fotbal-muzi--1?limit=525"

words_to_exclude = {"2023/2024", "celkově", "speciál"}
## @brief scraping data from tipsport.cz
# The function gets the match ID from the website and based on that it gets the odds for the match
#  @param driver webdriver set up in the function scrape_league
#  @return dictionary with the data from the given url
def scrape_data(driver):
    matches_played = []
    match_ids = []
    odds = []
    for match in driver.find_elements(By.CSS_SELECTOR, "span.o-matchRow__matchName > span"):
        if match.text != "" and not any(word in match.text for word in words_to_exclude):
            matches_played.append(match.text)
            match_id = match.get_attribute("data-m")
            match_ids.append(match_id)
    
    for odd in driver.find_elements(By.CSS_SELECTOR, "div.btnRate"):
        data_atribute = odd.get_attribute("data-atid")
        odd_id = data_atribute.split('||')[-2]
        if odd_id in match_ids:
            odds.append(float(odd.text) if odd.text != "" else 0)
    
    #pairing the odds in groups of 5
    odds = [odds[i:i+5] for i in range(0, len(odds), 5)]
    
    data = dict(zip(matches_played, odds))
    return data


## @brief creating a dataframe with the data from the given url
#  Function creates its own webdriver and then calls the function scrape_data to make the dataframe from url containing all the matches
#  @return dataframe with the data from the given url
def create_dataframe():    
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)

    driver.get(url_tipsport)

    final_df = pd.DataFrame.from_dict(scrape_data(driver), orient="index")
    
    driver.quit()
    
    final_df.columns = ["1", "1X", "X", "X2", "2"]
    final_df.index.name = "Match"

    return final_df