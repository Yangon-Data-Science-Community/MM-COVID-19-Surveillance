<!-- To do list -->

##### **Initial Data** based on [Source](https://github.com/theananda/myanmar-covid19-data)

### Web Scraping for Myanmar Covid-19 Data
1. Install Chrome Driver and Selenium and required library - **Done**

    ```bash
    $ sudo bash chrome_driver_selenium.sh
    $ pip install -r requirements.txt
    ```
2. Get Source data from [Source 1](https://doph.maps.arcgis.com/apps/opsdashboard/index.html#/f8fb4ccc3d2d42c7ab0590dbb3fc26b8) , [Source 2](https://www.worldometers.info/coronavirus/) and processed data- **Done**

    ```bash
    $ python update_MOHS_Dashboard_Data.py
    $ python update_Worldometers_Data.py
    ```
