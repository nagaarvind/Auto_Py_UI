import pandas as pd
import openpyxl as op
import datetime
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import argparse
from pathlib import Path
from UI import opnFile


# https://rowannicholls.github.io/python/graphs/time_data.html
def averageTime(arr):
    tot = 0
    for item in arr:
        t = datetime.time(int(item[0:2]),int(item[3:5]))
        seconds = (t.hour * 60 + t.minute) * 60 + t.second
        tot = tot + seconds
    return datetime.timedelta(seconds=tot//len(arr))


def plotGraph(inTime,outTime,date):
    # creating date with given date list
    newDate = []
    for item in date:
        newDate.append(datetime.date(2023,int(item[3:5]),int(item[0:2])))    

    newInTime = []
    for item in inTime:
        temp = item.split(".")
        newInTime.append(datetime.time(int(temp[0]),int(temp[1])))

    newOutTime = []
    for item in outTime:
        temp = item.split(".")
        newOutTime.append(datetime.time(int(temp[0]),int(temp[1])))

    fig, ax = plt.subplots(nrows=2)
    # # Convert to datetime.datetime object by adding a time to the date
    plotDate = [datetime.datetime.combine(d, datetime.datetime.min.time()) for d in newDate]
    
    plotInTime = [datetime.datetime.combine(datetime.date.today(), t) for t in newInTime]

    plotOutTime = [datetime.datetime.combine(datetime.date.today(), t) for t in newOutTime]


    ax[0].plot(plotDate, plotInTime)
    
    ax[1].plot(plotDate, plotOutTime)

    ax[0].set_xticks(newDate)
    ax[1].set_xticks(newDate)
    # Re-format the x-axis
    fmt = mdates.DateFormatter('%d/%m')
    ax[0].xaxis.set_major_formatter(fmt)

    fmt = mdates.DateFormatter('%H:%M')
    ax[0].yaxis.set_major_formatter(fmt)

    fmt = mdates.DateFormatter('%d/%m')
    ax[1].xaxis.set_major_formatter(fmt)

    fmt = mdates.DateFormatter('%H:%M')
    ax[1].yaxis.set_major_formatter(fmt)

    plt.grid()
    plt.show()
    
# show the plot
    # plt.ylim(8.00,10.00)
    # df.plot.line()
    # data_dict = {
    #              'InTime': inTime,
    #              'OutTime': outTime,
    #              'Date': plotDate,
    #              }
    # creating a data frame object
    # df = pd.DataFrame(data_dict,index=pd.date_range(start="8:00",periods=22,freq="15min"))
    # df = pd.DataFrame(data_dict)
    
    # df.plot(kind='line',
    #     x='Date',
    #     y=['InTime','OutTime'],
    #     color=['red','blue']
    #     )
    # plt.grid()
    # plt.show()


arr = []
inTime = []
outTime = []
listOfDate = []
# To get path of the file in Command Line
# parser = argparse.ArgumentParser()
# parser.add_argument("file_path", type=Path)

# p = parser.parse

# filename = opnFile()


df = pd.read_excel(filename)


workingDays = df.at[0,'Total Days Worked']

for i in range(12,43):
    if type(df.iat[0,i]) != str:
        continue
    elif(df.iat[0,i] == "WEEKLY OFF"):
        continue
    else:
        arr.append(df.iat[0,i])
        date = df.columns[i]
        listOfDate.append(date[0:5])


# for item in arr:
#     inTime.append(item[0:5])
#     outTime.append(item[12:17])

for item in arr:

    # intime.append(item[0:5])

    # outtime.append(item[12:17])
    int_time = item[0:5]
    if ":" in int_time:
        int_time= int_time.replace(":",".")
    inTime.append(int_time)
    
    out_time = item[12:17]
    if ":" in out_time:
        out_time = out_time.replace(":",".")
    outTime.append(out_time)


# print(inTime)
plotGraph(inTime,outTime,listOfDate)
