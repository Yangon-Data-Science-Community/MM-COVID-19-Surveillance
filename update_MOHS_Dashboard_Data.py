from bs4 import BeautifulSoup
from datetime import date
import pandas as pd
import csv
import os.path
from get_source_html import get_source

today = date.today()
today_str = today.strftime("%Y%m%d")


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

def append_current_csv(html_filename):
    """Updated the current csv summary data after scraping."""
    summary, township = filter_data(html_filename)
    # Summary
    previous_data = pd.read_csv(
        "./myanmar-covid19-data/MOHS_Dashboard_Data/MOHS Dashboard Data-Summary.csv")

    # replace data if today existed in the file
    today_format = today.strftime("%d-%m-%Y")
    exist = False
    for i, each in enumerate(previous_data["Date"]):
        if today_format == each:
            exist = True
            index_to_delete = i
    # remove the previous record
    if exist:
        # Delete row with index i
        previous_data = previous_data.drop(index_to_delete)

    today_data = pd.DataFrame(columns=previous_data.columns)
    today_data = today_data.append(
        {'Date': today_format,
         'Tested': summary[0],
         'PUI': summary[1],
         'Confirmed': summary[2],
         'Death': summary[3],
         'Recovered': summary[4]
         },
        ignore_index=True)
    updated = pd.concat([previous_data, today_data])
    updated.to_csv(
        "./MOHS-Dashboard-Data-Summary.csv", index=False)

    # for Township
    today_township_data = pd.DataFrame(columns=['SR','Township','Case'])
    today_township_data = today_township_data.append(township,ignore_index=True)
    today_township_data.to_csv("./MOHS Dashboard Data.csv", index=False)

def clear_up(filename):
    """Delete the processed file>"""
    os.remove(filename)


# Main application
if __name__ == "__main__":
    html_filename = "source_html_"+today_str+".html"
    if os.path.isfile(html_filename):
        append_current_csv(html_filename)
        clear_up(html_filename)
    else:
        if(get_source()):
            append_current_csv(html_filename)
            clear_up(html_filename)
        else:
            print("Data Source is not ready to be processed.")
