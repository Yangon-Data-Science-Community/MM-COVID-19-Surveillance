# importing the libraries
from bs4 import BeautifulSoup
from datetime import date, datetime
import pandas as pd
from get_source_html import get_source_worldometers
from utils import *

today = date.today()
today_str = today.strftime("%Y%m%d")
today_format = today.strftime("%d-%m-%Y")
timestamp = int(datetime.now().timestamp()*1000)

def filter_data(filename):
    html_content = open(filename, "r")
    soup = BeautifulSoup(html_content, 'html.parser')
    # soup = BeautifulSoup(html_content, "lxml")
    # print(soup.prettify()) # print the parsed data of html

    # Step 3: Analyze the HTML tag, where your content lives
    # Create a data dictionary to store the data.
    data = {}
    # Get the table
    gdp_table = soup.find("table", attrs={"id": "main_table_countries_today"})
    gdp_table_thead = gdp_table.thead.find_all("th")
    # Get all the headings of Lists
    headings = ["Date","No"]
    for td in gdp_table_thead:
        # remove any newlines and extra spaces from left and right
        value = td.text.replace('\n', '').strip().lower()
        if "country" in value:
            headings.append("Country_Code")
        elif "totalcases" in value:
            headings.append("No_Of_Confirmed")
        elif "newcases" in value:
            headings.append("New_Confirmed")
        elif "totaldeaths" in value:
            headings.append("No_Of_Death")
        elif "newdeaths" in value:
            headings.append("New_Death")
        elif "totalrecovered" in value:
            headings.append("Total_Recovered")
        elif "activecases" in value:
            headings.append("Active_Cases")
        elif "serious,critical" in value:
            headings.append("Serious_Critical")
        elif "tot" in value:
            headings.append("Total_Cases_1M_pop")
        elif "deaths/1m pop" in value:
            headings.append("Death_Cases_1M_pop")
        elif("totaltests") in value:
            headings.append("Total_Test")
        elif("tests/1m pop") in value:
            headings.append("Test_1M pop")
        elif("continent") in value:
            headings.append("Proviance_Code")
        elif("population") in value:
            headings.append("Population")
        else:
            print(value)
    headings.append("System_Date")
    gdp_table_tbody = gdp_table.tbody.find_all("tr")
    final_data = []
    for each in gdp_table_tbody:
        data_values = [today_format]
        for i, td in enumerate(each.find_all("td")):
            td_value = td.text.replace("+", "")
            td_value = td_value.replace("-", "")
            td_value = td_value.replace(",", "")
            td_value = td_value.replace("\n", "")
            if td_value == " ":
                td_value = ""
            try:
                td_value = float(td_value)
            except:
                pass
            data_values.append(td_value)
        data_values.append(timestamp)
        data_dict = dict(zip(headings, data_values))
        final_data.append(data_dict)

    # Step 4: Export the data to csv
    final_data_pd = pd.DataFrame(final_data)
    final_data_pd = final_data_pd.drop('No', 1)
    return final_data_pd


# Main application
if __name__ == "__main__":
    # step 1: process the data
    html_filename = "source_html_worldometers_"+today_str+".html"
    if os.path.isfile(html_filename) is False:
        print(today_str, " Data Source fetching..")
        get_source_worldometers()


    # step 2: left with insert data to the db
    data_to_store = filter_data(html_filename)
    engine = db_engine()
    data_to_store.to_sql('Worldometer_Dashboard_Detail', con = engine, if_exists = 'append', chunksize = 1000, index=False)

    # step 3: clean up process
    if clear_up(html_filename):
        print("Data source successfully updated.")
        if db_engine_close(engine):
            print("db connection closed.")
