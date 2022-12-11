# financial_analysis

To analyze a batch of stocks in order to determine the upcoming year's trading strategy by creating python script without third party modules like pandas and numpy.


## Data and Output
This script will request financial data for 2022 from an API, save this data into a csv, and then generate a comprehensive report using this generated csv.
Focuses on analyzing 5 stock ticker  in order to demonstrate the functionality of this pipeline. For example, to analyze Google, Amazon, Coursera, Netflix, and Facebook,  utilize the following names : `GOOG`, `AMZN`, `COUR`, `NFLX`, and `META`.


#Files:

extract.py
 
Specifically, this script will utilize the [Polygon API](https://polygon.io/) in order to request stock data. Then write data into a csv file using the [csv](https://docs.python.org/3/library/csv.html) module. 

analysis.py

Within this file using the subequent csv files to generate a report on each respective stock's population standard deviation of each week for both 2021 & 2022. 

stock.png
generates one line plot for each stock using mathplotlib
