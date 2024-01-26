from selenium import webdriver
from selenium.webdriver.chrome.service import Service

from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

import pandas as pd

## @brief scraping data from tipsport.cz
#  @param driver webdriver set up in the function scrape_league
#  @return dataframe with the data from the given url
def scrape_data(driver):
    matches_played = [match.text for match in driver.find_elements(By.CSS_SELECTOR, "span.o-matchRow__matchName") if match.text != "1.anglická f.l. 2023/2024 - celkově"]
    odds = [float(odd.text) if odd.text != "" else 0 for odd in driver.find_elements(By.CSS_SELECTOR, "div.btnRate")]
    individ_odds = [odds[i:i+5] for i in range(0, len(odds), 5)]

    data = dict(zip(matches_played, individ_odds))
    return pd.DataFrame.from_dict(data, orient="index")

## @brief scraping data from from the given url
#  @param url url of the league
#  @param driver webdriver set up in the function dataframe_create
#  @return the function scrape_data 
def scrape_league(url, driver, dataframe=None):
    driver.get(url)
    curr_data = scrape_data(driver)
    if dataframe is None:
        return curr_data
    else:
        return pd.concat([dataframe, curr_data], axis=0)

## @brief creating the final dataframe
#  @return final_df the final dataframe
def dataframe_create():
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)
    
    final_df = scrape_league("https://www.tipsport.cz/kurzy/fotbal/fotbal-muzi/1-anglicka-liga-118", driver)
    final_df = scrape_league("https://www.tipsport.cz/kurzy/fotbal/fotbal-muzi/1-nemecka-liga-130", driver, final_df)
    final_df = scrape_league("https://www.tipsport.cz/kurzy/fotbal/fotbal-muzi/1-spanelska-liga-140", driver, final_df)
    final_df = scrape_league("https://www.tipsport.cz/kurzy/fotbal/fotbal-muzi/1-italska-liga-127", driver, final_df)
    final_df = scrape_league("https://www.tipsport.cz/kurzy/fotbal/fotbal-muzi/1-francouzska-liga-124", driver, final_df)
    final_df = scrape_league("https://www.tipsport.cz/kurzy/fotbal/fotbal-muzi/1-slovenska-liga-138", driver, final_df)
    final_df = scrape_league("https://www.tipsport.cz/kurzy/fotbal/fotbal-muzi/1-ceska-liga-120", driver, final_df)
    final_df = scrape_league("https://www.tipsport.cz/kurzy/fotbal/fotbal-muzi/1-nizozemska-liga-125", driver, final_df)
    final_df = scrape_league("https://www.tipsport.cz/kurzy/fotbal/fotbal-muzi/1-turecka-liga-142", driver, final_df)
    final_df = scrape_league("https://www.tipsport.cz/kurzy/fotbal/fotbal-muzi/1-portugalska-liga-133", driver, final_df)
    
    driver.quit()
    
    final_df.columns = ["1", "1X", "X", "X2", "2"]
    final_df.index.name = "Match"
    return final_df