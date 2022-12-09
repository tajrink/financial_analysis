import csv
import statistics
import matplotlib.pyplot as plt


filenames=["GOOGL", "AMZN", "COUR", "NFLX", "AAPL"]


for file in filenames:
    data = []
    with open(f"data/{file}.csv", "r") as infile:
        reader = csv.DictReader(infile)
    # save this dictReader object into a list of dictionaries to analyze
        for row in reader:
            data.append(row)
    


    # get each week of stock data, 5 iterations at a time
    i = 0
    data_stdev = []


    while i < len(data):
        if  i+4>len(data):
            break
        day1 = float(data[i]["Closing_Price"])
        day2 = float(data[i + 1]["Closing_Price"])
        day3 = float(data[i + 2]["Closing_Price"])
        day4 = float(data[i + 3]["Closing_Price"])
        day5 = float(data[i + 4]["Closing_Price"])
            
        psd=statistics.pstdev([day1,day2,day3,day4,day5])
        data_stdev.append(psd)
    
            
        i+=5
        #mathplotlib

    plt.plot(data_stdev,label=f"{file}")
    plt.title('standard deviation for stock')
    plt.xlabel("Weeks")
    plt.ylabel("standard deviation")
    plt.legend(loc="upper left")
    plt.savefig("stock.png")
