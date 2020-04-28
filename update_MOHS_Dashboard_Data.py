from bs4 import BeautifulSoup
from datetime import date, datetime
import pandas as pd
import csv
import os.path
from get_source_html import get_source_mohs
from utils import *

today = date.today()
today_str = today.strftime("%Y%m%d")
today_format = today.strftime("%d-%m-%Y")
timestamp = int(datetime.now().timestamp()*1000)


def filter_data(filename):
    """Get the covid current summany from html file."""
    file_read = open(filename, "r")
    soup = BeautifulSoup(file_read, 'html.parser')
    all_main_info = soup.find_all("text")
    summary = []
    township = []
    for each in all_main_info:
        summary.append(float(each.text.replace(",", "")))
    all_township = soup.find_all("nav")
    for each in all_township:
        spans = each.find_all("span")
        if len(spans) > 0:
            for each in spans:
                inside_span = each.find_all("span")
                if len(inside_span) > 0:
                    obj = {}
                    township_n_region = inside_span[0].text.split(",")
                    if len(township_n_region) >= 2:
                        Township = inside_span[0].text.split(",")[0]
                        SR = inside_span[0].text.split(",")[1]
                        obj['Township'] = Township
                        obj['SR'] = SR
                        cases_raw = inside_span[5].text.split(":")
                        if len(cases_raw) >= 2:
                            cases = cases_raw[1]
                            obj['Case'] = cases
                            township.append(obj)
    return summary, township


def pre_processed_data(html_filename):
    """Updated the current csv summary data after scraping."""
    headers = ["Date", "No", "SR", "Township", "Case", "Tested", "PUI", "M", "F",
               "Child", "Adult", "Confirmed", "Death", "Recovered", "Latitude",
               "Longitude", "FID", "System_Date"]
    summary, township = filter_data(html_filename)

    township_summany = []

    # For whole country
    mm_dict = dict.fromkeys(headers)
    mm_dict['System_Date'] = timestamp
    mm_dict['Date'] = today_format
    mm_dict['SR'] = "Myanmar"
    mm_dict['Tested'] = summary[0]
    mm_dict['PUI'] = summary[1]
    mm_dict['Confirmed'] = summary[2]
    mm_dict['Death'] = summary[3]
    mm_dict['Recovered'] = summary[4]
    township_summany.append(mm_dict)

    # Township Summary
    refer_data = pd.read_csv(
        "./mm_township_refer.csv")

    for each_town in township:
        empty_dict = dict.fromkeys(headers)
        exist = False
        for i, each in enumerate(refer_data["Township"]):
            if each_town['Township'] == each:
                exist = True
                index_to_refer = i
        if exist:
            empty_dict['No'] = refer_data['No'].iloc[index_to_refer]
            empty_dict['SR'] = refer_data['SR'].iloc[index_to_refer].lstrip()
            empty_dict['Township'] = refer_data['Township'].iloc[index_to_refer].lstrip()
            empty_dict['Latitude'] = refer_data['Latitude'].iloc[index_to_refer]
            empty_dict['Longitude'] = refer_data['Longitude'].iloc[index_to_refer]
            empty_dict['FID'] = refer_data['FID'].iloc[index_to_refer]
        else:
            empty_dict['SR'] = each_town['SR'].lstrip()
            empty_dict['Township'] = each_town['Township'].lstrip()

        empty_dict['Case'] = each_town['Case']
        empty_dict['Confirmed'] = len(each_town['Case'].split(","))
        empty_dict['System_Date'] = timestamp
        empty_dict['Date'] = today_format

        township_summany.append(empty_dict)

    final_data_pd = pd.DataFrame(township_summany)
    return final_data_pd
  


# Main application
if __name__ == "__main__":
    # step 1: process the data
    html_filename = "source_html_mohs_"+today_str+".html"
    if os.path.isfile(html_filename) is False:
        print(today_str, " Data Source fetching..")
        get_source_mohs()

    # step 2: left with insert data to the db
    data_to_store = pre_processed_data(html_filename)
    engine = db_engine()
    data_to_store.to_sql('MOHS_Dashboard_Detail', con = engine, if_exists = 'append', chunksize = 1000, index=False)

    # step 3: clean up process
    if clear_up(html_filename):
        print("Data source successfully updated.")
        if db_engine_close(engine):
            print("db connection closed.")
